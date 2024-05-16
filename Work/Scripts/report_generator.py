import os
import pandas as pd
from datetime import datetime

# Получаем путь к текущей директории, где находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Получаем путь к директории Output (на один уровень выше папки Scripts)
output_dir = os.path.abspath(os.path.join(script_dir, '..', 'Output'))

# Проверяем, существует ли папка Output, если нет, то создаем ее
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Формируем путь к файлу Excel
file_path = os.path.join(script_dir, '..', 'Data', 'generated_data', 'db.xlsx')

# Считываем данные из файла Excel
df = pd.read_excel(file_path)


# Функция для создания текстового отчета
def generate_report(column_name, report_name):
    report_df = df[['Дата', 'Страна', column_name]]
    report_df = report_df.groupby(['Дата', 'Страна']).mean().reset_index()

    report_path = os.path.join(output_dir, report_name + '.txt')
    with open(report_path, 'w', encoding='utf-8') as file:
        header = f"{'Дата':<12} | {'Страна':<20} | {column_name}\n"
        file.write(header)
        separator = '-' * (12 + 3 + 20 + 3 + len(column_name) + 2) + '\n'
        file.write(separator)

        for _, row in report_df.iterrows():
            date = str(row['Дата'])
            country = row['Страна']
            value = str(row[column_name])
            row_str = f"{date:<12} | {country:<20} | {value}\n"
            file.write(row_str)

        file.write(separator)


def generate_annual_summary_report():
    df['Год'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year
    annual_summary = df.groupby('Год').agg({
        'Цена за баррель': 'mean',
        'Курс доллара': 'mean'
    }).reset_index()

    report_path = os.path.join(output_dir, 'annual_summary_report.txt')
    with open(report_path, 'w', encoding='utf-8') as file:
        header = f"{'Год':<5} | {'Цена за баррель (средняя)':<30} | {'Курс доллара (средний)':<20}\n"
        separator = '-' * (5 + 3 + 30 + 3 + 20 + 2) + '\n'
        file.write(header)
        file.write(separator)

        for _, row in annual_summary.iterrows():
            year = str(int(row['Год']))
            avg_price = f"{row['Цена за баррель']:.2f}"
            avg_exchange_rate = f"{row['Курс доллара']:.2f}"
            row_str = f"{year:<5} | {avg_price:<30} | {avg_exchange_rate:<20}\n"
            file.write(row_str)

        file.write(separator)


# Примеры создания отчетов
generate_report('Среднедневная добыча за год (1000 бар/д)', 'отчет_1')
generate_report('Цена за баррель', 'отчет_2')
generate_annual_summary_report()
