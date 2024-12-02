import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QWidget


class SecondChangeWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('second_change_window.ui', self)
        self.new_connection = sqlite3.connect('coffee.sqlite3')
        self.pushButton.clicked.connect(self.change_data)
        self.pushButton_2.clicked.connect(self.close_w)



    def close_w(self):
        self.close()

    def get_data(self):
        return (self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText(),
                self.plainTextEdit_3.toPlainText())



    def change_data(self):
        sort, field, value = self.get_data()
        print(self.get_data())
        self.new_connection.cursor().execute(f"""UPDATE coffee 
                                        SET {field} = ?  
                                        WHERE sort_title = ?""", (value, sort)).fetchall()
        self.new_connection.commit()


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('second_window.ui', self)
        self.new_connection = sqlite3.connect('coffee.sqlite3')
        self.pushButton.clicked.connect(self.create_data)
        self.pushButton_2.clicked.connect(self.close_w)



    def close_w(self):
        self.close()
    def get_data(self):
        return (self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText(),
                self.plainTextEdit_3.toPlainText(), self.plainTextEdit_4.toPlainText(),self.plainTextEdit_5.toPlainText(),self.plainTextEdit_6.toPlainText(),)



    def create_data(self):
        sort, degree, ground_grains, flavor, price, volume = self.get_data()
        print(self.get_data())
        self.new_connection.cursor().execute(f"""INSERT INTO coffee (sort_title,degree_of_roasting,
                                ground_or_grains,flavor_description,price,volume_of_packaging) 
                                VALUES (?,?,?,?,?,?)""",(sort, degree, ground_grains,flavor, price, volume)).fetchall()
        self.new_connection.commit()


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee_ui.ui', self)
        self.res = None
        self.connection = sqlite3.connect('coffee.sqlite3')
        self.select_data()
        self.pushButton.clicked.connect(self.push_data)
        self.pushButton_2.clicked.connect(self.select_data)
        self.pushButton_3.clicked.connect(self.change_data)



    def select_data(self):
        self.res = self.connection.cursor().execute(f"""SELECT * FROM coffee
                                              """).fetchall()
        self.tableWidget.setColumnCount(len(self.res[0]))
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


    def push_data(self):
        self.second_window = SecondWindow()
        self.second_window.show()


    def change_data(self):
        self.second_window_change = SecondChangeWindow()
        self.second_window_change.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
