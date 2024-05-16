import os
import pandas as pd

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
    # Выбираем только нужные столбцы
    report_df = df[['Дата', 'Страна', column_name]]
    
    # Группируем по дате и стране и находим среднее значение для 'Среднедневная добыча за год (1000 бар/д)'
    report_df = report_df.groupby(['Дата', 'Страна']).mean().reset_index()
    
    # Сохраняем в текстовый файл в папку Output
    with open(os.path.join(output_dir, report_name + '.txt'), 'w') as file:
        # Заголовок таблицы
        header = f"{'Дата':<12} | {'Страна':<20} | {column_name}\n"
        file.write(header)
        
        # Разделитель
        separator = '-' * (12 + 3 + 20 + 3 + len(column_name) + 2) + '\n'
        file.write(separator)
        
        # Записываем данные
        for _, row in report_df.iterrows():
            date = str(row['Дата'])
            country = row['Страна']
            value = str(row[column_name])
            row_str = f"{date:<12} | {country:<20} | {value}\n"
            file.write(row_str)
        
        # Завершающий разделитель
        file.write(separator)

# Создаем текстовые отчеты для каждого требуемого столбца
generate_report('Среднедневная добыча за год (1000 бар/д)', 'отчет_1')
generate_report('Цена за баррель', 'отчет_2')
generate_report('Курс доллара', 'отчет_3')  # Примерный отчет, так как нет данных для каждой даты и страны
generate_report('Добыча (1000 бар)', 'отчет_4')  # Примерный отчет, так как нет данных для каждой даты и страны
