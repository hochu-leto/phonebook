# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке
# изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О; привести все телефоны в формат +7(
# 999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999; объединить все
# дублирующиеся записи о человеке в одну.
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
phone_pattern = re.compile(r"([\+7|8)]+)\s*\(?(\d{3})\)?[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]*(\d{2})\s*(\(?(\w+\.)\s*("
                           r"\d+)\)?)*")
result = []
for contacts in contacts_list:
    fio = ','.join(contacts[:3])
    fio = fio.replace(' ', ',')
    result_list = fio.split(',')
    result_list = result_list[:3] + contacts[3:]
    result_list[5] = phone_pattern.sub(r"+7(\2)\3-\4-\5 \7\8 ", result_list[5]).strip()

    for c in result:
        if (c[0] + c[1]) == (result_list[0] + result_list[1]):
            for item in range(len(c) - 1):
                if result_list[item] == '':
                    result_list[item] = c[item]
            result.remove(c)
    result.append(result_list)
pprint(result)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result)
