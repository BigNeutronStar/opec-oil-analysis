from openpyxl import Workbook
from Library import data
from Library.paths import main, databases_paths

def generate_main():
    Workbook().save(main)
    data.read_data(databases_paths)
    data.collect_to_main(main)



