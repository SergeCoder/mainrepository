from excel import (create_table, write_data, unclear_list, clear_list,
                   clear_number_list, xml_file, xlsx_file, new_file)
from parse import (parse_numbers, clean_numbers)

import openpyxl as op
import pandas as pd
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QMessageBox

main_file = xlsx_file  # данные о книге
main_book = op.load_workbook(main_file)
xls = pd.ExcelFile(main_file)
main_sheet = xls.sheet_names[0]

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setFixedSize(QSize(800, 400))
        self.setWindowTitle('Преобразовать в xlsx')

        self.setup()

    def setup(self):
        self.xml_path = QLineEdit(self)
        self.xml_path.resize(425, 50)
        self.xml_path.move(100, 75)
        self.xml_path.setText(xml_file)

        self.wrong_xml = QPushButton('X', self)
        self.wrong_xml.clicked.connect(self.xml_path.clear)
        self.wrong_xml.resize(50, 50)
        self.wrong_xml.move(545, 75)

        self.xlsx_path = QLineEdit(self)
        self.xlsx_path.resize(425, 50)
        self.xlsx_path.move(100, 150)
        self.xlsx_path.setText(xlsx_file)

        self.wrong_xlsx = QPushButton('X', self)
        self.wrong_xlsx.clicked.connect(self.xlsx_path.clear)
        self.wrong_xlsx.resize(50, 50)
        self.wrong_xlsx.move(545, 150)

        self.claim = QPushButton('Преобразовать', self)
        self.claim.clicked.connect(self.start_parse)
        self.claim.resize(200, 50)
        self.claim.move(300, 300)

    def start_parse(self):
        if not self.xlsx_path.text() == '' and not self.xml_path.text() == '':
            print('Start')

            parse_numbers(unclear_data=unclear_list, clear_data=clear_list, data_file=xml_file)

            clean_numbers(unclear_numbers=clear_list, clear_numbers=clear_number_list)

            create_table(file=new_file)
            write_data(file=new_file, number_list=clear_number_list)

            self.end = QMessageBox(self)
            self.end.setWindowTitle('Конец преобразования')
            self.exit = self.end.addButton('Выйти', QMessageBox.AcceptRole)
            self.exit.clicked.connect(self.close)
            self.stay = self.end.addButton('Остаться', QMessageBox.AcceptRole)
            self.end.exec()


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()