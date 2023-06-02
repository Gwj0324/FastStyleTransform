from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from fastStyle import image_generation
import fastStyle
import sys
import os
envpath = r'D:\Anaconda\Lib\site-packages\PySide6\plugins\platforms'
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = envpath


class widget(QWidget):
    def __init__(self):
        super(widget, self).__init__()
        self.ui = QUiLoader().load('form.ui')
        self.ui.setStyleSheet(
            "QPushButton{"
            "background-color:rgba(36, 172, 242,30);"
            "border-style:outset;"
            "border-width:4px;"
            "border-radius:10px;"
            "border-color:rgba(255,255,255,30);"
            "font:bold 13px;"
            "color:rgba(0,0,0,100);"
            "padding:6px;"
            "}"
            "QPushButton:pressed{"
            "background-color:rgba(233, 66, 66,200);"
            "border-color:rgba(255,255,255,30);"
            "border-style:inset;"
            "color:rgba(0,0,0,100);"
            "}"
            "QPushButton:hover{"
            "background-color:rgba(255, 177, 91,100);"
            "border-color:rgba(255,255,255,200);"
            "color:rgba(0,0,0,200);"
            "}")
        self.ui.pushButton_content.clicked.connect(self.image_choose)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.ui.pushButton_style.clicked.connect(self.image_choose)
        self.content_image_path = ''
        self.style_image_path = ''
        self.result_image_path = './result.png'        

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def show_image(self, image_path,object):
        if(object == self.ui.pushButton_content):
            self.content_image_path = image_path
            self.ui.label_content.setPixmap(QPixmap(image_path))
            self.ui.label_content.setScaledContents(True)
        elif(object == self.ui.pushButton_style):
            self.style_image_path = image_path
            self.ui.label_style.setPixmap(QPixmap(image_path))
            self.ui.label_style.setScaledContents(True)
        elif(object == self.ui.pushButton_start):
            self.ui.label_result.setPixmap(QPixmap(image_path))
            self.ui.label_result.setScaledContents(True)

    def image_choose(self):
        file_name = QFileDialog.getOpenFileName(
            self, "open file dialog", "./", "Image files(*.png)")
        # "open file Dialog "为文件对话框的标题，第三个是打开的默认路径，第四个是文件类型过滤器
        if(file_name[0] != ''):
            self.show_image(file_name[0], self.sender())
    def start(self):
        image_generation(self.content_image_path,self.style_image_path,self.result_image_path)
        self.show_image(self.result_image_path,self.ui.pushButton_start)

if __name__ == "__main__":
    app = QApplication([])
    widget = widget()
    widget.ui.show()    
    sys.exit(app.exec())
