import csv

import psycopg2

from config import DATA_EMPLOYEES

"""Скрипт для заполнения данными таблиц в БД Postgres."""


def open_data_file(data):
    with open(data, encoding='utf-8') as file:
        return csv.DictReader(file.read())


print(open_data_file(DATA_EMPLOYEES))
