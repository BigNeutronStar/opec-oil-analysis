import pandas as pd 
bd = pd.read_excel('./Work/Data/oil-production_db.xlsx')
prod = dict()
rating = dict()
countries = bd['Страна']

def form(prod = prod, rating = rating):
    for i in range(len(countries)):
        row = bd.iloc[i]
        sum = round(pd.to_numeric(row, errors='coerce').sum(), 3)
        prod[countries[i]] = sum
        rating[countries[i]] = 0

    prod = dict(sorted(prod.items(), key=lambda item: item[1], reverse=True))

    i = 1
    for c in prod.keys():
        rating[c] = i
        i += 1

def get_rating(country: str):
    return rating[country]

def get_production(country: str):
    return prod[country]

