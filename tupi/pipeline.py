"""Fluxo conservador para dados já estruturados: preserva originais e sinaliza revisão."""

from pathlib import Path
import csv, json, unicodedata
from collections import Counter

CAMPOS = ("id", "source_id", "page", "line", "lemma_raw", "pt_raw", "en_raw")


def importar_tsv(caminho):
    with Path(caminho).open(encoding="utf-8-sig", newline="") as arquivo:
        reader = csv.DictReader(arquivo, delimiter="\t")
        if reader.fieldnames != list(CAMPOS):
            raise ValueError("Cabeçalho TSV incompatível")
        registros = []
        ids = set()
        for linha in reader:
            if set(linha) != set(CAMPOS) or any(v is None for v in linha.values()):
                raise ValueError("Linha TSV malformada")
            if not linha["id"] or linha["id"] in ids:
                raise ValueError("ID vazio ou duplicado")
            if not linha["source_id"]:
                raise ValueError("Fonte ausente")
            for campo in ("page", "line"):
                if not linha[campo].isdigit() or int(linha[campo]) < 1:
                    raise ValueError("Página/linha devem ser positivos")
            ids.add(linha["id"])
            registro = dict(linha)
            # NFC é uma representação canônica, não uma correção ortográfica.
            registro.update(
                lemma_nfc=unicodedata.normalize("NFC", linha["lemma_raw"]),
                status="pending_review",
            )
            registros.append(registro)
    return registros


def auditar(registros):
    frequencias = Counter(r["lemma_nfc"] for r in registros)
    alertas = []
    for r in registros:
        flags = []
        if not r["lemma_raw"].strip():
            flags.append("empty_lemma")
        if not r["pt_raw"].strip():
            flags.append("missing_pt")
        if not r["en_raw"].strip():
            flags.append("missing_en")
        if frequencias[r["lemma_nfc"]] > 1:
            flags.append("possible_homograph_or_duplicate")
        texto = "".join(r[k] for k in ("lemma_raw", "pt_raw", "en_raw"))
        if "\ufffd" in texto:
            flags.append("replacement_character")
        if any(unicodedata.category(c) == "Cc" and c not in "\n\t\r" for c in texto):
            flags.append("control_character")
        if r["lemma_raw"] != r["lemma_nfc"]:
            flags.append("canonical_unicode_change")
        if flags:
            alertas.append({"id": r["id"], "flags": flags})
    return {
        "records": len(registros),
        "flagged_records": len(alertas),
        "alerts": alertas,
        "linguistic_validation": False,
    }


def exportar_jsonl(registros, caminho):
    Path(caminho).write_text(
        "".join(
            json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in registros
        ),
        encoding="utf-8",
    )


def exportar_csv(registros, caminho):
    campos = [*CAMPOS, "lemma_nfc", "status"]
    with Path(caminho).open("w", encoding="utf-8-sig", newline="") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(registros)
