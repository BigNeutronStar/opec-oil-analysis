import pandas as pd
import numpy as np

__all__ = ['countires', 'dates', 'daily_production']

production = price = currency = pd.DataFrame()
years = list()

countries = dates = daily_production = pd.DataFrame()

def read_public(public_paths):
    global production, price, currency, years
   
    production = pd.read_excel(public_paths['prd'])
    years = list(production.head())[1:]
    countries = production['Страна']
    prds = (np.array(pd.to_numeric(production.iloc[i], errors='coerce')[1:]) for i in range(countries.size))

    production = pd.DataFrame({
        'Страна':countries,
        'Добыча':prds,
    })

    price = pd.read_excel(public_paths['price'])
    price['Дата'] = pd.to_datetime(price['Дата'], format='%d.%m.%Y')

    currency = pd.read_excel(public_paths['curr'])

def form_dates(path):
    global dates
    dates = pd.DataFrame({
        'date_id' : np.arange(1, price['Дата'].size + 1),
        'Дата' : price['Дата'].dt.strftime('%d.%m.%Y'),
        'Цена' : price['Цена'],
        'Курс' : currency['Курс']
    })

    dates.to_excel(path, index=False)

def form_countries(path):
    global countries

    countries = pd.DataFrame({
        'country_id': np.arange(1, production['Страна'].size + 1),
        'Страна' : production['Страна'],
    })

    countries.to_excel(path, index=False)
    
def form_dailyproduction(path):
    global daily_production
    time = pd.to_datetime(dates['Дата'], format='%d.%m.%Y')
    data = pd.DataFrame({
        'date_id' : np.tile(dates['date_id'], countries['country_id'].size),
        'country_id' : np.repeat(countries['country_id'], dates['date_id'].size),
    })
    dates_count = [(time.dt.year == year).sum() for year in years]
    column = []
    for id in countries['country_id']:
        values = production.iloc[id-1]['Добыча']
        res = []
        for mean, count in zip(values, dates_count):
            
            randoms = np.round(np.random.normal(mean, 50, count), 1)
            res = np.append(res, randoms)
            
        column = np.append(column, res)
    data['Добыча'] = column
    daily_production = pd.DataFrame(data)
    daily_production.to_excel(path, index=False)

