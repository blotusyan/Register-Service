#!/bin/bash

echo "started at $(date +"%T.%N")"

set -i -e

usage() { echo "Usage: $0 COMMAND" 1>&2; exit 1; }

export PACKAGE_DIR=./open_elt
export PYLINT_PARAMS="--disable=C0411,W1202"

if [ "$PIPENV_ACTIVE" != "1" ]; then
    echo "You must activate a pipenv shell before building"
    exit 1;
fi
echo "you are inside pipenv"

sam build --template-file template.yaml

echo "finished at $(date +"%T.%N")"
