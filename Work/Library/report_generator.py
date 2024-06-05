from os import makedirs, path, listdir
import pandas as pd


class ReportGenerator():
    def __init__(self, data, personal_data, path):
        self.data = data
        self.personal_data = personal_data

        self.path = path

        self.current_data = self.data

        self.check_dir()
    
    def check_dir(self):
        if not path.exists(self.path):
            makedirs(self.path)
    
    def setup_data(self):
        if self.data.is_in_priority:
            self.current_data = self.data
        else:
            self.current_data = self.personal_data

    def save_reports(self, save_dir):
        if not path.exists(save_dir):
            makedirs(save_dir)
            
        for filename in listdir(self.path):
            if filename.endswith(".txt"):
                report_path = path.join(self.path, filename)
                with open(report_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    with open(path.join(save_dir, filename), 'w', encoding='utf-8') as save_file:
                        save_file.write(content)
    
    def run_generator(self, country_name):
        reports = [
            self.generate_annual_average_report(),
            self.generate_annual_minmax_report(),
            self.generate_pivot_table(),
            self.generate_pivot_table_for_country(country_name),
        ]

        return reports

    def generate_annual_average_report(self):
        df = self.current_data.dates.copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

        pivot_table = pd.pivot_table(df, index=['Дата'], values=['Цена', 'Курс'], aggfunc='mean')
        report_path = path.join(self.path, 'annual_average_report.txt')

        with open(report_path, 'w') as f:
            header = f"{'Год':<5} | {'Цена за баррель (средняя)':<30} | {'Курс доллара (средний)':<20}\n"
            f.write(header)
            f.write('-' * len(header) + '\n')

            for year, row in pivot_table.iterrows():
                avg_price = f"{row['Цена']:.2f}"
                avg_exchange_rate = f"{row['Курс']:.2f}"
                line = f"{year:<5} | {avg_price:<30} | {avg_exchange_rate:<20}\n"
                f.write(line)

            f.write('-' * len(header) + '\n')
        return report_path

    def generate_annual_minmax_report(self):
        df = self.current_data.dates.copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

        pivot_table = pd.pivot_table(df, index=['Дата'], values=['Цена', 'Курс'], aggfunc={'Цена': ['min', 'max'], 'Курс': ['max', 'min']})
        pivot_table.columns = ['Максимальная цена за баррель', 'Минимальная цена за баррель', 'Максимальный курс доллара', 'Минимальный курс доллара']
        report_path = path.join(self.path, 'annual_minmax_report.txt')

        with open(report_path, 'w') as f:
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
        return report_path

    def generate_pivot_table(self):
        df = pd.merge(self.current_data.daily_production, self.current_data.countries, on='country_id')[['Добыча', 'Страна']]
        pivot_table = pd.pivot_table(df, index=['Страна'], values=['Добыча'], aggfunc='sum')
        report_path = path.join(self.path, 'total_production.txt')
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
        df = pd.merge(self.current_data.daily_production, self.current_data.dates, on='date_id')[['Дата', 'Добыча', 'country_id']]
        df = pd.merge(df, self.current_data.countries, on='country_id')[['Дата', 'Добыча', 'Страна']]

        df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y').dt.year

        pivot_table = pd.pivot_table(df[df['Страна'] == country_name], index=['Дата'], values=['Добыча'], aggfunc='sum')
        report_path = path.join(self.path, f'total_production_{country_name}.txt')

        with open(report_path, 'w') as f:
            header = f"{'Год':<5} | {'Суммарная добыча':<10}\n"
            f.write(header)
            f.write('-' * len(header) + '\n')

            for year, row in pivot_table.iterrows():
                line = f"{year:<5} | {row['Добыча']:<10}\n"
                f.write(line)

            f.write('-' * len(header) + '\n')
        return report_path