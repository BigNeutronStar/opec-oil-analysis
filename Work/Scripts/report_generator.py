import os
import pandas as pd
from datetime import datetime
from Library.paths import report_dir
from Library import data



def save_reports(output_dir):
    for filename in os.listdir(output_dir):
        if filename.endswith(".txt"):
            report_path = os.path.join(output_dir, filename)
            with open(report_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)

def generate_annual_average_report():
    df = data.dates.copy()
    df['Дата'] = pd.to_datetime(data.dates['Дата'], format='%d.%m.%Y').dt.year
    annual_summary = df.groupby('Дата').agg({
        'Цена': 'mean',
        'Курс': 'mean'
    }).reset_index()

    report_path = os.path.join(report_dir, 'annual_summary_report.txt')
    with open(report_path, 'w', encoding='utf-8') as file:
        header = f"{'Год':<5} | {'Цена за баррель (средняя)':<30} | {'Курс доллара (средний)':<20}\n"
        separator = '-' * (5 + 3 + 30 + 3 + 20 + 2) + '\n'
        file.write(header)
        file.write(separator)

        for _, row in annual_summary.iterrows():
            year = str(int(row['Дата']))
            avg_price = f"{row['Цена']:.2f}"
            avg_exchange_rate = f"{row['Курс']:.2f}"
            row_str = f"{year:<5} | {avg_price:<30} | {avg_exchange_rate:<20}\n"
            file.write(row_str)

        file.write(separator)

def generate_annual_minmax_report():
    df = data.dates.copy()
    df['Дата'] = pd.to_datetime(data.dates['Дата'], format='%d.%m.%Y').dt.year
    annual_summary = df.groupby('Дата').agg({
        'Цена': ['min', 'max'],
        'Курс': ['max', 'min']
    }).reset_index()
    annual_summary.columns = ['Год', 'Минимальная цена за баррель', 'Максимальная цена за баррель', 'Максимальный курс доллара', 'Минимальный курс доллара']

    report_path = os.path.join(report_dir, 'annual_minmax_report.txt')
    with open(report_path, 'w', encoding='utf-8') as file:
        header = f"{'Год':<5} | {'Мин. цена за баррель':<20} | {'Макс. цена за баррель':<20} | {'Макс. курс доллара':<20} | {'Мин. курс доллара':<20}\n"
        separator = '-' * (5 + 4 + 20 + 4 + 20 + 4 + 20 + 4 + 20) + '\n'
        file.write(header)
        file.write(separator)

        for _, row in annual_summary.iterrows():
            year = str(int(row['Год']))
            min_price = f"{row['Минимальная цена за баррель']:.2f}"
            max_price = f"{row['Максимальная цена за баррель']:.2f}"
            max_rate = f"{row['Максимальный курс доллара']:.2f}"
            min_rate = f"{row['Минимальный курс доллара']:.2f}"
            row_str = f"{year:<5} | {min_price:<20} | {max_price:<20} | {max_rate:<20} | {min_rate:<20}\n"
            file.write(row_str)

        file.write(separator)

def generate_pivot_table():
    pivot_table = pd.pivot_table(data.main, index=['Страна'], values=['Добыча'], aggfunc='sum')
    report_path = os.path.join(report_dir, 'total_production.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        header = f"{'Страна':<20} | {'Суммарная добыча':<10}"
        f.write(header + '\n')
        f.write('-' * len(header) + '\n')

        for index, row in pivot_table.iterrows():
            line = f"{index:<20} | {row['Добыча']:<10}"
            f.write(line + '\n')

        f.write('-' * len(header) + '\n')