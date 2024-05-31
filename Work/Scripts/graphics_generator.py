import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd

from Library import paths
from Library import data

matplotlib.use('agg')

def plot_boxwhiskers(atribute):
    margins = {                                                                                         
        "left"   : 0.06,
        "bottom" : 0.03,
        "right"  : 0.99,
        "top"    : 0.97  
    }
    fig = plt.figure()
    fig.subplots_adjust(**margins)  
    if atribute == 'Курс':
        column = data.dates[atribute]
        fig.set_size_inches(10, 10)
        plt.ylabel('1$/1P')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        plt.yticks(np.linspace(min(column), max(column), endpoint=True))
        path = paths.graphics_dir + "/Box&Whiskers" + "/Курс.png"
    elif atribute == 'Цена':
        column = data.dates[atribute]
        fig.set_size_inches(10, 10)
        plt.ylabel('Рубли')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        plt.yticks(np.linspace(min(column), max(column), endpoint=True))
        path = paths.graphics_dir + "/Box&Whiskers" + "/Цена.png"
    elif atribute == 'Добыча':
        df = data.main[['Дата', 'Страна', 'Добыча']].copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
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
    plt.title(f'{atribute} 2006-2022 гг.')
    if not os.path.exists(path):
        plt.savefig(path)
    return fig

def plot_graph(atribute):
    margins = {                                                                                         
        "left"   : 0.05,
        "bottom" : 0.05,
        "right"  : 0.99,
        "top"    : 0.97  
    }
    fig = plt.figure(figsize=(20,15))
    fig.subplots_adjust(**margins)  
    if (atribute == 'Курс'):
        plt.plot(pd.to_datetime(data.dates['Дата'], format="%d.%m.%Y"), data.dates['Курс'], label='Курс рубля')
        plt.title('Курс 2006-2022 гг.', fontsize=18)
        path = paths.graphics_dir + "/Графики" + "/Курс.png"
    elif (atribute == 'Цена'):
        plt.plot(pd.to_datetime(data.dates['Дата'], format="%d.%m.%Y"), data.dates['Цена'], label='Цена на нефть')
        plt.title('Цена на нефть 2006-2022 гг.', fontsize=18)
        path = paths.graphics_dir + "/Графики" + "/Цена.png"
    plt.xlabel('Дата', fontsize=18)
    plt.ylabel('Рубли', fontsize=18)
    plt.xticks(rotation=0)
    plt.tick_params(axis='both', labelsize=14)
    plt.grid(True)
    
    if not os.path.exists(path):
        plt.savefig(path)
    return fig
    
def hist():
    df = data.main[['Дата', 'Страна', 'Добыча']].copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
    grouped_data = df.groupby(['Страна', 'Дата'], as_index=False)['Добыча'].mean()

    years = grouped_data['Дата'].unique()

    grouped_data = grouped_data.groupby(['Страна'])['Добыча'].agg(list)

    fig, ax = plt.subplots(2, 3, figsize=(20, 15))
    for i in range(2):
        for j in range(3):
            ax[i, j].hist([prod[(i + 1) * (j + 1)] for prod in grouped_data], alpha=0.7, color='skyblue', edgecolor='black', bins=10)
            ax[i, j].set_title(years[(i + 1) * (j + 1)])
            ax[i, j].yaxis.set_major_locator(MultipleLocator(base = 1))
            ax[i, j].xaxis.set_major_locator(MultipleLocator(base = 500)) 
            ax[i, j].grid()
            ax[i, j].set_xlabel('Среднедневная добыча')
            ax[i, j].set_ylabel('Частота')
            
    fig.suptitle('Гистограммы среднедневной добычи по годам', fontsize=16)
    plt.grid(True, axis='y')
    plt.tight_layout()
    return fig

def diag():
    df = data.main[['Дата', 'Страна', 'Добыча']].copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
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
    return fig

def plot_scatter():
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
    plt.scatter(price, grouped_data['Algeria'], label='Algeria', s=10)
    plt.title('Категоризированная диаграмма рассеивания:', fontsize=18)
    plt.xlabel('Цена за баррель', fontsize=18)
    plt.ylabel('Добыча дневная (1000 баррелей/день)', fontsize=18)
    plt.legend(title='Название страны')
    plt.tick_params(axis='both', labelsize=14)
    plt.grid(True)
    return fig