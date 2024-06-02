from openpyxl import Workbook
from Library import data
from Library.paths import databases_paths
import flet as ft
import pandas as pd
import numpy as np

def generate_main():
    Workbook().save(databases_paths['main'])
    data.collect_to_main(databases_paths['main'])

def read_data():
    data.read_data(databases_paths)

def get_years_range():
    return min(data.years), max(data.years)

def get_countries():
    return data.countries_list

def generate_datatable(df):
    headers = [ft.DataColumn(ft.Text(header)) for header in df.columns]

    df_array = df.to_numpy()

    def create_row(row):
        return ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row])

    rows = np.apply_along_axis(create_row, axis=1, arr=df_array)
    
    datatable = ft.DataTable(
        columns=headers,
        rows=rows
    )
    return datatable

