"""
Модуль для генерации различных отчетов на основе данных.

Авторы: 
    Рахматуллин Айгиз,
    Мирумян Артем,
    Наумов Виталий
"""
import os
import pandas as pd


class ReportGenerator():
    """
    Класс для генерации различных отчетов на основе данных.
    """

    def __init__(self, data, personal_data, path):
        """
        Инициализация класса ReportGenerator.

        Вход:
            self (ReportGenerator): Экземпляр класса ReportGenerator.
            data (Data): Основные данные.
            personal_data (Data): Персональные данные.
            path (str): Путь для сохранения отчетов.

        Автор: 
            Наумов Виталий
        """
        self.data = data
        self.personal_data = personal_data
        self.path = path
        self.current_data = self.data
        self.check_dir()

    def check_dir(self):
        """
        Проверка существования директории и создание её при необходимости.

        Автор: 
            Наумов Виталий
        """
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def setup_data(self):
        """
        Настройка текущих данных на основе приоритета.

        Автор: 
            Наумов Виталий
        """
        if self.data.is_in_priority:
            self.current_data = self.data
        else:
            self.current_data = self.personal_data

    def save_reports(self, save_dir):
        """
        Сохранение отчетов в указанную директорию.

        Вход:
            save_dir (str): Путь для сохранения отчетов.

        Автор: 
            Наумов Виталий
        """
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for filename in os.listdir(self.path):
            if filename.endswith(".txt"):
                report_path = os.path.join(self.path, filename)
                with open(report_path, 'r') as file:
                    content = file.read()
                    with open(os.path.join(save_dir, filename), 'w') as save_file:
                        save_file.write(content)

    def run_generator(self, country_name):
        """
        Запуск генерации всех отчетов и возврат их путей.

        Вход:
            country_name (str): Название страны для фильтрации данных.

        Выход:
            reports (list): Список путей к сгенерированным отчетам.

        Автор: 
            Мирумян Артем
        """
        reports = [
            self.generate_annual_average_report(),
            self.generate_annual_minmax_report(),
            self.generate_pivot_table(),
            self.generate_pivot_table_for_country(country_name),
        ]

        return reports

    def generate_annual_average_report(self):
        """
        Генерация отчета о средних значениях по годам.

        Выход:
            report_path (str): Путь к сгенерированному отчету.

        Автор: 
            Рахматуллин Айгиз, Мирумян Артем
        """
        df = self.current_data.dates.copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

        pivot_table = pd.pivot_table(df, index=['Дата'], values=[
                                     'Цена', 'Курс'], aggfunc='mean')
        report_path = os.path.join(self.path, 'annual_average_report.txt')

        with open(report_path, 'w') as f:
            header = f"{'Год':<5} | {'Цена за баррель (средняя)':<30} | {
                'Курс доллара (средний)':<20}\n"
            f.write(header)
            f.write('-' * len(header) + '\n')

            for year, row in pivot_table.iterrows():
                avg_price = f"{row['Цена']:.2f}"
                avg_exchange_rate = f"{row['Курс']:.2f}"
                line = f"{year:<5} | {avg_price:<30} | {
                    avg_exchange_rate:<20}\n"
                f.write(line)

            f.write('-' * len(header) + '\n')
        return report_path

    def generate_annual_minmax_report(self):
        """
        Генерация отчета о минимальных и максимальных значениях по годам.

        Выход:
            report_path (str): Путь к сгенерированному отчету.

        Автор: 
            Рахматуллин Айгиз, Мирумян Артем
        """
        df = self.current_data.dates.copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

        pivot_table = pd.pivot_table(df, index=['Дата'], values=['Цена', 'Курс'], aggfunc={
                                     'Цена': ['min', 'max', 'mean'], 'Курс': ['min', 'max', 'mean']})
        pivot_table.columns = ['Максимальный курс доллара', 'Средний курс доллара', 'Минимальный курс доллара', 'Максимальная цена за баррель',
                               'Средняя цена за баррель', 'Минимальная цена за баррель']

        report_path = os.path.join(self.path, 'annual_minmax_report.txt')

        with open(report_path, 'w') as f:
            header = f"{'Год':<5} | {'Мин. цена за баррель':<20} | {'Макс. цена за баррель':<20} | {
                'Ср. цена за баррель':<20} | {'Мин. курс доллара':<20} | {'Макс. курс доллара':<20}| {'Ср. курс доллара':<20}\n"
            f.write(header)
            f.write('-' * len(header) + '\n')

            for year, row in pivot_table.iterrows():
                min_price = f"{row['Минимальная цена за баррель']:.2f}"
                max_price = f"{row['Максимальная цена за баррель']:.2f}"
                sr_price = f"{row['Средняя цена за баррель']:.2f}"
                min_rate = f"{row['Минимальный курс доллара']:.2f}"
                max_rate = f"{row['Максимальный курс доллара']:.2f}"
                sr_rate = f"{row['Средний курс доллара']:.2f}"
                line = f"{year:<5} | {min_price:<20} | {max_price:<20} | {
                    sr_price:<20} | {min_rate:<20} | {max_rate:<20} | {sr_rate:<20}\n"
                f.write(line)

            f.write('-' * len(header) + '\n')

        return report_path

    def generate_pivot_table(self):
        """
        Генерация сводной таблицы по суммарной добыче.

        Выход:
            report_path (str): Путь к сгенерированному отчету.

        Автор: 
            Рахматуллин Айгиз
        """
        df = pd.merge(self.current_data.daily_production,
                      self.current_data.countries, on='country_id')[['Добыча', 'Страна']]
        pivot_table = pd.pivot_table(df, index=['Страна'], values=[
                                     'Добыча'], aggfunc='sum')
        report_path = os.path.join(self.path, 'total_production.txt')
        with open(report_path, 'w') as f:
            header = f"{'Страна':<20} | {'Суммарная добыча':<10}"
            f.write(header + '\n')
            f.write('-' * len(header) + '\n')

            for index, row in pivot_table.iterrows():
                line = f"{index:<20} | {row['Добыча']:<10}"
                f.write(line + '\n')

            f.write('-' * len(header) + '\n')
        return report_path

    def generate_pivot_table_for_country(self, country_name):
        """
        Генерация сводной таблицы по суммарной добыче для заданной страны.

        Вход:
            country_name (str): Название страны для фильтрации данных.

        Выход:
            report_path (str): Путь к сгенерированному отчету.

        Автор: 
            Рахматуллин Айгиз
        """
        df = pd.merge(self.current_data.daily_production, self.current_data.dates, on='date_id')[
            ['Дата', 'Добыча', 'country_id']]
        df = pd.merge(df, self.current_data.countries, on='country_id')[
            ['Дата', 'Добыча', 'Страна']]

        df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

        pivot_table = pd.pivot_table(df[df['Страна'] == country_name], index=[
                                     'Дата'], values=['Добыча'], aggfunc='sum')
        report_path = os.path.join(
            self.path, f'total_production_{country_name}.txt')

        with open(report_path, 'w') as f:
            header = f"{'Год':<5} | {'Суммарная добыча':<10}\n"
            f.write(header)
            f.write('-' * len(header) + '\n')

            for year, row in pivot_table.iterrows():
                line = f"{year:<5} | {row['Добыча']:<10}\n"
                f.write(line)

            f.write('-' * len(header) + '\n')
        return report_path
