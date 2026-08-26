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
# --python-platform x86_64-unknown-linux-gnu: los workflows corren en
# ubuntu-latest (GitHub-hosted). Sin fijar la plataforma, `uv pip compile`
# resuelve para el SO donde lo corras -- si lo generas en Windows/Mac,
# el lock trae paquetes especificos de esa plataforma (ej. pywinpty,
# colorama) que no existen en Linux, y el chequeo de "lock actualizado"
# en CI falla siempre por una diferencia de plataforma, no de contenido.
#
# --no-cache: la cache local de `uv` puede quedar con metadata de una
# resolucion anterior (de una version distinta de algun paquete directo)
# y producir un resultado distinto al de una maquina limpia -- confirmado
# en la practica: con cache tibia resolvio una version de una dependencia
# transitiva que NO coincidia con lo que arrojaba GitHub Actions (cache
# fria) para el mismo requirements-dev.txt. Sin --no-cache el lock local
# puede quedar "actualizado" en tu maquina pero desactualizado para CI.
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
    --python-platform x86_64-unknown-linux-gnu \
    --no-header \
    --no-cache \
    -o "locks/py${v}.txt"
done

echo "Listo. Revisa 'git diff locks/' antes de commitear."
