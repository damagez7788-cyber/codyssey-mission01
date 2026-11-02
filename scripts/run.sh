#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")/.."
image_name=jun-workshop:1.0
container_name=${WORKSHOP_CONTAINER:-jun-workshop}
host_port=${WORKSHOP_PORT:-18080}
docker build -t "$image_name" .
docker run -d --name "$container_name" -p "127.0.0.1:${host_port}:80" "$image_name"
printf 'Open http://localhost:%s\n' "$host_port"
