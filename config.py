import os
import pathlib

ROOT = pathlib.Path(__file__).parent
DATA_EMPLOYEES = pathlib.Path(ROOT, 'homework-1', 'north_data', 'employees_data.csv')

PASS = os.getenv('Password')
