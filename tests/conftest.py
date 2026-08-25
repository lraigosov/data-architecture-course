import pathlib
import sys

# curso_helpers (04-recursos/helpers) se importa vía el paquete instalado en
# modo editable (`pip install -e .`, ver pyproject.toml) -- sin sys.path.

# scripts/ no está empaquetado (son scripts de linea de comandos, no una
# librería), así que sí necesita sys.path para que los tests lo importen.
ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPTS_PATH = ROOT / "scripts"
if str(SCRIPTS_PATH) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_PATH))
