import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd

matplotlib.use('agg')

class GraphGenerator():
    def __init__(self, data, personal_data, path):
        self.data = data
        self.personal_data = personal_data

        self.path = path

        self.current_data = self.data
    
    def setup_data(self):
        if self.data.is_in_priority:
            self.current_data = self.data
        else:
            self.current_data = self.personal_data

    def plot_boxwhiskers(self, atribute, start=2006, end=2022, countries=[]):
        margins = {                                                                                         
            "left"   : 0.06,
            "bottom" : 0.03,
            "right"  : 0.99,
            "top"    : 0.97  
        }
        fig = plt.figure()
        fig.subplots_adjust(**margins)  
        if atribute == 'Курс':
            df = self.current_data.dates[['Дата', 'Курс']].copy()
            df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
            df = df[(df['Дата'] <= end) & (df['Дата'] >= start)]
            column = df[atribute]
            fig.set_size_inches(10, 10)
            plt.ylabel('1$/1P')
            plt.boxplot(column, showmeans=True)
            plt.xticks([])
            plt.yticks(np.linspace(min(column), max(column), endpoint=True))
            path = self.path + "/Box&Whiskers" + "/Курс.png"
        elif atribute == 'Цена':
            df = self.current_data.dates[['Дата', 'Цена']].copy()
            df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
            df = df[(df['Дата'] <= end) & (df['Дата'] >= start)]
            column = df[atribute]
            fig.set_size_inches(10, 10)
            plt.ylabel('Рубли')
            plt.boxplot(column, showmeans=True)
            plt.xticks([])
            plt.yticks(np.linspace(min(column), max(column), endpoint=True))
            path = self.path + "/Box&Whiskers" + "/Цена.png"

        elif atribute == 'Добыча':
            df = pd.merge(self.current_data.daily_production, self.current_data.dates, on='date_id')[['Дата', 'Добыча', 'country_id']]
            df = pd.merge(df, self.current_data.countries, on='country_id')[['Дата', 'Добыча', 'Страна']]
            df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
            df = df[(df['Дата'] <= end) & (df['Дата'] >= start)]

            if len(countries) != 0: 
                df = df[df['Страна'].isin(countries)]

            df.groupby(['Страна', 'Дата'])['Добыча'].mean()
            grouped_data = df.groupby(['Страна'])['Добыча'].agg(list)
            fig.set_size_inches(15, 10)
            plt.boxplot(grouped_data, showmeans=True)
            plt.xticks(ticks=range(1, len(grouped_data) + 1), labels=grouped_data.index)
            plt.title('Среднедневная добыча 2006-2022 гг.')
            plt.ylabel('Среднедневная добыча (1000 бар/д)')
            plt.grid(True)
            plt.suptitle('')

            path = self.path + "/Box&Whiskers" + "/Добыча.png"
            
        plt.grid(True)
        plt.title(f'{atribute} {start}-{end} гг.')
        if not os.path.exists(path):
            self.save_graph(fig, path)
        return fig

    def plot_graph(self, atribute, start=2006, end=2022):
        margins = {                                                                                         
            "left"   : 0.05,
            "bottom" : 0.05,
            "right"  : 0.99,
            "top"    : 0.97  
        }
        fig = plt.figure(figsize=(20,15))
        fig.subplots_adjust(**margins)  
        if (atribute == 'Курс'):
            df = self.current_data.dates[['Дата', 'Курс']].copy()
            df['Дата'] = pd.to_datetime(self.current_data.dates['Дата'], format="%d.%m.%Y")
            df = df[(df['Дата'].dt.year <= end) & (df['Дата'].dt.year >= start)]
            plt.plot(df['Дата'], df['Курс'], label='Курс рубля')
            path = self.path + "/Графики" + "/Курс.png"
        elif (atribute == 'Цена'):
            df = self.current_data.dates[['Дата', 'Цена']].copy()
            df['Дата'] = pd.to_datetime(self.current_data.dates['Дата'], format="%d.%m.%Y")
            df = df[(df['Дата'].dt.year <= end) & (df['Дата'].dt.year >= start)]
            plt.plot(df['Дата'], df['Цена'], label='Цена на нефть')
            path = self.path + "/Графики" + "/Цена.png"
        plt.title(f'{atribute} {start}-{end} гг.', fontsize=18)
        plt.xlabel('Дата', fontsize=18)
        plt.ylabel('Рубли', fontsize=18)
        plt.xticks(rotation=0)
        plt.tick_params(axis='both', labelsize=14)
        plt.grid(True)
        
        if not os.path.exists(path):
            self.save_graph(fig, path)
        return fig
        
    def hist(self, start=2006, end=2022, countries=[]):
        df = pd.merge(self.current_data.daily_production, self.current_data.dates, on='date_id')[['Дата', 'Добыча', 'country_id']]
        df = pd.merge(df, self.current_data.countries, on='country_id')[['Дата', 'Добыча', 'Страна']]
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        df = df[(df['Дата'] <= end) & (df['Дата'] >= start)]

        if len(countries) != 0: 
                df = df[df['Страна'].isin(countries)]

        grouped_data = df.groupby(['Страна', 'Дата'], as_index=False)['Добыча'].mean()

        years = sorted(grouped_data['Дата'].unique())

        grouped_data = grouped_data.groupby(['Страна'])['Добыча'].agg(list)

        num_years = len(years)
        n_cols = min(num_years, 3)  
        n_rows = (num_years + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))  

        if num_years == 1:
            axes = [axes]
        else:
            axes = axes.flatten()
        
        for idx, year in enumerate(years):
            ax = axes[idx]
            ax.hist([prod[idx] for prod in grouped_data if len(prod) > idx], alpha=0.7, color='skyblue', edgecolor='black', bins=10)
            ax.set_title(year)
            ax.yaxis.set_major_locator(MultipleLocator(base=1))
            ax.xaxis.set_major_locator(MultipleLocator(base=500))
            ax.grid(True, axis='y')
            ax.set_xlabel('Среднедневная добыча')
            ax.set_ylabel('Частота')

        for idx in range(len(years), len(axes)):
            fig.delaxes(axes[idx])
                
        plt.suptitle('Гистограммы среднедневной добычи по годам', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.98])
        path = self.path + "/Гистограмма" + "/Добыча.png"
        if not os.path.exists(path):
            self.save_graph(fig, path)
        return fig

    def diag(self, start=2006, end=2022, countries=[]):
        df = pd.merge(self.current_data.daily_production, self.current_data.dates, on='date_id')[['Дата', 'Добыча', 'country_id']]
        df = pd.merge(df, self.current_data.countries, on='country_id')[['Дата', 'Добыча', 'Страна']]
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        df = df[(df['Дата'] <= end) & (df['Дата'] >= start)]

        if len(countries) != 0: 
                df = df[df['Страна'].isin(countries)]

        grouped_data = df.groupby(['Страна', 'Дата'], as_index=False)['Добыча'].mean()

        countries = grouped_data['Страна'].unique()
        years = grouped_data['Дата'].unique()
        
        grouped_data = grouped_data.groupby(['Страна'])['Добыча'].agg(list)

        margins = {                                                                                         
            "left"   : 0.06,
            "bottom" : 0.06,
            "right"  : 0.89,
            "top"    : 0.97  
        }

        fig = plt.figure(figsize=(19, 14))
        fig.subplots_adjust(**margins)  
        plt.title("Кластеризованная столбчатая диаграмма по среднедневной добыче", fontsize=18)

        bar_width = 0.05
        k = -6

        for c in countries:
            plt.bar([i + k*bar_width for i in years], grouped_data[c], width=bar_width, align='center', label=c)
            k += 1

        plt.ylabel('Среднедневная добыча (1000 бар/д)', fontsize=18)
        plt.yticks(np.arange(min(df['Добыча']), max(df['Добыча']), 100))
        plt.xticks([y for y in years], labels=years)
        plt.tick_params(axis='both', labelsize=14)
        plt.grid(True, axis='y')
        plt.legend(loc='upper right', bbox_to_anchor=(1.13, 1))
        path = self.path + "/Диаграмма" + "/Добыча.png"
        if not os.path.exists(path):
            self.save_graph(fig, path)
        return fig

    def plot_scatter(self, atribute, start=2006, end=2022, countries=[]):
        atr = self.current_data.dates[['Дата', atribute]].copy()
        atr['Дата'] = pd.to_datetime(atr['Дата'], format='mixed', dayfirst=True).dt.year
        atr = atr[(atr['Дата'] <= end) & (atr['Дата'] >= start)]
        atr = atr[atribute]

        df = pd.merge(self.current_data.daily_production, self.current_data.dates, on='date_id')[['Дата', 'Добыча', 'country_id']]
        df = pd.merge(df, self.current_data.countries, on='country_id')[['Дата', 'Добыча', 'Страна']]
        
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        df = df[(df['Дата'] <= end) & (df['Дата'] >= start)]
        
        if len(countries) != 0: 
                df = df[df['Страна'].isin(countries)]

        grouped_data = df.groupby('Страна')['Добыча'].agg(list)

        margins = {                                                                                         
            "left"   : 0.06,
            "bottom" : 0.06,
            "right"  : 0.988,
            "top"    : 0.986  
        }
        fig = plt.figure(figsize=(20, 20))
        fig.subplots_adjust(**margins)                            
        
        for c, prod in grouped_data.items():
            plt.scatter(atr, prod, label=c, s=10)
        plt.title('Категоризированная диаграмма рассеивания:', fontsize=18)
        plt.xlabel(f'{atribute}', fontsize=18)
        plt.ylabel('Добыча дневная (1000 баррелей/день)', fontsize=18)
        plt.legend(title='Название страны')
        plt.tick_params(axis='both', labelsize=14)
        plt.grid(True)
        path = self.path + "/Рассеивание" + "/Рассеивание.png"
        if not os.path.exists(path):
            self.save_graph(fig, path)
        return fig

    def save_graph(self, fig, path):
        print(path)
        fig.savefig(path)

    def clear(self):
        plt.close('all')