# -*- encoding: utf-8 -*-
"""Minecraft语言文件更新器"""

import hashlib
import sys
from zipfile import ZipFile
from pathlib import Path

import requests as r


def get_response(url: str):
    """获取响应"""
    try:
        resp = r.get(url, timeout=60)
        resp.raise_for_status()
        return resp
    except r.exceptions.RequestException as ex:
        print(f"请求发生错误: {ex}")
        sys.exit()


def get_file(url: str, file_name: str, file_path: Path, sha1: str):
    """下载文件"""
    for _ in range(3):
        with open(file_path, "wb") as f:
            f.write(get_response(url).content)
        size_in_bytes = file_path.stat().st_size
        if size_in_bytes > 1048576:
            size = f"{round(size_in_bytes / 1048576, 2)} MB"
        else:
            size = f"{round(size_in_bytes / 1024, 2)} KB"
        with open(file_path, "rb") as f:
            if hashlib.file_digest(f, "sha1").hexdigest() == sha1:
                print(f"文件SHA1校验一致。文件大小：{size_in_bytes} B（{size}）\n")
                break
            print("文件SHA1校验不一致，重新尝试下载。\n")
    else:
        print(f"无法下载文件“{file_name}”。\n")


# 文件夹
P = Path(__file__).resolve().parent
LANG_DIR = P / "source"
LANG_DIR.mkdir(exist_ok=True)

# 获取version_manifest_v2.json
version_manifest_path = P / "version_manifest_v2.json"
try:
    print("正在获取版本清单“version_manifest_v2.json”……\n")
    version_manifest = r.get(
        "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json",
        timeout=60,
    )
    version_manifest.raise_for_status()
    version_manifest_json: dict = version_manifest.json()
except r.exceptions.RequestException as e:
    print("无法获取版本清单，请检查网络连接。")
    sys.exit()

# 获取版本
V: str = version_manifest_json["latest"]["snapshot"]
with open(P / "version.txt", "w", encoding="utf-8") as ver:
    ver.write(V)
version_info: dict = next(
    (_ for _ in version_manifest_json["versions"] if _["id"] == V), {}
)
if not version_info:
    print("无法在版本清单中找到最新版本。")
    sys.exit()
print(f"选择的版本：{V}\n")

# 获取client.json
client_manifest_url: str = version_info["url"]
print(f"正在获取客户端索引文件“{client_manifest_url.rsplit('/', 1)[-1]}”的内容……")
client_manifest: dict = get_response(client_manifest_url).json()

# 获取资产索引文件
asset_index_url: str = client_manifest["assetIndex"]["url"]
print(f"正在获取资产索引文件“{asset_index_url.rsplit('/', 1)[-1]}”的内容……\n")
asset_index: dict = get_response(asset_index_url).json()["objects"]

# 获取客户端JAR
client_url: str = client_manifest["downloads"]["client"]["url"]
client_sha1: str = client_manifest["downloads"]["client"]["sha1"]
client_path = LANG_DIR / "client.jar"
print(f"正在下载客户端Java归档“client.jar”（{client_sha1}）……")
get_file(client_url, "client.jar", client_path, client_sha1)

# 解压English (United States)语言文件
with ZipFile(client_path) as client:
    with client.open("assets/minecraft/lang/en_us.json") as content:
        with open(LANG_DIR / "en_us.json", "wb") as en:
            print("正在从client.jar解压语言文件“en_us.json”……")
            en.write(content.read())

# 删除客户端JAR
print("正在删除client.jar……\n")
client_path.unlink()

print("已完成。")
