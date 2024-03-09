# Minecraft本地化键名资源包

此项目用于提供将Minecraft Java版语言文件替换为本地化键名（Translation Key）的资源包。

## 说明

### 获取语言文件

本仓库会在每天🕧00:30（UTC+8，即🕟UTC 16:30）自动检查Minecraft Java版语言文件（`en_us.json`）更新并更新资源包。使用脚本为[`source.py`](/source.py)（需要库`requests`）。获取到的语言文件存储在与脚本同级的`source`文件夹下。

### 资源包

资源包使用[`pack.py`](/pack.py)生成。脚本生成的语言文件为[`key.json`](/key.json)，同[`pack.mcmeta`](/pack.mcmeta)一同打包为[`key_language_pack.zip`](/key_language_pack.zip)。

资源包向游戏内添加了名为“Translation (Key)”的语言，选择之后所有字符串会变为本地化键名。

## 反馈

遇到的问题和功能建议等可以提出议题（Issue）。

欢迎创建拉取请求（Pull request）。
