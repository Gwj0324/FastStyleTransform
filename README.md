# FastStyleTransform
使用PySide6制作了Tensorflow上快速风格迁移示例的窗口程序

## 1，fastStyle文件夹下是快速风格迁移的窗口程序

### 安装环境

1，我用的是Python3.10.1 64bit 解释器，不清楚其它是否可以。

2，pip install 命令安装相关依赖库

PySide6 Pillow matplotlib tensorflow tensorflow_hub

3,使用pyinstaller工具打包发布程序

我这里使用了`pyinstaller --name=main --windowed main.py`命令来打包的。

需要将`form.ui`文件拷贝到生成的`./dist/main/` 目录下。

### 使用说明

1，添加一张内容图片，然后再添加一张风格图片。

![image-20230602233347593](E:\本科毕业设计\FastStyleTransform\image-20230602233347593.png)

2，点击生成图像

![image-20230602233421223](E:\本科毕业设计\FastStyleTransform\image-20230602233421223.png)

## 2,Test文件夹下是vgg卷积神经网络做的图像风格迁移程序

