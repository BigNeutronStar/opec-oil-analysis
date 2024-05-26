import os
import pandas as pd
from Library.paths import report_dir
from Library import data

def generate_annual_average_report():
    df = data.dates.copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

    pivot_table = pd.pivot_table(df, index=['Дата'], values=['Цена', 'Курс'], aggfunc='mean')
    report_path = os.path.join(report_dir, 'annual_summary_report.txt')

    with open(report_path, 'w', encoding='utf-8') as f:
        header = f"{'Год':<5} | {'Цена за баррель (средняя)':<30} | {'Курс доллара (средний)':<20}\n"
        f.write(header)
        f.write('-' * len(header) + '\n')

        for year, row in pivot_table.iterrows():
            avg_price = f"{row['Цена']:.2f}"
            avg_exchange_rate = f"{row['Курс']:.2f}"
            line = f"{year:<5} | {avg_price:<30} | {avg_exchange_rate:<20}\n"
            f.write(line)

        f.write('-' * len(header) + '\n')

def generate_annual_minmax_report():
    df = data.dates.copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

    pivot_table = pd.pivot_table(df, index=['Дата'], values=['Цена', 'Курс'], aggfunc={'Цена': ['min', 'max'], 'Курс': ['max', 'min']})
    pivot_table.columns = ['Максимальная цена за баррель', 'Минимальная цена за баррель', 'Максимальный курс доллара', 'Минимальный курс доллара']
    report_path = os.path.join(report_dir, 'annual_minmax_report.txt')

    with open(report_path, 'w', encoding='utf-8') as f:
        header = f"{'Год':<5} | {'Мин. цена за баррель':<20} | {'Макс. цена за баррель':<20} | {'Макс. курс доллара':<20} | {'Мин. курс доллара':<20}\n"
        f.write(header)
        f.write('-' * len(header) + '\n')

        for year, row in pivot_table.iterrows():
            min_price = f"{row['Минимальная цена за баррель']:.2f}"
            max_price = f"{row['Максимальная цена за баррель']:.2f}"
            max_rate = f"{row['Максимальный курс доллара']:.2f}"
            min_rate = f"{row['Минимальный курс доллара']:.2f}"
            line = f"{year:<5} | {min_price:<20} | {max_price:<20} | {max_rate:<20} | {min_rate:<20}\n"
            f.write(line)

        f.write('-' * len(header) + '\n')

def generate_pivot_table():
    df = data.dates.copy()
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

def generate_pivot_table_for_country(country_name):
    df = data.main.copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

    pivot_table = pd.pivot_table(df[df['Страна'] == country_name], index=['Дата'], values=['Добыча'], aggfunc='sum')
    report_path = os.path.join(report_dir, f'total_production_{country_name}.txt')

    with open(report_path, 'w', encoding='utf-8') as f:
        header = f"{'Год':<5} | {'Суммарная добыча':<10}\n"
        f.write(header)
        f.write('-' * len(header) + '\n')

        for year, row in pivot_table.iterrows():
            line = f"{year:<5} | {row['Добыча']:<10}\n"
            f.write(line)

        f.write('-' * len(header) + '\n')

