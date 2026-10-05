# -*- coding: utf-8 -*-
import requests
import re
import json

def fetch_classicplus_census():
    url = "https://classicplus.io/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            m = re.search(r'<script id="cp-census" type="application/json">(.*?)</script>', r.text, re.DOTALL)
            if m:
                return json.loads(m.group(1))
    except Exception as e:
        print("Live fetch error, fallback to local:", e)
    return None

data = fetch_classicplus_census()
print("Live fetch successful?", data is not None)
if data:
    print("Snapshot Date:", data.get("snapshotDate"))
    print("Total chars across all:", sum(data["datasets"]["all"]["counts"]))

