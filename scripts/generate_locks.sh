#!/usr/bin/env bash
# Regenera los lock files exactos (locks/pyX.Y.txt) para cada version de
# Python soportada, a partir de requirements-dev.txt (que a su vez incluye
# requirements.txt y el paquete local -e .).
#
# No usamos --generate-hashes a propósito: pip no permite mezclar modo
# hash-checking con un requirement editable (-e .) como el paquete local
# curso_helpers, y el objetivo aquí es version pinning reproducible, no
# verificación criptográfica de artefactos.
#
# --no-header: el header que autogenera `uv pip compile` incluye la ruta
# de salida exacta usada en el comando, lo que produciría un diff falso
# contra el chequeo de "lock actualizado" en ci.yml (que compila a un
# archivo temporal con otro nombre).
#
# Requiere `uv` (https://docs.astral.sh/uv/). Uso:
#   bash scripts/generate_locks.sh
#
# Si tu red intercepta TLS (proxy corporativo, etc.) y `uv` falla con
# errores de certificado, agrega --native-tls al comando de abajo.
#
# Tras correrlo, revisa el diff de locks/*.txt y commitea junto con
# cualquier cambio a requirements.txt / requirements-dev.txt / pyproject.toml.
set -euo pipefail
cd "$(dirname "$0")/.."

VERSIONS=(3.11 3.12 3.13 3.14)

for v in "${VERSIONS[@]}"; do
  echo "==> Generando locks/py${v}.txt"
  uv pip compile requirements-dev.txt \
    --python-version "$v" \
    --no-header \
    -o "locks/py${v}.txt"
done

echo "Listo. Revisa 'git diff locks/' antes de commitear."
