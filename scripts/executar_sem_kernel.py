from pathlib import Path
import os, sys, json, nbformat
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output

root = Path(__file__).resolve().parents[1]
os.chdir(root)
p = root / "notebooks/01_auditoria_reproduzivel.ipynb"
n = nbformat.read(p, as_version=4)
shell = InteractiveShell.instance()
count = 0
for cell in n.cells:
    if cell.cell_type != "code":
        continue
    count += 1
    with capture_output() as captured:
        res = shell.run_cell(cell.source, store_history=True)
    if res.error_before_exec or res.error_in_exec:
        raise RuntimeError(captured.stdout + captured.stderr)
    cell.execution_count = count
    cell.outputs = []
    for name, text in [("stdout", captured.stdout), ("stderr", captured.stderr)]:
        if text:
            cell.outputs.append(nbformat.v4.new_output("stream", name=name, text=text))
n.metadata["validacao_local"] = {
    "modo": "IPython em processo novo; sem servidor/kernel Jupyter",
    "celulas_aprovadas": count,
}
nbformat.write(n, p)
print("PASS:", count, "celulas IPython; Jupyter sera validado na CI")
