#!/usr/bin/env python3
"""下載文章用到的 Logdown 圖片到 assets/images/ 。
用法(在 repo 根目錄): python3 scripts/download_images.py
只需 Python 3,不用安裝套件。已下載的檔案會略過,可重複執行。"""
import json, os, sys, urllib.request

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
items = json.load(open(os.path.join(root, "scripts", "images_manifest.json"), encoding="utf-8"))
ok, failed = 0, []
for it in items:
    dest = os.path.join(root, it["path"])
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        ok += 1; continue
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        req = urllib.request.Request(it["url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
            f.write(r.read())
        ok += 1; print("OK  ", it["path"])
    except Exception as e:
        failed.append((it["url"], str(e))); print("FAIL", it["url"], e)
print(f"\n成功 {ok} / {len(items)}")
if failed:
    print("以下圖片下載失敗(可能 Logdown 已移除),請從原始筆記補圖:")
    for u, e in failed: print(" ", u)
    sys.exit(1)
