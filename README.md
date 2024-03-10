# Minecraft本地化键名资源包

此项目用于提供将Minecraft Java版语言文件替换为本地化键名（Translation Key）的资源包。

推荐与模组[Language Reload](https://modrinth.com/mod/language-reload)和[Untranslated Items](https://www.curseforge.com/minecraft/mc-mods/untranslated-items)一同使用。

## 说明

### 获取语言文件

本仓库会在每天🕧00:30（UTC+8，即🕟UTC 16:30）自动检查Minecraft Java版语言文件（`en_us.json`）更新并更新资源包。使用脚本为[`source.py`](/source.py)（需要库`requests`）。获取到的语言文件存储在与脚本同级的`source`文件夹下。

### 资源包

**注：本项目忽略了所有以`translation.`开头的键名，因为它们被用于测试游戏内字符串能否正常显示。并且它们过于复杂，常规字符串中不会出现类似的情况。如果需要替换了这些键名的资源包，参见[Nickid2018/TranslationKeyPack](https://github.com/Nickid2018/TranslationKeyPack)和[bilintsui/keypack-generator](https://github.com/bilintsui/keypack-generator)。**

资源包使用[`pack.py`](/pack.py)生成。脚本生成的语言文件为[`key.json`](/key.json)和[`key_arg.json`](/key_arg.json)，同[`pack.mcmeta`](/pack.mcmeta)一同打包为[`key_language_pack.zip`](/key_language_pack.zip)。

资源包向游戏内添加了名为“Translation (Keys)”的语言，选择之后，所有字符串会变为本地化键名。

此外，资源包还提供一种名为“Translation (Keys with Arguments)”的语言，类似MediaWiki的`qqx`语言。选择之后，字符串除了变为本地化键名之外，还会在其后用括号补上原先使用的参数。

选择“Translation (Keys)”的效果如图所示：
![Sample](/sample/1.png)
![Sample](/sample/2.png)
![Sample](/sample/3.png)
![Sample](/sample/4.png)
![Sample](/sample/5.png)

## 反馈

遇到的问题和功能建议等可以提出议题（Issue）。

欢迎创建拉取请求（Pull request）。
