from openpyxl import Workbook

import flet as ft
import numpy as np
import shutil, os
import pandas as pd

class Data:
    def __init__(self):
        self.countries = pd.DataFrame()
        self.dates = pd.DataFrame()
        self.daily_production = pd.DataFrame()
        self.years = []
        self.countries_list = []
        self.is_empty = True
        self.is_in_priority = False

        self.paths = {}
    
    def set_priority(self):
        self.is_in_priority = True

    def remove_priority(self):
        self.is_in_priority = False

    def read_data(self, databases_paths):
        for key, path in databases_paths.items():
            self.paths[key] = path

        if any(not os.path.exists(path) for path in databases_paths.values()):
            self.destroy()
            return
        
        if 'countries' in databases_paths:
            self.countries = pd.read_excel(databases_paths['countries'])
            self.set_countries()
        if 'dates' in databases_paths:
            self.dates = pd.read_excel(databases_paths['dates'])
            self.dates['Дата'] = pd.to_datetime(self.dates['Дата'], format='%d.%m.%Y')
            self.dates['Дата'] = self.dates['Дата'].dt.strftime('%d.%m.%Y')
            self.set_years()
        if 'daily_production' in databases_paths:
            self.daily_production = pd.read_excel(databases_paths['daily_production'])

        self.is_empty = self.countries.empty or self.dates.empty or self.daily_production.empty

    def set_years(self):
        df = self.dates[['Дата']].copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        self.years = df['Дата'].unique()

    def set_countries(self):
        self.countries_list = self.countries['Страна']
    
    def save_data(self, name, path):
        if path == None:
            return
        if not path.endswith('.xlsx'):
            path += '.xlsx'
        Workbook().save(path)
        dict = {
            'dates' : self.dates,
            'countries' : self.countries,
            'daily_production' : self.daily_production,
        }
        dict[name].to_excel(path, index=False)
    
    def generate_datatable(self, df):
        if df.size == 0:
            return ft.Column()
        
        if df.shape[0] > 12:
            df = df.iloc[0:100]

        headers = [ft.DataColumn(ft.Text(header)) for header in df.columns]

        df_array = df.to_numpy()

        def create_row(row):
            return ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row])

        rows = np.apply_along_axis(create_row, axis=1, arr=df_array)

        if df.shape[0] > 12:
            last_row = ft.DataRow(
                cells=[ft.DataCell(ft.Text("...")) if i == 0 else ft.DataCell(ft.Text("")) for i in range(len(headers))]
            )

            rows = np.append(rows, [last_row])

        datatable = ft.DataTable(
            columns=headers,
            rows=rows
        )
        return datatable

    def destroy(self):
        self.countries = pd.DataFrame()
        self.dates = pd.DataFrame()
        self.daily_production = pd.DataFrame()
        dir = os.path.dirname(list(self.paths.values())[0])
        print(dir)
        shutil.rmtree(dir, ignore_errors=True)
        self.is_empty = True

    
class Uploader():
    def __init__(self, path):
        self.upload_path = path
        
    def upload_data(self, name, path):
        if not os.path.exists(self.upload_path):
            os.makedirs(self.upload_path)
        new_path = os.path.join(self.upload_path, name + "_personal.xlsx")
        Workbook().save(new_path)
        shutil.copy(path, new_path)
        return new_path

