from PyQt5.QtCore import Qt
from PIL import Image,ImageFilter 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
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
        self.ui.pushButton.clicked.connect(self.choose_folder)
        self.ui.image_list.currentRowChanged.connect(self.show_chosen_image)
    def show_image_list(self):
        """завантажуємо список частинок"""
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images.append(filename)
            self.ui.image_list.clear()
            self.ui.image_list.addItems(images)

    def choose_folder(self):
        """відкриття вікна вибору папки"""
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            message = QMessageBox()
            message.setText("Помилка відкриття папки! Помилка: 1488")
            message.exec_()

    def load_image(self, imagename):
        self.image_name = imagename
        self.image_path = os.path.join(self.workdir, self.image_name)
        self.image = Image.open(self.image_path)



    def show_image(self):
        """відображуємо картинку у вікні програми"""
        self.ui.image_label.hide()
        h = self.ui.image_label.height()
        w = self.ui.image_label.width()

        pixmap_image = QPixmap(self.image_path)
        pixmap_image = pixmap_image.scaled(w,h,Qt.KeepAspectRatio)
        self.ui.image_label.setPixmap(pixmap_image)
        self.ui.image_label.show()



    def show_chosen_image(self):
        """показати вибране зображення"""
        if self.ui.image_list.currentRow()>=0:
            self.image_name = self.ui.image_list.currentItem().text()
            self.load_image(self.image_name)
            self.show_image()

    def save_image(self):
        path = os.path.join(self.workdir, "edited")
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        self.new_path = os.path.join(path, self.image_name)
        self.new_image.save(self.new_path)
        self.image_path = self.new_path



    def do_black_white(self):
        self.new_image = self.image.convert('L')
        self.save_image()
        self.show_image()



app = QApplication([])
ex = Widget()
ex.show()
app.exec_()