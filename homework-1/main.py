import csv

import psycopg2

from config import DATA_EMPLOYEES, PASS


def open_data_file(data) -> list:
    new_list = []

    with open(data, encoding='utf-8') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            try:
                row['employee_id'] = int(row['employee_id'])
            except:
                continue
            new_list.append(row)
    return new_list


def add_data_to_database(data_list: list, name_table: str, column_count: int) -> None:
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


data_list = open_data_file(DATA_EMPLOYEES)
add_data_to_database(data_list, 'employees', 6)
