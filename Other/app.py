import sys
import time
from itertools import combinations
import win32clipboard
from math import factorial as f

from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QPushButton,
    QMainWindow,
    QProgressBar,
    QWidget,
    QLineEdit,
    QTextEdit,
    QLabel,
    QMessageBox
)

from PyQt6.QtGui import QIcon

from PyQt6 import QtGui, QtCore

from PyQt6.QtCore import pyqtSignal, QObject, QThread


class SetWithSum:
    def __init__(self, terms):
        self._items = list(terms)
        self._sum = sum(terms)

    def add(self, num):
        self._items.append(num)
        self._sum += num
        return self

    def clone(self):
        return SetWithSum(self.items())

    def items(self):
        return self._items

    def sum(self):
        return self._sum

    def __repr__(self):
        return f'{self._items} = {self._sum}'


def find_sum(terms, target):
    terms = list(sorted(terms))
    result = [SetWithSum([terms[0]])]
    for digit in terms[1:]:
        twin = result
        twin.extend([i.clone().add(digit) for i in result])
        twin = sorted(twin, key=SetWithSum.sum)
        term = twin[0]
        result = [term]
        for num in twin:
            if (term.sum()) < num.sum() and num.sum() <= target:
                term = num
                result.append(term)
    output = max(result, key=SetWithSum.sum)
    if (str(output).split(' '))[-1] == str(target):
        return f'{output}'
    else:
        raise ValueError('No matching sum')


def find_terms(terms, target):
    left = round((sum(terms) - target), 2)
    if left in terms:
        terms.remove(left)
        return f'{terms} = {target}'
    i = 2
    while i != len(terms):
        ammount = combinations(terms, i)
        comb_num = f(len(terms)) / (f(i) * f(len(terms) - i))
        counter = 0
        for j in ammount:
            print(j)
            if round(sum(j), 2) == target:
                return f'{j} = {target}'
            elif round(sum(j), 2) == left:
                for num in j:
                    terms.remove(num)
                return f'{terms} = {target}'
            elif round(sum(j), 2) > target:
                counter += 1
        if counter == comb_num:
            return 'Немає співпадінь серед вказаних накладних'
        i += 1
    return 'Немає співпадінь серед вказаних накладних'

class myApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Оплата по банку по накладних')
        self.setWindowIcon(QIcon('coin-wallet-100.ico'))
        self.resize(350, 400)

        widget = QWidget()
        layout = QVBoxLayout()


        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText('Введіть суму оплати')
        self.input1.move(50, 50)
        layout.addWidget(self.input1)

        self.input2 = QTextEdit(self)
        self.input2.setPlaceholderText('Вставте накладні, які можуть входити в цю суму, в стовбчик.\nНаприклад: \n1245,32\n196,24\n458,25\n...')
        self.input2.move(50, 0)
        layout.addWidget(self.input2)

        self.progressBar = QProgressBar()
        self.progressBar.setMaximum(100)
        layout.addWidget(self.progressBar)

        self.button = QPushButton('Знайти')
        self.button.clicked.connect(self.launch)
        self.button.clicked.connect(self.setsum)
        self.button.move(200, 0)
        layout.addWidget(self.button)

        self.label = QLabel('Тут відобразиться результат.\nЯкщо накладних багато, це може зайняти деякий час.\nРезультат буде автоматично скопійовано в буфер обміну,\nвставте його в будь-який текстовий файл!')
        layout.addWidget(self.label)

        self.time = QLabel()
        layout.addWidget(self.time)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def launch(self):
        self.progressBar.setValue(0)



    def setsum(self):
        text = self.input1.text()
        text2 = self.input2.toPlainText()
        mytable = text.maketrans(",", ".")
        reversed = text.maketrans(".", ",")
        target = float(text.translate(mytable))
        terms = [(line.translate(mytable)) for line in text2]
        terms = list(map(float, ''.join(terms).split()))
        start = time.time()
        try:
            result = find_sum(terms, target)
        except ValueError:
            result = find_terms(terms, target)
        finally:
            self.progressBar.setValue(100)
            self.label.setText(result.translate(reversed))
            self.time.setText(f'Виконано за {int(time.time() - start) // 60} хвилин {int(time.time() - start) % 60} секунд')
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(result.translate(reversed))
            win32clipboard.CloseClipboard()


if __name__=="__main__":
    app = QApplication(sys.argv)

    window = myApp()
    window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')