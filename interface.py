from excel import (create_table, write_data, collect_unfound, collect_data, unclear_list, clear_list,
                   clear_other_list, other_data_list, clear_number_list, copy_data_list, write_unfound,
                   unfound_numbers, copy_other_list, report_file, xml_file, xlsx_file, new_file,
                   unfound_file, log_list, check_list, check_numbers, log_file, write_log, clear_copy_list)
from parse import (parse_numbers, clean_numbers)

import openpyxl as op
import pandas as pd
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QMessageBox, QLabel

xlsx_book = op.load_workbook(xlsx_file) # данные о книге
xlsx = pd.ExcelFile(xlsx_file)
xlsx_sheet = xlsx.sheet_names[0]

report_book = op.load_workbook(report_file) # данные о логе
report = pd.ExcelFile(report_file)
report_sheet = report.sheet_names[0]

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setFixedSize(QSize(800, 400))
        self.setWindowTitle('Преобразовать в xlsx')

        self.setup()

    def setup(self):
        self.xml_path = QLineEdit(self)
        self.xml_path.resize(475, 50)
        self.xml_path.move(100, 50)
        self.xml_path.setText(xml_file)

        self.xlsx_path = QLineEdit(self)
        self.xlsx_path.resize(475, 50)
        self.xlsx_path.move(100, 125)
        self.xlsx_path.setText(xlsx_file)

        self.copy_path = QLineEdit(self)
        self.copy_path.resize(475, 50)
        self.copy_path.move(100, 200)
        self.copy_path.setText(report_file)

        self.xml_label = QLabel(self)
        self.xml_label.resize(500, 25)
        self.xml_label.move(100, 25)
        self.xml_label.setText('Путь к xml для сбора информации:')

        self.xlsx_label = QLabel(self)
        self.xlsx_label.resize(500, 25)
        self.xlsx_label.move(100, 100)
        self.xlsx_label.setText('Путь к xlsx для чтения и проверки:')

        self.copy_label = QLabel(self)
        self.copy_label.resize(500, 25)
        self.copy_label.move(100, 175)
        self.copy_label.setText('Путь к отчету xlsx для проверки:')

        self.wrong_xml = QPushButton('X', self)
        self.wrong_xml.clicked.connect(self.xml_path.clear)
        self.wrong_xml.resize(50, 50)
        self.wrong_xml.move(600, 50)

        self.wrong_xlsx = QPushButton('X', self)
        self.wrong_xlsx.clicked.connect(self.xlsx_path.clear)
        self.wrong_xlsx.resize(50, 50)
        self.wrong_xlsx.move(600, 125)

        self.wrong_copy = QPushButton('X', self)
        self.wrong_copy.clicked.connect(self.copy_path.clear)
        self.wrong_copy.resize(50, 50)
        self.wrong_copy.move(600, 200)

        self.claim = QPushButton('Преобразовать', self)
        self.claim.clicked.connect(self.start_parse)
        self.claim.resize(200, 50)
        self.claim.move(175, 300)

        self.check_copy = QPushButton('Проверка', self)
        self.check_copy.clicked.connect(self.check_data)
        self.check_copy.resize(200, 50)
        self.check_copy.move(400, 300)

    def start_parse(self):
        if not self.xlsx_path.text() == '' and not self.xml_path.text() == '':
            parse_numbers(unclear_data=unclear_list, clear_data=clear_list, other_data_list=other_data_list,
                          clear_other_data=clear_other_list, data_file=xml_file,
                          my_file=xlsx_file, my_sheet=xlsx_sheet, log_list=log_list)

            clean_numbers(unclear_numbers=clear_list, clear_numbers=clear_number_list)

            create_table(file=new_file)
            write_data(file=new_file, number_list=clear_number_list, other_data_list=clear_other_list)

            check_numbers(unclear_data=unclear_list, log_list=log_list, check_list=check_list)

            create_table(file=log_file)
            write_log(file=log_file, check_list=check_list)

            self.end = QMessageBox(self)
            self.end.setWindowTitle('Конец преобразования')
            self.exit = self.end.addButton('Выйти', QMessageBox.AcceptRole)
            self.exit.clicked.connect(self.close)
            self.stay = self.end.addButton('Остаться', QMessageBox.AcceptRole)
            self.end.exec()

    def check_data(self):
        if not self.copy_path.text() == '':
            collect_data(schet_list=unclear_list, other_data=other_data_list,
                        clear_other_data=clear_other_list, file=xlsx_file, sheet=xlsx_sheet)

            collect_unfound(copy_list=copy_data_list, copy_other_data=copy_other_list, clear_data=unclear_list,
                           unfound_numbers=unfound_numbers, clear_copy_data=clear_copy_list,
                            file=report_file, sheet=report_sheet)

            create_table(file=unfound_file)
            write_unfound(file=unfound_file, unfound_numbers=unfound_numbers, copy_other_list=copy_other_list)

            self.end = QMessageBox(self)
            self.end.setWindowTitle('Конец проверки')
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