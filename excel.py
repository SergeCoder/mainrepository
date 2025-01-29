import openpyxl as op
import pandas as pd
import os
from datetime import datetime

unclear_list = []
clear_list = []

clear_number_list = []

xlsx_files = []
xml_files = []
xlsx_dates = []
xml_dates = []

def open_book(xlsx_files, xml_files, xlsx_dates, xml_dates):
    """открытие книг"""
    all_files = os.listdir()
    for file in all_files:
        if '.xlsx' in file: # поиск xlsx файла
            xlsx_files.append(file)
            xlsx_dates.append(file[-15:-5:])

        if '.xml' in file: # поиск xml файла
            xml_files.append(file)
            xml_dates.append(file[-15:-4:])

open_book(xlsx_files=xlsx_files, xml_files=xml_files, xlsx_dates=xlsx_dates, xml_dates=xml_dates)

xlsx_file = (f'{os.path.dirname(os.path.abspath(__file__))}\\'
             f'{xlsx_files[xlsx_dates.index(max(xlsx_dates))]}')

xml_file = (f'{os.path.dirname(os.path.abspath(__file__))}\\'
            f'{xml_files[xml_dates.index(max(xml_dates))]}')

old_xlsx_file = (f'{os.path.dirname(os.path.abspath(__file__))}\\'
                 f'{xlsx_files[xlsx_dates.index(min(xlsx_dates))]}')

date = str(datetime.date(datetime.now())).split('-')
new_file = f'Бронь {date[2]}.{date[1]}.{date[0]}.xlsx'

def collect_data(schet_list, file, sheet):
    """сбор данных из прайс-листа"""
    info = pd.read_excel(file, sheet) # поиск количества строк
    count = info.count().to_list()
    count = count[6]

    df = pd.read_excel(file, sheet_name=sheet)
    numbers = df.iloc[:, 6] # поиск столбца со счетами

    for number in range(3, count+2): # форматирование счетов
        schetnomer = numbers[number]
        schetnomer = schetnomer.split(' ')[1]

        schet_list.append(schetnomer)

def create_table(file):
    """создание новой таблицы"""
    book = op.Workbook()
    sheet = book.active

    book.save(file)
    book.close()

def write_data(file, number_list):
    """запись информации в новую книгу"""
    book = op.load_workbook(file)
    sheet = book['Sheet']

    row = 5
    for number in number_list:
        if number[0:2] != '1 ':
            sheet[f'A{row}'] = int(number)
        else:
            sheet[f'A{row}'] = int(number[2::])

        row += 1

    book.save(file)
    book.close()