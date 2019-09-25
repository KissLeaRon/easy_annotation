import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow,QGridLayout,QLabel,QHBoxLayout,QVBoxLayout, QCheckBox,QRadioButton, QLineEdit, QMessageBox,QTextEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import os
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
    self.mizo = QLabel("Mizotation tool v1.1.0",self)
    #self.mizo.setFontScale(2)
    self.mizo.move(400,10)
    self.pixmap = QPixmap("./resized/{}".format(DF["id_"][self.num]))
    self.img = QLabel(self)
    self.img.setPixmap(self.pixmap)
    self.img.resize(600,600)
    self.img.move(10,50)

    com = str(DF["caption"][self.num])
    self.comment = QTextEdit(self)
    self.comment.setText(com.replace("\\n","<br>"))
    self.comment.move(20,660)
    self.comment.resize(300,600)

    self.label1 = QLabel("画像について",self)
    self.label1.move(630,180)
    self.cb11 = QCheckBox("自然", self)
    self.cb11.move(640,200)
    self.cb22 = QCheckBox("人 (感情表現)", self)
    self.cb22.move(640,230)
    self.cb33 = QCheckBox("食べ物", self)
    self.cb33.move(640,260)
    self.cb44 = QCheckBox("植物", self)
    self.cb44.move(640,290)


    label2 = QLabel("コメントについて",self)
    label2.move(750,180)
    self.cb1 = QCheckBox("自然", self)
    self.cb1.move(760,200)
    self.cb2 = QCheckBox("人 (感情表現)", self)
    self.cb2.move(760,230)
    self.cb3 = QCheckBox("食べ物", self)
    self.cb3.move(760,260)
    self.cb4 = QCheckBox("植物", self)
    self.cb4.move(760,290)

    label3 = QLabel("全体について",self)
    label3.move(700,440)
    self.cb8 = QCheckBox("1", self)
    self.cb8.move(675,470)
    self.cb9 = QCheckBox("2", self)
    self.cb9.move(705,470)
    self.cb0 = QCheckBox("3", self)
    self.cb0.move(735,470)
    self.cb = QCheckBox("4", self)
    self.cb.move(765,470)

    go_next = QPushButton("Go Next",self)
    go_next.move(800,800)
    go_next.clicked.connect(self.paging)


    self.textbox = QLineEdit(self)
    self.label = QLabel("アノテーター",self)
    self.label.move(635,105)
    self.textbox.move(720,100)
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
      sys.exit(app.exec_())
    self.pixmap = QPixmap("./resized/{}".format(DF["id_"][self.num]))
    self.img.setPixmap(self.pixmap)
    self.comment.setText(str(DF["caption"][self.num]))
    self.state()
    self.show()

  def onClicked(self):
    pass


  def a(self):
    self.show()
   
  def output(self):
    self.st = [self.cb11.isChecked(),
          self.cb22.isChecked(),
          self.cb33.isChecked(),
          self.cb44.isChecked(),
          self.cb1.isChecked(),
          self.cb2.isChecked(),
          self.cb3.isChecked(),
          self.cb4.isChecked(),
          self.cb8.isChecked(),
          self.cb9.isChecked(),
          self.cb0.isChecked(),
          self.cb.isChecked(),
        ]
    buf = [DF["id_"][self.num] , self.annotator] + list(map(str,self.st))
    print(",".join(buf))

  def state(self):
    self.cb11.setCheckState(Qt.Unchecked)
    self.cb22.setCheckState(Qt.Unchecked)
    self.cb33.setCheckState(Qt.Unchecked)
    self.cb44.setCheckState(Qt.Unchecked)
    self.cb1.setCheckState(Qt.Unchecked)
    self.cb2.setCheckState(Qt.Unchecked)
    self.cb3.setCheckState(Qt.Unchecked)
    self.cb4.setCheckState(Qt.Unchecked)
    self.cb8.setCheckState(Qt.Unchecked)
    self.cb9.setCheckState(Qt.Unchecked)
    self.cb0.setCheckState(Qt.Unchecked)
    self.cb.setCheckState(Qt.Unchecked)
    self.show()

if __name__ == "__main__":
  if(len(os.listdir("."))):
      pass
  app = QApplication(sys.argv)
  win = ExampleWidget()
  sys.exit(app.exec_())
