import pyautogui as pag
import os
import time
import keyboard as key
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gersangAlarm.gersang_alarm_UI import Ui_MainWindow
image_list_1 = []

class check_image_fuction(QMainWindow,Ui_MainWindow):
  def init(self):
    super().init()
    self.setupUi(self)
    self.worker_a = worker_a()
    self.show()

  def start(self):

    self.worker_a.start()
    pass


path1 = "./icon1/"
directory1 = os.listdir(path1)



for file in directory1:
  if file.endswith('.png') or file.endswith('.jpg'):
    image_list_1.append(file)


class worker_a(QThread):
  def run(self):
    try:
      while True:
        # Loop through list to find all the images
        for image in image_list_1:
          var = pag.locateAllOnScreen(path1 + image, confidence=0.98)
          var = list(var)
          time.sleep(0.5)
          if len(var) != 0:
            key.press('alt')
            time.sleep(0.05)
            key.press('1')
            time.sleep(0.05)
            key.release('1')
            time.sleep(0.05)
            key.release('alt')
        del var
        time.sleep(0.5)
    except KeyboardInterrupt:
      print('\n')


app = QApplication([])
main_dialog = check_imagefuction() 
QApplication.processEvents()
app.exit(app.exec()) 