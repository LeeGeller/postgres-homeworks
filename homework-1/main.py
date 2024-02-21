import csv

import psycopg2

from config import DATA_EMPLOYEES, PASS, DATA_CUSTOMERS, DATA_ORDERS


def open_data_file(data) -> list:
    """
    Открывает файл csv. Перебирает его и создает список из словарей.
    Т.к. в БД в колонке employee_id должен быть тип int,
    меняем тип в row по ключу 'employee_id'.
    :data: путь до файла
    :return: список из словарей
    """
    new_list = []

    with open(data, encoding='utf-8') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            if row.get('employee_id'):
                row['employee_id'] = int(row['employee_id'])
            new_list.append(row)
    return new_list


def add_data_to_database(data_list: list, name_table: str, column_count: int) -> None:
    """
    Отправляет информацию в БД.
    :data_list: список из словарей, заполненный данными
    :name_table: название таблицы, куда отправляется инфо
    :column_count: количество столбцов в этой таблице
    """
    count = '%s ' * column_count
    with psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password=PASS
    ) as conn:
        with conn.cursor() as cur:
            for data_info in data_list:
                val = tuple(data_info.values())
                cur.execute(f"INSERT INTO {name_table} VALUES ({', '.join(count.split())})", val)
                print(val)
    conn.close()
