from pathlib import Path
import nbformat, json
from nbclient import NotebookClient
from nbconvert import HTMLExporter

root = Path(__file__).resolve().parents[1]
build = root / "build"
build.mkdir(exist_ok=True)
resultados = []
for caminho in sorted((root / "notebooks").glob("*.ipynb")):
    nb = nbformat.read(caminho, as_version=4)
    nbformat.validate(nb)
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    NotebookClient(
        nb,
        timeout=120,
        kernel_name="python3",
        resources={"metadata": {"path": str(root)}},
    ).execute()
    nbformat.write(nb, build / caminho.name)
    html, _ = HTMLExporter().from_notebook_node(nb)
    (build / (caminho.stem + ".html")).write_text(html, encoding="utf-8")
    resultados.append(
        {
            "notebook": caminho.name,
            "passou": True,
            "modo": "kernel Jupyter novo via nbclient",
        }
    )
    print("PASS", caminho.name)
(build / "notebooks.json").write_text(
    json.dumps(resultados, indent=2) + "\n", encoding="utf-8"
)
# O acervo histórico requer Colab e upload manual: validar esquema, não executar.
for caminho in (root / "acervo").glob("*.ipynb"):
    nb = nbformat.read(caminho, as_version=4)
    nbformat.validate(nb)
    assert all(
        not c.get("outputs") and c.get("execution_count") is None
        for c in nb.cells
        if c.cell_type == "code"
    )
