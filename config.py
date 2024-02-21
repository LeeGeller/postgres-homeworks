import os
import pathlib

ROOT = pathlib.Path(__file__).parent
DATA_EMPLOYEES = pathlib.Path(ROOT, 'homework-1', 'north_data', 'employees_data.csv')
DATA_CUSTOMERS = pathlib.Path(ROOT, 'homework-1', 'north_data', 'customers_data.csv')
DATA_ORDERS = pathlib.Path(ROOT, 'homework-1', 'north_data', 'orders_data.csv')

PASS = os.getenv('Password')
