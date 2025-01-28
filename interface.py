from excel import (create_table, write_data,
                   unclear_list, clear_list, clear_number_list, xml_file, xlsx_file, new_file)
from parse import (parse_numbers, clean_numbers)

import openpyxl as op
import pandas as pd
import os
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow

def on_clicked():
    print('Clicked')

    parse_numbers(unclear_data=unclear_list, clear_data=clear_list, data_file=xml_file)

    clean_numbers(unclear_numbers=clear_list, clear_numbers=clear_number_list)

    print(clear_number_list)

    create_table(file=new_file)
    write_data(file=new_file, number_list=clear_number_list)

def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setFixedSize(QSize(800, 400))
    window.setWindowTitle('Преобразовать в xlsx')

    xml = QPushButton('Открыть xml', window)
    xml.resize(175, 50)
    xml.move(550, 75)

    wrong_xml = QPushButton('X', window)
    wrong_xml.resize(50, 50)
    wrong_xml.move(495, 75)

    xml_path = QLineEdit(window)
    xml_path.resize(425, 50)
    xml_path.move(50, 75)

    xml_path.setText(xml_file)


    xlsx = QPushButton('Открыть xlsx', window)
    xlsx.resize(175, 50)
    xlsx.move(550, 150)

    wrong_xlsx = QPushButton('X', window)
    wrong_xlsx.resize(50, 50)
    wrong_xlsx.move(495, 150)

    xlsx_path = QLineEdit(window)
    xlsx_path.resize(425, 50)
    xlsx_path.move(50, 150)

    xlsx_path.setText(xlsx_file)

    claim = QPushButton(window)
    claim.setText('Преобразовать')
    claim.clicked.connect(on_clicked)
    claim.resize(200, 50)
    claim.move(300, 300)

    window.show()

    app.exec()

if __name__ == "__main__":
    main_file = xlsx_file  # данные о книге
    main_book = op.load_workbook(main_file)

    xls = pd.ExcelFile(main_file)

    main_sheet = xls.sheet_names[0]

    main()