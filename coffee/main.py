import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee_ui.ui', self)
        self.res = None
        self.pushButton.clicked.connect(self.select_data)

    def select_data(self):
        self.connection = sqlite3.connect(f'{self.plainTextEdit.toPlainText()}.sqlite3')
        self.res = self.connection.cursor().execute(f"""SELECT * FROM coffee
                                              """).fetchall()


        self.tableWidget.setColumnCount(len(self.res[0]))
        print(self.res)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
