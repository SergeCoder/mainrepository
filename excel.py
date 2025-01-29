import openpyxl as op
import pandas as pd
import os
from datetime import datetime

unclear_list = []
clear_list = []

clear_number_list = []
other_data_list = []
clear_other_list = []


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


date = str(datetime.date(datetime.now())).split('-')
new_file = f'Бронь {date[2]}.{date[1]}.{date[0]}.xlsx'

def collect_data(schet_list, other_data, clear_other_data, file, sheet):
    """сбор данных из прайс-листа"""
    info = pd.read_excel(file, sheet) # поиск количества строк
    count = info.count().to_list()
    count = count[6]

    df = pd.read_excel(file, sheet_name=sheet)
    numbers = df.iloc[:, 6] # поиск информации в таблице
    names = df.iloc[:, 1]
    inns = df.iloc[:, 2]
    start_dates = df.iloc[:, 4]
    end_dates = df.iloc[:, 5]
    schets = df.iloc[:, 6]
    prices_schets = df.iloc[:, 7]
    discounts = df.iloc[:, 8]
    makets = df.iloc[:, 9]
    prices_makets = df.iloc[:, 10]

    for number in range(3, count+2): # форматирование счетов и данных
        schetnomer = numbers[number]
        schetnomer = schetnomer.split(' ')[1]

        name = names[number]
        inn = inns[number]
        start_date = start_dates[number]
        end_date = end_dates[number]
        schet = schets[number]
        price_schet = prices_schets[number]
        discount = discounts[number]
        maket = makets[number]
        price_maket = prices_makets[number]

        if schetnomer != '':
            schet_list.append(schetnomer)

        if not schet in other_data:
            other_data.append([name, inn, start_date, end_date, schet,
                               price_schet, discount, maket, price_maket])

    for data in other_data:
        for clear_schet in schet_list:
            if clear_schet in data[4]:
                clear_other_data.append([data[0], data[1], data[2], data[3], data[4],
                                         data[5], data[6], data[7], data[8]])

def create_table(file):
    """создание новой таблицы"""
    book = op.Workbook()
    sheet = book.active

    book.save(file)
    book.close()

def write_data(file, number_list, other_data_list):
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

    row = 5
    for data in other_data_list:
        sheet[f'B{row}'] = data[0]
        sheet[f'C{row}'] = data[1]
        sheet[f'E{row}'] = data[2]
        sheet[f'F{row}'] = data[3]
        sheet[f'G{row}'] = data[4]
        sheet[f'H{row}'] = data[5]
        sheet[f'I{row}'] = data[6]
        sheet[f'J{row}'] = data[7]
        sheet[f'K{row}'] = data[8]

        row += 1

    book.save(file)
    book.close()