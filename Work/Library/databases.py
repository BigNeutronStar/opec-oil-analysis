import pandas as pd
import numpy as np

__all__ = ['production', 'price', 'currency', 'dates', 'countries', 'years']

production = price = currency = dates = pd.DataFrame()
countries = years = dates_count = rating = list()

def read(public_paths):
    global production, price, currency, countries, years

    production = pd.read_excel(public_paths['prd'])
    countries = production['Страна']
    years = list(production.head())[1:]
    prds = [list(pd.to_numeric(production.iloc[i], errors='coerce'))[1:] for i in range(len(countries))]
    production = dict(zip(countries, prds))

    price = pd.read_excel(public_paths['price'])
    currency = pd.read_excel(public_paths['curr'])

def form_date(path):
    global dates, dates_count

    dates = pd.to_datetime(price['Дата'], format='%Y-%m-%d')
    dates_count = [(dates.dt.year == year).sum() for year in years]

    currency['Дата'] = pd.to_datetime(currency['Дата'], format='%m.%d.%Y')
    currency.sort_values(by='Дата', inplace=True)
    
    df = pd.DataFrame({
        'Дата' : dates.dt.strftime('%d.%m.%Y'),
        'Цена' : price['Цена'],
        'Курс' : np.array(currency['Курс']),
    })

    df.to_excel(path, index=False)

def form_rating(path, period = [2006, 2022]):
    global rating

    start, end = get_years_id(period)

    sum_prd = [sum(prd[i] for i in range(start, end + 1)) for prd in production.values()]

    total_prod = dict(zip(production.keys(), sum_prd))
    total_prod = dict(sorted(total_prod.items(), key=lambda item: item[1], reverse=True))
    
    rtn = dict(zip(countries, np.zeros((1, len(countries)))))
    rating = rtn.values()

    i = 1
    for c in total_prod.keys():
        rtn[c] = i
        i += 1

    df = pd.DataFrame({
        'Страна' : rtn.keys(),
        'Рейтинг' : rtn.values()
    })

    df.to_excel(path, index=False)
    
def form_dailyproduction(path):
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

    df = pd.DataFrame(data)
    df.to_excel(path, index=False)

def get_years_id(period):
    return (years.index(period[0]), years.index(period[1]))




