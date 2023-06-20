import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit


from PyQt5.QtCore import Qt

import requests

class Doviz(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        yazi1 = QLabel("1. Döviz")
        self.birinci_doviz = QLineEdit()

        yazi2 = QLabel("2.Döviz")
        self.ikinci_doviz = QLineEdit()

        yazi3 = QLabel("Miktar")
        self.miktar = QLineEdit()

        self.cevir = QPushButton("Çevir")



        self.sonuc = QLineEdit()
        self.sonuc.setVisible(False)
        self.sonuc.setReadOnly(True)




        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(yazi1)
        h_box.addWidget(self.birinci_doviz)
        h_box.addWidget(yazi2)
        h_box.addWidget(self.ikinci_doviz)
        h_box.addWidget(yazi3)
        h_box.addWidget(self.miktar)
        h_box.addStretch()



        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.sonuc, alignment=Qt.AlignHCenter)
        v_box.addLayout(h_box)
        v_box.addWidget(self.cevir, alignment=Qt.AlignHCenter)
        v_box.addStretch()



        self.setLayout(v_box)

        self.setWindowTitle("Döviz Çevirici")

        self.cevir.clicked.connect(self.baglanti)

    def baglanti(self):

        url = "http://data.fixer.io/api/latest?access_key=e4a2c44d478954424efbabe1a0d2d61a"

        birinci_doviz = self.birinci_doviz.text()
        ikinci_doviz = self.ikinci_doviz.text()
        miktar = float(self.miktar.text())

        response = requests.get(url)
        json_verisi = response.json()

        birincideger = json_verisi["rates"][birinci_doviz]
        ikincideger = json_verisi["rates"][ikinci_doviz]

        sonuc = ikincideger / birincideger * miktar
        self.sonuc.setVisible(True)
        self.sonuc.setText(str(sonuc))













app = QApplication(sys.argv)
doviz_arayuz = Doviz()
doviz_arayuz.show()
sys.exit(app.exec_())





