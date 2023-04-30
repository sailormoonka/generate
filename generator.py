from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    info.setText('Переможець:')

app = QApplication([])
main_win =  QWidget()
main_win.setWindowTitle("Визначник переможця")
main_win.resize(400, 200)
main_win.move(900, 70)
v_line = QVBoxLayout()
button = QPushButton("Генерувати")
info = QLabel("Натисніть, щоб обрати переможця!")
winner = QLabel("?")

v_line.addWidget(info, alignment=Qt.AlignCenter)
v_line.addWidget(winner, alignment=Qt.AlignCenter)
v_line.addWidget(button, alignment=Qt.AlignCenter)

button.clicked.connect(show_winner)

main_win.setLayout(v_line)
main_win.show()
app.exec_()
