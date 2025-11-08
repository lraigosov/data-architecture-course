#!/usr/bin/env python
"""Validador simple de notebooks del curso.

Objetivo:
- Comprobar presencia de secciones mínimas en la primera parte del notebook.
- Generar un reporte agregando cumplimiento por archivo.

Criterios (heurísticos, no estrictos):
1. Primera celda Markdown debe contener título (# )
2. Debe existir alguna celda Markdown con la palabra 'Objetivo' o 'Objetivos'
3. Debe existir una sección 'Ejercicios' o 'Ejercicio'
4. Debe existir una sección 'Referencias'

Uso:
    python scripts/validate_notebooks.py --path .

Limitaciones:
- No ejecuta código ni valida reproducibilidad.
- Heurístico: busca palabras clave ignorando mayúsculas/minúsculas.

Salida:
- Tabla en consola.
- Código de salida 0 siempre (informativo), puede adaptarse si se desea forzar.
"""
from __future__ import annotations
import json
import argparse
import pathlib
from typing import List, Dict

REQUIRED_KEYWORDS = {
    "title": ["#"],
    "objectives": ["objetivo", "objetivos"],
    "exercises": ["ejercicio", "ejercicios"],
    "references": ["referencias"]
}

def find_notebooks(root: pathlib.Path) -> List[pathlib.Path]:
    return [p for p in root.rglob("*.ipynb") if not p.name.startswith(".")]

def load_notebook(path: pathlib.Path) -> Dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def evaluate(notebook_json: Dict) -> Dict[str, bool]:
    cells = notebook_json.get("cells", [])
    markdown_cells = [c for c in cells if c.get("cell_type") == "markdown"]
    text_joined = ["\n".join(c.get("source", [])) for c in markdown_cells]

    # Heurísticas
    results = {k: False for k in REQUIRED_KEYWORDS}
    if markdown_cells:
        first = "\n".join(markdown_cells[0].get("source", [])).lower()
        # Título: línea que empieza con '# '
        if first.strip().startswith("#"):
            results["title"] = True

    all_text = "\n".join(text.lower() for text in text_joined)
    for key, variants in REQUIRED_KEYWORDS.items():
        if key == "title":
            continue  # ya evaluado
        if any(v in all_text for v in variants):
            results[key] = True
    return results

def format_row(name: str, res: Dict[str, bool]) -> str:
    flags = ["✔" if res[k] else "✘" for k in REQUIRED_KEYWORDS]
    return f"{name};" + ";".join(flags)

def main(path: str):
    root = pathlib.Path(path).resolve()
    notebooks = find_notebooks(root)
    rows = []
    aggregated = {k: 0 for k in REQUIRED_KEYWORDS}
    for nb in notebooks:
        try:
            nb_json = load_notebook(nb)
        except Exception:
            continue
        res = evaluate(nb_json)
        for k, v in res.items():
            aggregated[k] += int(v)
        rows.append(format_row(str(nb.relative_to(root)), res))

    header = "archivo;title;objectives;exercises;references"
    print(header)
    for r in rows:
        print(r)
    total = len(notebooks)
    print("\nResumen:")
    for k in REQUIRED_KEYWORDS:
        print(f"{k}: {aggregated[k]}/{total} ({(aggregated[k]/total*100 if total else 0):.1f}%)")
    print("\nTotal notebooks evaluados:", total)
    print("\nNota: Este script es heurístico y sirve como apoyo rápido de estandarización, no reemplaza la revisión humana.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Valida estructura mínima de notebooks")
    parser.add_argument("--path", default=".", help="Ruta raíz para buscar notebooks")
    args = parser.parse_args()
    main(args.path)
