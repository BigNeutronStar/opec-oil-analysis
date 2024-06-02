from openpyxl import Workbook
from Library import data
from Library.paths import databases_paths
import flet as ft
import pandas as pd
import numpy as np

def read_data():
    data.read_data(databases_paths)

def get_years_range():
    return min(data.years), max(data.years)

def get_countries():
    return data.countries_list

def generate_datatable(df):
    if df.shape[0] > 12:
        df = df.iloc[0:100]

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

def save_data(name, path):
    if not path.endswith('.xlsx'):
        path += '.xlsx'
    Workbook().save(path)
    dict = {
        'dates' : data.dates,
        'countries' : data.countries,
        'daily_production' : data.daily_production,
    }
    dict[name].to_excel(path, index=False)

