import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd

from Library import paths
from Library import data

matplotlib.use('agg')

def plot_boxwhiskers(atribute, start=2006, end=2022, countries={}):
    margins = {                                                                                         
        "left"   : 0.06,
        "bottom" : 0.03,
        "right"  : 0.99,
        "top"    : 0.97  
    }
    fig = plt.figure()
    fig.subplots_adjust(**margins)  
    if atribute == 'Курс':
        df = data.dates[['Дата', 'Курс']].copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        df = df[df['Дата'] <= end and df['Дата'] >= start]
        column = df[atribute]
        fig.set_size_inches(10, 10)
        plt.ylabel('1$/1P')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        plt.yticks(np.linspace(min(column), max(column), endpoint=True))
        path = paths.graphics_dir + "/Box&Whiskers" + "/Курс.png"
    elif atribute == 'Цена':
        df = data.dates[['Дата', 'Цена']].copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        df = df[df['Дата'] <= end and df['Дата'] >= start]
        column = df[atribute]
        fig.set_size_inches(10, 10)
        plt.ylabel('Рубли')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        plt.yticks(np.linspace(min(column), max(column), endpoint=True))
        path = paths.graphics_dir + "/Box&Whiskers" + "/Цена.png"
    elif atribute == 'Добыча':
        df = data.main[['Дата', 'Страна', 'Добыча']].copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        df = df[df['Дата'] <= end and df['Дата'] >= start]
        df.groupby(['Страна', 'Дата'])['Добыча'].mean()
        grouped_data = df.groupby(['Страна'])['Добыча'].agg(list)
        fig.set_size_inches(15, 10)
        plt.boxplot(grouped_data, showmeans=True)
        plt.xticks(ticks=range(1, len(grouped_data) + 1), labels=grouped_data.index)
        plt.title('Среднедневная добыча 2006-2022 гг.')
        plt.ylabel('Среднедневная добыча (1000 бар/д)')
        plt.grid(True)
        plt.suptitle('')

        path = paths.graphics_dir + "/Box&Whiskers" + "/Добыча.png"
        
    plt.grid(True)
    plt.title(f'{atribute} {start}-{end} гг.')
    if not os.path.exists(path):
        save_graph(fig, path)
    return fig

def plot_graph(atribute, start=2006, end=2022):
    margins = {                                                                                         
        "left"   : 0.05,
        "bottom" : 0.05,
        "right"  : 0.99,
        "top"    : 0.97  
    }
    fig = plt.figure(figsize=(20,15))
    fig.subplots_adjust(**margins)  
    if (atribute == 'Курс'):
        df = data.dates[['Дата', 'Курс']].copy()
        df['Дата'] = pd.to_datetime(data.dates['Дата'], format="%d.%m.%Y")
        df = df[(df['Дата'].dt.year <= end) & (df['Дата'].dt.year >= start)]
        plt.plot(df['Дата'], df['Курс'], label='Курс рубля')
        path = paths.graphics_dir + "/Графики" + "/Курс.png"
    elif (atribute == 'Цена'):
        df = data.dates[['Дата', 'Цена']].copy()
        df['Дата'] = pd.to_datetime(data.dates['Дата'], format="%d.%m.%Y")
        df = df[(df['Дата'].dt.year <= end) & (df['Дата'].dt.year >= start)]
        plt.plot(df['Дата'], df['Цена'], label='Цена на нефть')
        path = paths.graphics_dir + "/Графики" + "/Цена.png"
    plt.title(f'{atribute} {start}-{end} гг.', fontsize=18)
    plt.xlabel('Дата', fontsize=18)
    plt.ylabel('Рубли', fontsize=18)
    plt.xticks(rotation=0)
    plt.tick_params(axis='both', labelsize=14)
    plt.grid(True)
    
    if not os.path.exists(path):
        save_graph(fig, path)
    return fig
    
def hist(start=2006, end=2022, countries={}):
    df = data.main[['Дата', 'Страна', 'Добыча']].copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
    df = df[(df['Дата'] <= end) & (df['Дата'] >= start)]
    grouped_data = df.groupby(['Страна', 'Дата'], as_index=False)['Добыча'].mean()

    years = data.get_years()

    grouped_data = grouped_data.groupby(['Страна'])['Добыча'].agg(list)

    fig, ax = plt.subplots(2, 3, figsize=(20, 15))
    for i in range(2):
        for j in range(3):
            ax[i, j].hist([prod[(i + 1) * (j + 1)] for prod in grouped_data], alpha=0.7, color='skyblue', edgecolor='black', bins=10)
            ax[i, j].set_title(years[(i + 1) * (j + 1)])
            ax[i, j].yaxis.set_major_locator(MultipleLocator(base = 1))
            ax[i, j].xaxis.set_major_locator(MultipleLocator(base = 500)) 
            ax[i, j].grid(True, axis='y')
            ax[i, j].set_xlabel('Среднедневная добыча')
            ax[i, j].set_ylabel('Частота')
            
    plt.title('Гистограммы среднедневной добычи по годам', fontsize=18)
    plt.tight_layout()
    path = paths.graphics_dir + "/Гистограмма" + "/Добыча.png"
    if not os.path.exists(path):
        save_graph(fig, path)
    return fig

def diag(atribute, start=2006, end=2022, countries={}):
    df = data.main[['Дата', 'Страна', 'Добыча']].copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
    grouped_data = df.groupby(['Страна', 'Дата'], as_index=False)['Добыча'].mean()

    countries = data.get_countries()
    years = data.get_years()
    
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
    path = paths.graphics_dir + "/Диаграмма" + "/Добыча.png"
    if not os.path.exists(path):
        save_graph(fig, path)
    return fig

def plot_scatter(atribute, start=2006, end=2022, countries={}):
    margins = {                                                                                         
        "left"   : 0.06,
        "bottom" : 0.06,
        "right"  : 0.988,
        "top"    : 0.986  
    }
    fig = plt.figure(figsize=(20, 20))
    fig.subplots_adjust(**margins)                            
    price = data.dates['Цена']
    df = data.main[['Страна', 'Добыча']].copy()
    grouped_data = df.groupby('Страна')['Добыча'].agg(list)
    for c, prod in grouped_data.items():
        plt.scatter(price, prod, label=c, s=10)
    plt.title('Категоризированная диаграмма рассеивания:', fontsize=18)
    plt.xlabel('Цена за баррель', fontsize=18)
    plt.ylabel('Добыча дневная (1000 баррелей/день)', fontsize=18)
    plt.legend(title='Название страны')
    plt.tick_params(axis='both', labelsize=14)
    plt.grid(True)
    path = paths.graphics_dir + "/Рассеивание" + "/Все.png"
    if not os.path.exists(path):
        save_graph(fig, path)
    return fig

def save_graph(fig, path):
    print(path)
    fig.savefig(path)