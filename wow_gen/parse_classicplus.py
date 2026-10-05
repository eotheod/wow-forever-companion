# -*- coding: utf-8 -*-
import json
import re

with open("classicplus_dump.html", "r", encoding="utf-8") as f:
    html = f.read()

m = re.search(r'<script id="cp-census" type="application/json">(.*?)</script>', html, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    print("Version:", data.get("version"))
    print("Snapshot Date:", data.get("snapshotDate"))
    print("Datasets:", list(data.get("datasets", {}).keys()))
    
    classes = data["classes"]
    races = data["races"]
    combos = data["combos"]
    
    for realm_key in ["all", "pve", "pvp"]:
        dset = data["datasets"][realm_key]
        counts = dset["counts"]
        total_chars = sum(counts)
        print(f"\n--- REALM: {realm_key.upper()} (Total chars: {total_chars:,}) ---")
        
        # Calculate faction totals
        faction_counts = {"Alliance": 0, "Horde": 0}
        class_counts = {c["name"]: 0 for c in classes}
        race_counts = {r["name"]: 0 for r in races}
        
        for idx, cnt in enumerate(counts):
            combo = combos[idx]
            r_idx = combo["race"]
            c_idx = combo["class"]
            race = races[r_idx]
            cls = classes[c_idx]
            
            faction_counts[race["faction"]] += cnt
            class_counts[cls["name"]] += cnt
            
        print("Faction Split:")
        for fac, cnt in faction_counts.items():
            pct = (cnt / total_chars) * 100
            print(f"  {fac}: {cnt:,} ({pct:.1f}%)")
            
        print("Class Popularity:")
        sorted_classes = sorted(class_counts.items(), key=lambda x: x[1], reverse=True)
        for cname, cnt in sorted_classes:
            pct = (cnt / total_chars) * 100
            print(f"  {cname}: {cnt:,} ({pct:.1f}%)")
            
        # Level 60 count
        by_level = dset["byLevel"]
        lvl60_count = by_level[19] if len(by_level) > 19 else 0
        print(f"Max Level (60) Characters: {lvl60_count:,} ({(lvl60_count/total_chars)*100:.1f}%)")
else:
    print("No cp-census script found!")

