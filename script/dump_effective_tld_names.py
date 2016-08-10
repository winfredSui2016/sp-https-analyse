# encoding=utf-8
import json
from pprint import pprint

import requests

url = 'https://publicsuffix.org/list/effective_tld_names.dat'

rs = requests.get(url)

if rs.status_code != 200:
    raise BaseException('http_code is ' + str(rs.status_code))

content = rs.content.decode('utf-8')

list = []

for line in content.split('\n'):
    line = line.strip()
    if line == '' or line.startswith('//'):
        continue
    list.append(line)

print(json.dumps(list))
