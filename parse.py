from excel import (collect_data, xlsx_file)

from bs4 import BeautifulSoup as bs
import openpyxl as op
import pandas as pd
from datetime import datetime

unclear_list = []
clear_list = []

clear_number_list = []

main_file = xlsx_file # данные о книге
main_book = op.load_workbook(main_file)

xls = pd.ExcelFile(main_file)

main_sheet = xls.sheet_names[0]

date = str(datetime.date(datetime.now())).split('-')
new_file = f'Бронь {date[2]}.{date[1]}.{date[0]}.xlsx'

def parse_numbers(unclear_data, other_data_list, clear_other_data,
                  clear_data, data_file):
    """парсит номера из xml"""
    with open(data_file, 'r', encoding="UTF-8") as xml:
        file = xml.read()

    soup = bs(file, 'xml')

    collect_data(schet_list=unclear_data, other_data=other_data_list,
                 clear_other_data=clear_other_data, file=main_file, sheet=main_sheet)

    schetnomers = soup.find_all('SCHETNOMER')

    for data in unclear_data:
        for schetnomer in schetnomers:
            if schetnomer.text == data:

                phone = schetnomer.find_next('TELEF').text # поиск телефона

                if phone.count('+') >= 2: # если в строке больше одного номера
                    count_phones = phone.count('+') # ищет количество номеров
                    phone = phone.split('+')

                    for i in range(1, count_phones+1): # разделение номеров друг от друга
                        double_phone = f'1 +{phone[i]}'

                        if not double_phone in clear_data:
                            clear_data.append(double_phone)

                else:
                    if not phone in clear_data:
                        clear_data.append(phone)

def clean_numbers(unclear_numbers, clear_numbers):
    """приводит номера к стандарту"""
    number_list = [''.join(filter(str.isdigit, number)) for number in unclear_numbers]
    for number in number_list:
        if number[0:2] != '1 ': # если не больше одного номера
            number = '8{}{}{}{}'.format(number[1:4], number[4:7], number[7:9], number[9:11])
            if number[0:4] == '8831':
                clear_numbers.append(number[4::])
            elif number[0:4] == '8832':
                clear_numbers.append(number[4::])
            else:
                clear_numbers.append(number)

        else: # если больше одного номера
            number = '8{}{}{}{}'.format(number[1:4], number[4:7], number[7:9], number[9:11])
            if number[0:4] == '8831':
                clear_numbers.append(number[4::])
            elif number[0:4] == '8832':
                clear_numbers.append(number[4::])
            else:
                clear_numbers.append(f'1 {number}')