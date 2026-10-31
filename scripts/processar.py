from pathlib import Path
import argparse, json, sys

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from tupi import importar_tsv, auditar, exportar_csv, exportar_jsonl

p = argparse.ArgumentParser()
p.add_argument("entrada", type=Path)
p.add_argument("--saida", type=Path, default=Path("build"))
a = p.parse_args()
registros = importar_tsv(a.entrada)
relatorio = auditar(registros)
a.saida.mkdir(parents=True, exist_ok=True)
exportar_csv(registros, a.saida / "registros.csv")
exportar_jsonl(registros, a.saida / "registros.jsonl")
(a.saida / "auditoria.json").write_text(
    json.dumps(relatorio, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(
    json.dumps(
        {
            "records": len(registros),
            "flagged_records": relatorio["flagged_records"],
            "linguistic_validation": False,
        }
    )
)
