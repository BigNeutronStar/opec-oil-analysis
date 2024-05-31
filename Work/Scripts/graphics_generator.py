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
    fig = plt.figure()
    if atribute == 'Курс':
        column = data.dates[atribute]
        fig.set_size_inches(10, 6)
        plt.ylabel('1$/1P')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        path = paths.graphics_dir + "/Box&Whiskers" + "/Курс.png"
    elif atribute == 'Цена':
        column = data.dates[atribute]
        fig.set_size_inches(10, 6)
        plt.ylabel('Рубли')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        path = paths.graphics_dir + "/Box&Whiskers" + "/Цена.png"
    elif atribute == 'Добыча':
        df = data.main[['Дата', 'Страна', 'Добыча']].copy()
        df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
        df.groupby(['Страна', 'Дата'])['Добыча'].mean()
        grouped_data = df.groupby(['Страна'])['Добыча'].agg(list)
        fig.set_size_inches(20, 12)
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

def plot_course():
    fig = plt.figure(figsize=(10,6))
    plt.plot(pd.to_datetime(data.dates['Дата'], format="%d.%m.%Y"), data.dates['Курс'], label='Курс рубля')
    plt.title('Курс 2006-2022 гг.')
    plt.xlabel('Дата')
    plt.ylabel('Рубли')
    plt.xticks(rotation=0)
    plt.grid(True)
    path = paths.graphics_dir + "/Графики" + "/Курс.png"
    if not os.path.exists(path):
        plt.savefig(path)
    return fig
   

def plot_price():
    fig = plt.figure(figsize=(10,6))
    plt.plot(pd.to_datetime(data.dates['Дата'], format="%d.%m.%Y"), data.dates['Цена'], label='Цена на нефть')
    plt.title('Цена на нефть 2006-2022 гг.')
    plt.xlabel('Дата')
    plt.ylabel('Рубли')
    plt.xticks(rotation=0)
    plt.grid(True)
    path = paths.graphics_dir + "/Графики" + "/Цена.png"
    if not os.path.exists(path):
        plt.savefig(path)
    return fig
    
def hist():
    fig, ax = plt.subplots(2, 3)
    for i in range(2):
        for j in range(3):
            ax[i, j].hist([prod[(i + 1) * (j + 1)] for prod in production.values()], alpha=0.7, color='skyblue', edgecolor='black', bins=10)
            ax[i, j].set_title(years[(i + 1) * (j + 1)])
            ax[i, j].yaxis.set_major_locator(MultipleLocator(base = 1))
            ax[i, j].xaxis.set_major_locator(MultipleLocator(base = 500)) 
            ax[i, j].grid()
            ax[i, j].set_xlabel('Среднедневная добыча')
            ax[i, j].set_ylabel('Частота')
            
    fig.suptitle('Гистограммы среднедневной добычи по годам', fontsize=16)
    plt.tight_layout()
    plt.show()


def diag():
    df = data.main[['Дата', 'Страна', 'Добыча']].copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
    df.groupby(['Страна', 'Дата'])['Добыча'].mean()
    grouped_data = df.groupby(['Страна'])['Добыча'].agg(list)
    years = df['Дата']
    countries = df['Страна']

    fig = plt.figure(figsize=(30, 6))
    ax = fig.add_subplot()
    ax.set_ylabel('Среднедневная добыча (1000 бар/д)')
    fig.suptitle("Кластеризованная столбчатая диаграмма по среднедневной добыче")

    bar_width = 0.05
    k = -6
    for i in range(len(years)):
        for c in countries:
            ax.bar([j + k*bar_width for j in years], grouped_data[c], width=bar_width, align='center', label=c)
            k += 1

    ax.set_xticks([y for y in years])
    ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
    plt.grid(True, axis='y')
    plt.legend(loc='upper right', bbox_to_anchor=(1.13, 1))
    return fig

def plot_scatter():
    fig = plt.figure(figsize=(10, 8))
    price = data.dates['Цена']
    df = data.main[['Страна', 'Добыча']].copy()
    grouped_data = df.groupby('Страна')['Добыча'].agg(list)
    plt.scatter(price, grouped_data['Algeria'], label='Algeria', s=10)
    plt.title('Категоризированная диаграмма рассеивания:')
    plt.xlabel('Цена за баррель')
    plt.ylabel('Добыча дневная (1000 баррелей/день) ')
    plt.legend(title='Название страны')
    plt.grid(True)
    return fig