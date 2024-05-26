import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd

from Library import paths
from Library import data

def plot_boxwhiskers(atribute):
    fig = plt.figure(figsize=(10,6))
    if atribute == 'Курс':
        column = data.dates[atribute]
        plt.ylabel('1$/1P')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        path = os.path.join(paths.graphics_dir,"Box&Whiskers","Курс.png")
    elif atribute == 'Цена':
        column = data.dates[atribute]
        plt.ylabel('Рубли')
        plt.boxplot(column, showmeans=True)
        plt.xticks([])
        path = os.path.join(paths.graphics_dir,"Box&Whiskers","Цена.png")
    elif atribute == 'Добыча':
        positions = np.arange(2, len(countries) * 2 + 1, 2)

        plt.boxplot(production.values(), showmeans=True, positions=positions)
        plt.title('Среднедневная добыча 2006-2022 гг.')
        plt.xticks(positions, [c for c in countries], rotation = 15)
        plt.ylabel('Среднедневная добыча (1000 бар/д)')
        plt.grid()
        plt.suptitle('')
 
        df = pd.DataFrame(
            dict(
                data.daily_production.groupby('country_id')['Добыча'].apply(list)
            )
        )
        df.boxplot()
        path = os.path.join(paths.graphics_dir,"Box&Whiskers","Добыча.png")
    plt.grid()
    plt.title(f'{atribute} 2006-2022 гг.')
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
    path = os.path.join(paths.graphics_dir,"Графики изменения","Курс.png")
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
    path = os.path.join(paths.graphics_dir,"Графики изменения","Цена.png")
    plt.savefig(path)
    return fig
    
def hist():
    pass

def diag():
    pass

def hui():
    plt.figure(figsize=(10,6))
    positions = np.arange(2, len(countries['Страна'].size) * 2 + 1, 2)

    plt.boxplot(production.values(), showmeans=True, positions=positions)
    plt.title('Среднедневная добыча 2006-2022 гг.')
    plt.xticks(positions, [c for c in countries], rotation = 15)
    plt.ylabel('Среднедневная добыча (1000 бар/д)')
    plt.grid()
    plt.suptitle('')
    plt.show()

    #### Графики измененения цены и курса
   

   

    ####### Кластеризованная столбчатая
    fig = plt.figure(figsize=(30, 6))
    ax = fig.add_subplot()
    ax.set_ylabel('Среднедневная добыча (1000 бар/д)')
    fig.suptitle("Кластеризованная столбчатая диаграмма по среднедневной добыче")
    x = years

    y1 = production["Congo"]
    y2 = production["Iraq"]
    y3 = production["Algeria"]
    y4 = production["Angola"]
    y5 = production["Equatorial Guinea"]
    y6 = production["Gabon"]
    y7 = production["IR Iran"]
    y8 = production["Kuwait"]
    y9 = production["Libya"]
    y10 = production["Nigeria"]
    y12 = production["United Arab Emirates"]
    y13 = production["Venezuela"]
    bar_width = 0.05

    ax.bar([i - 6*bar_width for i in x], y1, width=bar_width, align='center', label="Congo")
    ax.bar([i - 5*bar_width for i in x], y2, width=bar_width, align='center', label="Iraq")
    ax.bar([i - 4*bar_width for i in x], y3, width=bar_width, align='center', label="Algeria")
    ax.bar([i - 3*bar_width for i in x], y4, width=bar_width, align='center', label="Angola")
    ax.bar([i - 2*bar_width for i in x], y5, width=bar_width, align='center', label="Equatorial Guinea")
    ax.bar([i - bar_width for i in x], y6, width=bar_width, align='center', label="Gabon")
    ax.bar([i for i in x], y7, width=bar_width, align='center', label="IR Iran")
    ax.bar([i + bar_width for i in x], y8, width=bar_width, align='center', label="Kuwait")
    ax.bar([i + 2*bar_width for i in x], y9, width=bar_width, align='center', label="Libya")
    ax.bar([i + 3*bar_width for i in x], y10, width=bar_width, align='center', label="Nigeria")
    ax.bar([i + 4*bar_width for i in x], y12, width=bar_width, align='center', label="United Arab Emirates")
    ax.bar([i + 5*bar_width for i in x], y13, width=bar_width, align='center', label="Venezuela")
    ax.set_xticks([i for i in x])
    ax.set_xticklabels(x, rotation=45, ha='right', fontsize=10)
    plt.grid(True, axis='y')
    plt.legend(loc='upper right', bbox_to_anchor=(1.13, 1))
    plt.show()


    ###### Категоризированная гистограмма
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

    ##### Диаграмма рассеивания  (ВСЕ)
    plt.figure(figsize=(10, 8))
    x = price

    for i in countries:
        y = daily_production[i]
        plt.scatter(x, y, label=i, s=1)
        
    plt.title('Категоризированная диаграмма рассеивания:')
    plt.xlabel('Цена за баррель')
    plt.ylabel('Добыча дневная (1000 баррелей/день) ')
    plt.legend(title='название страны')
    plt.grid(True)
    plt.show()

    ##### Диаграмма рассеивания
    x = price

    for i in countries:
        plt.figure(figsize=(10, 8))
        y = daily_production[i]
        plt.scatter(x, y, label=i, s=1)
        
        plt.title('Категоризированная диаграмма рассеивания:')
        plt.xlabel('Цена за баррель')
        plt.ylabel('Добыча дневная (1000 баррелей/день) ')
        plt.legend(title='название страны')
        plt.grid(True)
        plt.show()
