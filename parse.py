from excel import (collect_data, xlsx_file, report_file)
                   # clear_other_list, other_data_list, collect_unfound, unfound_file, log_list,
                   # copy_data_list, copy_other_list, unfound_numbers, write_unfound, clear_copy_list,
                   # create_table, write_data, xml_file, check_list, check_numbers, log_file, write_log)

from bs4 import BeautifulSoup as bs
import openpyxl as op
import pandas as pd
from datetime import datetime

xlsx_book = op.load_workbook(xlsx_file) # данные о книге
xlsx = pd.ExcelFile(xlsx_file)
xlsx_sheet = xlsx.sheet_names[0]

report_book = op.load_workbook(report_file) # данные о логе
report = pd.ExcelFile(report_file)
report_sheet = report.sheet_names[0]

unclear_list = []
clear_list = []
clear_number_list = []

date = str(datetime.date(datetime.now())).split('-')
new_file = f'Бронь {date[2]}.{date[1]}.{date[0]}.xlsx'

def parse_numbers(unclear_data, other_data_list, clear_other_data,
                  clear_data, log_list, data_file, my_file, my_sheet):
    """парсит номера из xml"""
    with open(data_file, 'r', encoding="UTF-8") as xml:
        file = xml.read()

    soup = bs(file, 'xml')

    collect_data(schet_list=unclear_data, other_data=other_data_list,
                 clear_other_data=clear_other_data, file=my_file, sheet=my_sheet)

    schetnomers = soup.find_all('SCHETNOMER')

    for data in unclear_data: # просмотр списка с чистыми счетами
        for schetnomer in schetnomers: # просмотр списка со счетами из xml
            if schetnomer.text == data:

                phone = schetnomer.find_next('TELEF').text # поиск телефона

                if phone.count('+') >= 2: # если в строке больше одного номера
                    count_phones = phone.count('+') # ищет количество номеров
                    phone = phone.split('+')

                    for i in range(1, count_phones+1): # разделение номеров друг от друга
                        double_phone = f'+{phone[i]}'

                        if not double_phone in clear_data:
                            clear_data.append(double_phone)

                else:
                    if not phone in clear_data:
                        clear_data.append(phone)

            else:
                log_list.append(schetnomer.text)

def clean_numbers(unclear_numbers, clear_numbers):
    """приводит номера к стандарту"""
    number_list = [''.join(filter(str.isdigit, number)) for number in unclear_numbers]
    for number in number_list:
        number = '8{}{}{}{}'.format(number[1:4], number[4:7], number[7:9], number[9:11])
        if number[0:4] == '8831':
            clear_numbers.append(number[4::])
        else:
            clear_numbers.append(number)

# parse_numbers(unclear_data=unclear_list, clear_data=clear_list, other_data_list=other_data_list,
#               clear_other_data=clear_other_list, data_file=xml_file,
#               my_file=xlsx_file, my_sheet=xlsx_sheet, log_list=log_list)
#
# clean_numbers(unclear_numbers=clear_list, clear_numbers=clear_number_list)
#
# create_table(file=new_file)
# write_data(file=new_file, number_list=clear_number_list, other_data_list=clear_other_list)
#
# check_numbers(unclear_data=unclear_list, log_list=log_list, check_list=check_list)
#
# create_table(file=log_file)
# write_log(file=log_file, check_list=check_list)
#
# collect_data(schet_list=unclear_list, other_data=other_data_list,
#             clear_other_data=clear_other_list, file=xlsx_file, sheet=xlsx_sheet)
#
# collect_unfound(copy_list=copy_data_list, copy_other_data=copy_other_list, clear_data=unclear_list,
#                unfound_numbers=unfound_numbers, clear_copy_data=clear_copy_list, file=report_file, sheet=report_sheet)
#
# create_table(file=unfound_file)
# write_unfound(file=unfound_file, unfound_numbers=unfound_numbers, copy_other_list=copy_other_list)