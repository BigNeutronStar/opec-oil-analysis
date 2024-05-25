from openpyxl import Workbook
from Library import data
from Library.paths import databases_paths

def generate_main():
    Workbook().save(databases_paths['main'])
    data.collect_to_main(databases_paths['main'])

def read_data():
    data.read_data(databases_paths)


