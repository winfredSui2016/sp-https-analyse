#!/usr/bin/env bash

cd $(dirname $0)

pip freeze > requirements.txt
echo "# requirements was dump in requirements.txt"
cat requirements.txt
