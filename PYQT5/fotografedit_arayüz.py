import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout, QMainWindow, QAction, qApp, QInputDialog
from PyQt5.QtGui import QPixmap, QImage, QTransform
from PIL import Image, ImageFilter

class PhotoEdit(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.fotoalani = QLabel()

        self.dondur = QPushButton("Döndür")
        self.cozunurluk = QPushButton("Çözünürlük Değiştir")

        h_box = QHBoxLayout()
        h_box.addWidget(self.dondur)
        h_box.addWidget(self.cozunurluk)

        v_box = QVBoxLayout()
        v_box.addWidget(self.fotoalani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.dondur.clicked.connect(self.fotodondur)
        self.cozunurluk.clicked.connect(self.cozunurlukdegistir)

    def sil(self):
        self.fotoalani.clear()

    def dosya_ac(self):
        dosya_ismi, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("DESKTOP"))
        if dosya_ismi:
            pixmap = QPixmap(dosya_ismi)
            self.fotoalani.setPixmap(pixmap)

    def dosya_kaydet(self):
        dosya_ismi, _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("DESKTOP"))
        if dosya_ismi:
            pixmap = self.fotoalani.pixmap()
            if pixmap:
                pixmap.save(dosya_ismi)

    def fotodondur(self):
        angle, ok = QInputDialog.getInt(self, "Döndürme Açısı", "Açıyı girin:")
        if ok:
            pixmap = self.fotoalani.pixmap()
            if pixmap is not None:
                pixmap = pixmap.transformed(QTransform().rotate(angle))
                self.fotoalani.setPixmap(pixmap)


    def cozunurlukdegistir(self):
        width, ok1 = QInputDialog.getInt(self, "Çözünürlük Değiştir", "Genişlik:")
        height, ok2 = QInputDialog.getInt(self, "Çözünürlük Değiştir", "Yükseklik:")
        if ok1 and ok2:
            pixmap = self.fotoalani.pixmap()
            if pixmap is not None:
                image = pixmap.toImage()
                image = image.scaled(width, height)
                pixmap = QPixmap.fromImage(image)
                self.fotoalani.setPixmap(pixmap)



class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere = PhotoEdit()
        self.setCentralWidget(self.pencere)
        self.menuleri_olustur()

        self.setWindowTitle("Photo Edit")
        self.show()

    def menuleri_olustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")

        dosya_ac = QAction("Dosya Aç", self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_ac.triggered.connect(self.pencere.dosya_ac)

        dosya_kaydet = QAction("Dosya Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")
        dosya_kaydet.triggered.connect(self.pencere.dosya_kaydet)

        sil = QAction("Sil", self)
        sil.setShortcut("Ctrl+D")
        sil.triggered.connect(self.pencere.sil)

        cikis = QAction("Çık", self)
        cikis.setShortcut("Ctrl+Q")
        cikis.triggered.connect(qApp.quit)

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(sil)
        dosya.addAction(cikis)


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
