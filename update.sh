#!/usr/bin/env bash

cd $(dirname $0)

# 更新域名后缀列表
./env/bin/python script/dump_effective_tld_names.py > app/static/app/data/effective_tld_names.json
