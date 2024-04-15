import os
from openpyxl import Workbook
from Library import databases
from Library.paths import output_dir, output_paths, public_paths

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    for path in output_paths.values():
        print(path)
        Workbook().save(path)

databases.read_public(public_paths)
databases.form_date(output_paths['date'])
databases.form_rating(output_paths['rating'])
databases.form_dailyproduction(output_paths['dailyprd'])
databases.form_total(output_paths['main'])