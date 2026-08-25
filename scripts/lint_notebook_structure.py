#!/usr/bin/env python
"""Linter informal de estructura de notebooks del curso.

IMPORTANTE: esto NO es un validador del estándar completo definido en
docs/estandar_notebooks.md ni un validador de reproducibilidad. Es un
chequeo de apoyo, muy parcial, que solo detecta 4 palabras clave. No
comprueba prerrequisitos, instalación, índice, evaluación, créditos,
semillas aleatorias, entorno documentado, requirements.txt, rutas
relativas ni ningún otro punto del estándar o de la sección
"Reproducibilidad" del documento. No sustituye la revisión humana
contra el checklist del estándar.

Objetivo:
- Comprobar presencia de 4 señales mínimas en la primera parte del notebook.
- Generar un reporte agregando cumplimiento por archivo.

Criterios (heurísticos, no estrictos, no exhaustivos):
1. Primera celda Markdown debe contener título (# )
2. Debe existir alguna celda Markdown con la palabra 'Objetivo' o 'Objetivos'
3. Debe existir una sección 'Ejercicios' o 'Ejercicio'
4. Debe existir una sección 'Referencias'

Uso:
    python scripts/lint_notebook_structure.py --path .

Limitaciones:
- No ejecuta código ni valida reproducibilidad.
- No verifica el resto de secciones del estándar
  (ver docs/estandar_notebooks.md).
- Heurístico: busca palabras clave ignorando mayúsculas/minúsculas.
- No está conectado a CI/CD: se ejecuta manualmente, no bloquea PRs.

Salida:
- Tabla en consola.
- Código de salida 1 si algún notebook falla alguno de los 4 checks
  anteriores; 0 si todos los notebooks los cumplen. Sigue siendo un
  chequeo parcial (ver "IMPORTANTE" arriba), pero dentro de ese alcance
  limitado sí actúa como gate real: no queda como "solo informativo".
"""
from __future__ import annotations
import sys
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

def main(path: str) -> int:
    root = pathlib.Path(path).resolve()
    notebooks = find_notebooks(root)
    rows = []
    aggregated = {k: 0 for k in REQUIRED_KEYWORDS}
    any_failed = False
    for nb in notebooks:
        try:
            nb_json = load_notebook(nb)
        except Exception:
            any_failed = True
            rows.append(f"{nb.relative_to(root)};ERROR_AL_LEER")
            continue
        res = evaluate(nb_json)
        for k, v in res.items():
            aggregated[k] += int(v)
        if not all(res.values()):
            any_failed = True
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
    print(
        "\nNota: Este es un linter informal de apoyo, NO un validador del "
        "estándar completo ni de reproducibilidad (ver "
        "docs/estandar_notebooks.md). No reemplaza la revisión humana."
    )

    if any_failed:
        print("\nRESULTADO: FAIL (al menos un notebook no cumple los 4 checks mínimos)")
        return 1
    print("\nRESULTADO: OK")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Linter informal de estructura mínima de notebooks "
            "(no valida el estándar completo ni reproducibilidad)"
        )
    )
    parser.add_argument("--path", default=".", help="Ruta raíz para buscar notebooks")
    args = parser.parse_args()
    sys.exit(main(args.path))
