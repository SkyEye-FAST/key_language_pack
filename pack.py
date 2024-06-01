# -*- encoding: utf-8 -*-
"""Minecraft本地化键名资源包生成器"""

import json
import re
import zipfile as z
from pathlib import Path
from typing import Dict, List

# 当前绝对路径
P = Path(__file__).resolve().parent

# 读取语言文件
with open(P / "mc_lang" / "full" / "en_us.json", "rb") as s:
    source: Dict[str, str] = json.load(s)

# 生成语言文件
with open(P / "output" / "key.json", "w", encoding="utf-8") as f:
    json.dump({k: k for k in source.keys()}, f, indent=2)

for key, value in source.items():
    if key.startswith("translation."):
        continue
    if "%" in value:
        arguments: List[str] = re.findall(r"%\d*\$?[sd]", value)
        arguments_list = [f"({arg})" for arg in arguments]
        source[key] = re.sub(
            r"%\d+\$s", r"%s", f"{key} {" ".join(arguments_list)}"
        ).rstrip()
    else:
        source[key] = key

with open(P / "output" / "key_arg.json", "w", encoding="utf-8") as file:
    json.dump(source, file, indent=2)

# 生成资源包
pack_dir = P / "key_language_pack.zip"
with z.ZipFile(pack_dir, "w", compression=z.ZIP_DEFLATED, compresslevel=9) as f:
    f.write(P / "pack.mcmeta", arcname="pack.mcmeta")
    f.write(P / "output" / "key.json", arcname="assets/minecraft/lang/key.json")
    f.write(P / "output" / "key_arg.json", arcname="assets/minecraft/lang/key_arg.json")
