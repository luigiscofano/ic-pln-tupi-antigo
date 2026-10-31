"""Adaptador opcional Tesseract. Não baixa modelos nem chama APIs externas."""

from pathlib import Path
import subprocess, shutil


def extrair(imagem, idioma="por", psm=6):
    if not Path(imagem).is_file():
        raise FileNotFoundError(imagem)
    if not idioma.replace("+", "").replace("_", "").isalnum():
        raise ValueError("Idioma inválido")
    if not isinstance(psm, int) or not 0 <= psm <= 13:
        raise ValueError("PSM inválido")
    comando = shutil.which("tesseract")
    if comando is None:
        raise RuntimeError("Instale Tesseract e o modelo de idioma separadamente")
    result = subprocess.run(
        [
            comando,
            str(Path(imagem).resolve()),
            "stdout",
            "-l",
            idioma,
            "--psm",
            str(psm),
        ],
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True,
        timeout=120,
    )
    return result.stdout
