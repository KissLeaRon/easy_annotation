import sys
import os
from itertools import chain

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow,QGridLayout,QLabel,QHBoxLayout,QVBoxLayout, QCheckBox,QRadioButton, QLineEdit, QMessageBox,QTextEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

import pandas as pd

if len(sys.argv) <= 1:
  print("ERROR")
  print("usage: python3 mizo_gui.py `TSV file`")
  exit()

path = sys.argv[1]
DF = pd.read_csv(path,delimiter="\t")
LENGTH = len(DF)

class ExampleWidget(QWidget):
  def __init__(self):
    self.num = 0
    super().__init__()
    self.initUI()
    self.annotator = ""

  def initUI(self):
    self.setWindowTitle("Annotation")
    self.mizo = QLabel("Mizotation tool v1.2.0",self)
    self.mizo.move(400,10)

    self.now = QLabel((DF["id_"][self.num]),self)
    self.now.move(30,30)

    self.pixmap = QPixmap("./resized/{}".format(DF["id_"][self.num]))
    self.img = QLabel(self)
    self.img.setPixmap(self.pixmap)
    self.img.resize(600,600)
    self.img.move(10,50)

    com = str(DF["caption"][self.num])
    self.comment = QTextEdit(self)
    self.comment.setText(com.replace("\\n","<br>"))
    self.comment.move(620,80)
    self.comment.resize(300,600)

    self.label1 = QLabel("画像について",self)
    self.label1.move(20,670)
    self.cb11 = QCheckBox("自然", self)
    self.cb11.move(30,700)
    self.cb22 = QCheckBox("人 (感情表現)", self)
    self.cb22.move(30,730)
    self.cb33 = QCheckBox("食べ物", self)
    self.cb33.move(130,700)
    self.cb44 = QCheckBox("植物(オブジェクト)", self)
    self.cb44.move(130,730)


    label2 = QLabel("コメントについて",self)
    label2.move(270,670)
    self.cb1 = QCheckBox("自然", self)
    self.cb1.move(280,700)
    self.cb2 = QCheckBox("人 (感情表現)", self)
    self.cb2.move(280,730)
    self.cb3 = QCheckBox("食べ物", self)
    self.cb3.move(380,700)
    self.cb4 = QCheckBox("植物(オブジェクト)", self)
    self.cb4.move(380,730)

    label3 = QLabel("全体について",self)
    label3.move(510,670)
    self.cb8 = QCheckBox("1:(自然)", self)
    self.cb8.move(520,700)
    self.cb9 = QCheckBox("2:(中間)", self)
    self.cb9.move(520,730)
    self.cb0 = QCheckBox("3:(自分)", self)
    self.cb0.move(620,700)
    self.cb = QCheckBox("4:(その他)", self)
    self.cb.move(620,730)

    self.checkbox = [
        self.cb11,
        self.cb22,
        self.cb33,
        self.cb44,
        self.cb1,
        self.cb2,
        self.cb3,
        self.cb4,
        self.cb8,
        self.cb9,
        self.cb0,
        self.cb,
        ]

    go_next = QPushButton("Go Next",self)
    go_next.move(830,720)

    go_next.clicked.connect(self.paging)


    self.textbox = QLineEdit(self)
    self.label = QLabel("アノテーター",self)
    self.label.move(700,692)
    self.textbox.move(780,690)
    self.textbox.textChanged[str].connect(self.onChanged)
    self.show()

  def onChanged(self,text):
    #self.label.setText(text)
    #self.label.adjustSize()
    self.annotator = text

  def paging(self):
    if(self.annotator == ""):
      msgBox = QMessageBox()
      msgBox.setText("アノテーターを入力してください")
      msgBox.setStandardButtons(QMessageBox.Yes)
      ret = msgBox.exec_()
      return

    self.output()
    self.num += 1
    if self.num >= LENGTH:
      self.close()
    self.pixmap = QPixmap("./resized/{}".format(DF["id_"][self.num]))
    self.img.setPixmap(self.pixmap)
    com = str(DF["caption"][self.num])
    self.comment.setText(com.replace("\\n",",<br>"))
    self.now.setText(DF["id_"][self.num])
    self.state()
    self.repaint()

  def onClicked(self):
    pass


  def a(self):
    self.show()

  def output(self):
    self.st = [cb.isChecked() for cb in self.checkbox]
    buf = chain((DF["id_"][self.num], self.annotator), self.st)
    print(",".join(str(o) for o in buf), flush=True)

  def state(self):
    for btn in self.checkbox: btn.setCheckState(Qt.Unchecked)
    self.update()

if __name__ == "__main__":
  if(len(os.listdir("."))):
      pass
  app = QApplication(sys.argv)
  win = ExampleWidget()
  sys.exit(app.exec_())
