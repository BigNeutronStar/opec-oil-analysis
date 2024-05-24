import pandas as pd
import numpy as np

__all__ = ['countires', 'dates']

##daily_production = production = price = currency = dates = total = pd.DataFrame()
##countries = years = dates_count = rating = list()
production = price = currency = pd.DataFrame()

countries = dates = pd.DataFrame()

def read_public(public_paths):
    #global production, dates, price, currency, countries, years
    global production, price, currency
   
    production = pd.read_excel(public_paths['prd'])
    countries = production['Страна']
    prds = (np.array(pd.to_numeric(production.iloc[i], errors='coerce')[1:]) for i in range(countries.size))

    production = pd.DataFrame({
        'Страна':countries,
        'Добыча':prds
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
    
    sum_prd = dict()

    for country, prod in zip(production['Страна'], production['Добыча']):
        sum_prd[country] = round(sum(prod), 3)

    total_prod = dict(zip(production.keys(), sum_prd))
    total_prod = dict(sorted(total_prod.items(), key=lambda item: item[1], reverse=True))
    
    rtn = dict(zip(countries, np.zeros((1, len(countries)))))

    i = 1
    for c in total_prod.keys():
        rtn[c] = i
        i += 1
    
    rating = list(rtn.values())

    countries = pd.DataFrame({
        'country_id': np.arange(1, production['Страна'].size + 1),
        'Страна' : rtn.keys(),
        'Рейтинг' : rtn.values()
    })

    countries.to_excel(path, index=False)
    
def form_dailyproduction(path):
    global daily_production
    data = {
        'Дата' : dates.dt.strftime('%d.%m.%Y')
    }
    for c in countries:
        values = production[c]
        res = []
        for mean, count in zip(values, dates_count):
            randoms = np.round(np.random.normal(mean, 50, count), 1)
            res = np.append(res, randoms)
        data[c] = res
    daily_production = data
    df = pd.DataFrame(data)
    df.to_excel(path, index=False)

def form_total(path):
    global total
    data = pd.DataFrame({
        'date_id' : np.tile(np.arange(dates.size), countries.size),
        'Дата' : np.tile(dates.dt.strftime('%d.%m.%Y'), countries.size),
        'Цена за баррель' : np.tile(price, countries.size),
        'Курс доллара' : np.tile(currency, countries.size),

        'country_id' : np.repeat(np.arange(countries.size) + 1, dates.size),
        'Страна' : np.repeat(countries, dates.size),
        'Номер страны по добыче' : np.repeat(rating, dates.size),
        'Среднедневная добыча за год (1000 бар/д)' : np.array([np.repeat(row, dates_count) for row in production.values()]).ravel(),
        'Добыча (1000 бар)' : np.array([daily_production[c] for c in countries]).ravel(),
    })

    data.to_excel(path, index=False)
    total = data



