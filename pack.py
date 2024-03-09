# -*- encoding: utf-8 -*-
"""Minecraft本地化键名资源包生成器"""

import json
import zipfile as z
from pathlib import Path

# 当前绝对路径
P = Path(__file__).resolve().parent

# 读取语言文件
with open(P / "source" / "en_us.json", "rb") as s:
    source = json.load(s)

# 生成语言文件
with open(P / "key.json", "w", encoding="utf-8") as f:
    json.dump({k: k for k in source.keys()}, f, indent=2)

# 生成资源包
pack_dir = P / "key_language_pack.zip"
with z.ZipFile(pack_dir, "w", compression=z.ZIP_DEFLATED, compresslevel=9) as f:
    f.write(P / "pack.mcmeta", arcname="pack.mcmeta")
    f.write(P / "key.json", arcname="assets/minecraft/lang/key.json")
