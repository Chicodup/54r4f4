from PIL import Image,ImageFilter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui import Ui_MainWindow
import os
# with Image.open("parrot.jpg") as original:
#    pic_gray = original.convet("L")
#    pic_blur = original.filterr(ImageFilter.BLUR)
#    pic_up = pic_gray.transpose(Image.ROTATE_90)
#    pic_gray.save("bw_pic.jpg")
#    pic_up.save("bw_pic2.jpg")
#    pic_blur.save("blur_pic.jpg")
#    pic_up.show()

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filename = None
        self.image = None
        self.ui.papka_btn.clicked.connect(self.choose_folder)


    def show_image_list(self):
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images.append(filename)
            self.ui.image_list.clear()
            self.ui.image_list.addItems(images)

    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            message = QMessageBox()
            message.setText("Помилка відкриття папки! Помилка: 1488")
            message.exec_()




app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
