import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
HELPERS_PATH = ROOT / "04-recursos" / "helpers"
if str(HELPERS_PATH) not in sys.path:
    sys.path.insert(0, str(HELPERS_PATH))

SCRIPTS_PATH = ROOT / "scripts"
if str(SCRIPTS_PATH) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_PATH))
