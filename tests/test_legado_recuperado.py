"""Caracterização técnica das regras recuperadas; não é avaliação linguística."""
import csv
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tupi.legado import clean_text, normalize_navarro
from tupi.pipeline import importar_tsv


class LegadoRecuperadoTest(unittest.TestCase):
    def test_limpeza_unicode_e_pontuacao(self):
        self.assertEqual(clean_text(None), "")
        self.assertEqual(clean_text("  a\u0303  –  b ’ c  "), "ã-b'c")
        self.assertEqual(clean_text(""), "")

    def test_excecoes_registradas(self):
        # São saídas especificadas no código recuperado, não gabaritos linguísticos.
        for original, proposta in [("AI", "AÎ"), ("AIPI", "AÎPI"), ("AIA", "ÃÎA")]:
            with self.subTest(original=original):
                self.assertEqual(normalize_navarro(original), proposta)
        self.assertEqual(normalize_navarro("  "), "")

    def test_importacao_padrao_nao_aplica_legado(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "teste.tsv"
            path.write_text(
                "id\tsource_id\tpage\tline\tlemma_raw\tpt_raw\ten_raw\n"
                "1\tsintetico\t1\t1\tAI\tFixture\tFixture\n",
                encoding="utf-8",
            )
            registro = importar_tsv(path)[0]
            self.assertEqual(registro["lemma_raw"], "AI")
            self.assertEqual(registro["lemma_nfc"], "AI")
            self.assertEqual(registro["status"], "pending_review")


if __name__ == "__main__":
    unittest.main()
