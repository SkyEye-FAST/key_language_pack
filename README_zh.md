# Minecraft本地化键名语言资源包

- **[English](README.md) | [中文](README_zh.md)**

----

此项目用于提供将Minecraft Java版语言文件内容替换为本地化键名（Translation Key）的资源包。

推荐与模组[Language Reload](https://modrinth.com/mod/language-reload)和[Untranslated Items](https://www.curseforge.com/minecraft/mc-mods/untranslated-items)一同使用。

## 下载

- [**下载最新版本资源包**](https://github.com/SkyEye-FAST/key_language_pack/releases/latest/download/key_language_pack.zip)
- [查看历史版本](https://github.com/SkyEye-FAST/key_language_pack/releases/)

> [!TIP]
> 由于1.19.2之后所有版本的语言文件都可以通用，不一定需要选择对应版本的标签，选择最新版本即可。

## 说明

### 获取语言文件

本仓库会在每天🕧00:30（UTC+8，即🕟UTC 16:30）自动检查Minecraft Java版语言文件（`en_us.json`）更新并更新资源包。使用脚本为[`source.py`](source.py)（需要库`requests`）。获取到的语言文件存储在与脚本同级的`source`文件夹下。

### 资源包

> [!IMPORTANT]
> 本项目忽略了所有以`translation.`开头的键名，因为它们被用于测试游戏内字符串能否正常显示。并且它们过于复杂，常规字符串中不会出现类似的情况。如果需要替换了这些键名的资源包，参见[Nickid2018/TranslationKeyPack](https://github.com/Nickid2018/TranslationKeyPack)和[bilintsui/keypack](https://github.com/bilintsui/keypack)。

资源包使用[`pack.py`](pack.py)生成。脚本生成的语言文件为[`key.json`](key.json)和[`key_arg.json`](key_arg.json)，同[`pack.mcmeta`](pack.mcmeta)一同打包为`key_language_pack.zip`。

资源包向游戏内添加了名为“Translation (Keys)”的语言，选择之后，所有字符串会变为本地化键名。

此外，资源包还提供一种名为“Translation (Keys with Arguments)”的语言，类似MediaWiki的`qqx`语言。选择之后，字符串除了变为本地化键名之外，还会在其后用括号补上原先使用的参数。

选择“Translation (Keys)”的效果如图所示：
![Sample](sample/1.png)
![Sample](sample/2.png)
![Sample](sample/3.png)
![Sample](sample/4.png)
![Sample](sample/5.png)

## 协议

资源包在[Apache 2.0协议](LICENSE)下发布。

``` text
  Copyright 2024-2025 SkyEye_FAST

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
```

## 反馈

遇到的问题和功能建议等可以提出议题（Issue）。

欢迎创建拉取请求（Pull request）。
