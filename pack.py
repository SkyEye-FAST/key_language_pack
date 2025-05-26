"""Minecraft translation key resource pack generator."""

import json
import re
import zipfile as z
from pathlib import Path

# Current absolute path
P = Path(__file__).resolve().parent

# Read language file
source_path = P / "mc_lang" / "full" / "en_us.json"
with source_path.open("r", encoding="utf-8") as s:
    source: dict[str, str] = json.load(s)

# Generate language file
output_dir = P / "output"
output_dir.mkdir(exist_ok=True)
key_file = output_dir / "key.json"
with key_file.open("w", encoding="utf-8") as f:
    json.dump({k: k for k in source.keys()}, f, indent=2)

for key, value in source.items():
    if not key.startswith("translation."):
        if "%" in value:
            arguments: list[str] = re.findall(r"%\d*\$?[sd]", value)
            arguments_list: list[str] = [f"({arg})" for arg in arguments]
            source[key] = re.sub(
                r"%\d+\$s", r"%s", f"{key} {' '.join(arguments_list)}"
            ).rstrip()
        else:
            source[key] = key

key_arg_file = output_dir / "key_arg.json"
with key_arg_file.open("w", encoding="utf-8") as f:
    json.dump(source, f, indent=2)

# Generate resource pack
pack_dir = P / "key_language_pack.zip"
with z.ZipFile(pack_dir, "w", compression=z.ZIP_DEFLATED, compresslevel=9) as zipf:
    zipf.write(P / "pack.mcmeta", arcname="pack.mcmeta")
    zipf.write(P / "pack.png", arcname="pack.png")
    zipf.write(key_file, arcname="assets/minecraft/lang/key.json")
    zipf.write(key_arg_file, arcname="assets/minecraft/lang/key_arg.json")
