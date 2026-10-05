# -*- coding: utf-8 -*-
import requests
import re
import json

url = 'https://classicplus.io/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
r = requests.get(url, headers=headers, timeout=10)
text = r.text

print("Length of HTML:", len(text))

# Save a copy to inspect
with open("classicplus_dump.html", "w", encoding="utf-8") as f:
    f.write(text)

# Look for json or data variables
for line in text.splitlines():
    if any(k in line.lower() for k in ["realm", "census", "alliance", "horde", "characters", "pvp", "pve"]):
        if len(line.strip()) < 300:
            print("LINE:", line.strip())

