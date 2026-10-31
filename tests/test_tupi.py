import unittest, tempfile, json, csv, unicodedata
from pathlib import Path
from tupi import (
    importar_tsv,
    auditar,
    exportar_csv,
    exportar_jsonl,
    distancia,
    cer,
    wer,
)

ROOT = Path(__file__).resolve().parents[1]


class TestTupi(unittest.TestCase):
    def test_preservacao(self):
        registros = importar_tsv(ROOT / "data/demo.tsv")
        self.assertEqual(len(registros), 3)
        self.assertTrue(all(r["status"] == "pending_review" for r in registros))
        self.assertEqual(registros[1]["en_raw"], "")

    def test_auditoria(self):
        a = auditar(importar_tsv(ROOT / "data/demo.tsv"))
        self.assertEqual(a["records"], 3)
        self.assertEqual(a["flagged_records"], 2)
        self.assertFalse(a["linguistic_validation"])

    def test_csv_json_roundtrip(self):
        r = importar_tsv(ROOT / "data/demo.tsv")
        r[0]["pt_raw"] = 'aspas " e, vírgula\nlinha'
        with tempfile.TemporaryDirectory() as d:
            j = Path(d) / "out.jsonl"
            c = Path(d) / "out.csv"
            exportar_jsonl(r, j)
            exportar_csv(r, c)
            self.assertEqual(
                [json.loads(l) for l in j.read_text(encoding="utf-8").splitlines()], r
            )
            with c.open(encoding="utf-8-sig", newline="") as f:
                self.assertEqual(list(csv.DictReader(f)), r)

    def test_unicode_nao_apaga_diacriticos(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "x.tsv"
            p.write_text(
                "id\tsource_id\tpage\tline\tlemma_raw\tpt_raw\ten_raw\n1\tx\t1\t1\ta\u0303\tp\te\n",
                encoding="utf-8",
            )
            r = importar_tsv(p)
            self.assertEqual(r[0]["lemma_raw"], "a\u0303")
            self.assertEqual(r[0]["lemma_nfc"], "ã")
            self.assertIn("canonical_unicode_change", auditar(r)["alerts"][0]["flags"])

    def test_invalidos(self):
        base = (ROOT / "data/demo.tsv").read_text(encoding="utf-8")
        for bad in [
            base.replace("source_id", "fonte"),
            base.replace("2\tsintetico", "1\tsintetico"),
            base.replace("\t1\t1\tEXEMPLO", "\t0\t1\tEXEMPLO"),
            base + "4\tx\t1\n",
        ]:
            with self.subTest(bad=bad), tempfile.TemporaryDirectory() as d:
                p = Path(d) / "x.tsv"
                p.write_text(bad, encoding="utf-8")
                with self.assertRaises(ValueError):
                    importar_tsv(p)

    def test_metricas(self):
        self.assertEqual(distancia("kitten", "sitting"), 3)
        self.assertAlmostEqual(cer("abc", "axc"), 1 / 3)
        self.assertEqual(wer("a b", "a x b"), 0.5)
        self.assertEqual(cer("a", "aaa"), 2)

    def test_referencia_vazia(self):
        for f in [cer, wer]:
            with self.assertRaises(ValueError):
                f("", "x")

    def test_homografos_preservados(self):
        r = importar_tsv(ROOT / "data/demo.tsv")
        self.assertEqual(r[0]["lemma_nfc"], r[1]["lemma_nfc"])
        self.assertNotEqual(r[0]["id"], r[1]["id"])

    def test_distancia_oraculo(self):
        import itertools

        for a in ["", "a", "ab", "aba"]:
            for b in ["", "a", "ba", "bbbb"]:
                tabela = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
                for i in range(len(a) + 1):
                    tabela[i][0] = i
                for j in range(len(b) + 1):
                    tabela[0][j] = j
                for i in range(1, len(a) + 1):
                    for j in range(1, len(b) + 1):
                        tabela[i][j] = min(
                            tabela[i - 1][j] + 1,
                            tabela[i][j - 1] + 1,
                            tabela[i - 1][j - 1] + (a[i - 1] != b[j - 1]),
                        )
                self.assertEqual(distancia(a, b), tabela[-1][-1])


if __name__ == "__main__":
    unittest.main()
