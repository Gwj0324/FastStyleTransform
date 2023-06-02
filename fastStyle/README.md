# 安装环境

1，我用的是Python3.10.1 64bit 解释器，不清楚其它是否可以。

2，pip install 命令安装相关依赖库

PySide6 Pillow matplotlib tensorflow tensorflow_hub

3,使用pyinstaller工具打包发布程序

我这里使用了`pyinstaller --name=main --windowed main.py`命令来打包的。
需要将`form.ui`文件拷贝到生成的`./dist/main/` 目录下。