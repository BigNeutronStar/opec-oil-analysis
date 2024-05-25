import os
from openpyxl import Workbook
from Library import data
from Library.paths import output_dir, output_paths, public_paths

def generate():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        for path in output_paths.values():
            print(path)
            Workbook().save(path)

    data.read_public(public_paths)
    data.form_dates(output_paths['dates'])
    data.form_countries(output_paths['countries'])
    data.form_dailyproduction(output_paths['daily_production'])

    
    ##data.form_total(output_paths['main'])



