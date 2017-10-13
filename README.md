# SoraVoiceScripts
Voice Scripts for PC games *Sora no Kiseki* / *Trails in the Sky* series.    
They can be used for the project [SoraVoce](https://github.com/ZhenjianYang/SoraVoice).

Scripts for these games were done:

|Game Title                |Publisher|Platform        |Language          |             |
|--------------------------|---------|----------------|------------------|-------------|
|*Trails in the Sky FC*    |Xseed    |Steam/GOG/Humble|English           |Done by [Snakes&Ladies Games](https://www.youtube.com/c/SnakesLadiesGames)
|*Trails in the Sky FC*    |Xseed    |Steam           |Chinese Simplified|[ED6-FC-Steam-CN](https://github.com/Ouroboros/ED6-FC-Steam-CN)
|*Sora no Kiseki FC*       |YLT      |                |Chinese Simplified|The Original PC ver

Get them at [Release](https://github.com/ZhenjianYang/SoraVoiceScripts/releases/latest), or   
## Follow these steps

1.  **Clone**   
  `git clone --recursive https://github.com/ZhenjianYang/SoraVoiceScripts`
  
2.  **Install python3 and 7zip**   
  We assume the path of 7zip is `C:\Program Files\7-Zip\7z.exe`  
  Some python libs need to be installed. Please refer to [tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler).

3.  Copy **\.dir** files in games' in installation folders to this project   
    ***Trails in the Sky FC*** : Copy **\.dir** files to `game_files/DIR_FC/`   

4.  **Generate script files**   
  Just run the batch file `DoAll.bat`   
  New script files will be packed under folder `pack`

## Dependence

- [tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler), forked from [Ouroboros/EDDecompiler](https://github.com/Ouroboros/EDDecompiler)   

- [tools/PyLibs](https://github.com/ZhenjianYang/PyLibs), forked from [Ouroboros/PyLibs](https://github.com/Ouroboros/PyLibs)   

# SoraVoiceScripts
PC游戏《空之轨迹》系列的语音脚本    
语音脚本可以用于项目[SoraVoce](https://github.com/ZhenjianYang/SoraVoice)。

下列游戏的语音脚本已完成：   

|游戏标题       |发行商 |平台            |语言     |              |
|---------------|-------|----------------|---------|--------------|
|空之轨迹 FC    |Xseed  |Steam/GOG/Humble|英语     |由[Snakes&Ladies Games](https://www.youtube.com/c/SnakesLadiesGames)完成
|空之轨迹 FC    |Xseed  |Steam           |简体中文 |[ED6-FC-Steam-CN](https://github.com/Ouroboros/ED6-FC-Steam-CN)
|空之轨迹 FC    |娱乐通 |                |简体中文 |原版PC

在[这里](https://github.com/ZhenjianYang/SoraVoiceScripts/releases/latest)可以获取到上述语音脚本。或者，
## 参照以下步骤   

1.  **获取**   
  `git clone --recursive https://github.com/ZhenjianYang/SoraVoiceScripts`
  
2.  **安装python3以及7zip**   
  这里假定7zip路径为：`C:\Program Files\7-Zip\7z.exe`   
  还需要安装一些python库，具体请参考[tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler)。

3.  将游戏安装目录下的 **.dir**文件复制到本项目   
    **《空之轨迹 FC》**: 复制 **\.dir**文件到`game_files/DIR_FC/`   

4.  **生成脚本文件**   
  执行`DoAll.bat`即可    
  新的脚本文件会打包好并置于文件夹`pack`下

## 依赖

- [tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler), Fork自[Ouroboros/EDDecompiler](https://github.com/Ouroboros/EDDecompiler)   

- [tools/PyLibs](https://github.com/ZhenjianYang/PyLibs), Fork自[Ouroboros/PyLibs](https://github.com/Ouroboros/PyLibs) 
