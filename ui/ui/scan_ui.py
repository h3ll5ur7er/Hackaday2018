from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from requests import get

image_url = "http://127.0.0.1:4242/poc/image"

data = get(image_url).content

app = QApplication([])
lbl = QLabel()
img = QPixmap()

img.loadFromData(data)
lbl.setPixmap(img)

lbl.show()
app.exec_()
