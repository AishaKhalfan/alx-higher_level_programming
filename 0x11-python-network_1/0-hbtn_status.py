#!/usr/bin/python3
# a Python script that fetches https://alx-intranet.hbtn.io/status

from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as f:
    body = f.read()
print('Body response:')
print(f'  - type: {type(body)}')
print(f'  - content: {body}')
print(f'  - utf8 content: {body.decode("utf-8")}')


