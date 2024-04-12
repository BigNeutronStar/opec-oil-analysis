import pandas as pd
from openpyxl import Workbook

def form(production, rating_path):
    total_prod = dict()
    prod = dict()
    rating = dict()

    countries = production['Страна']
    for i in range(len(countries)):
        row = production.iloc[i]
        prod_list = list(pd.to_numeric(row, errors='coerce'))[1:]
        prod[countries[i]] = prod_list
        total_prod[countries[i]] = round(sum(prod_list), 3)
        rating[countries[i]] = 0

    total_prod = dict(sorted(total_prod.items(), key=lambda item: item[1], reverse=True))

    i = 1
    for c in total_prod.keys():
        rating[c] = i
        i += 1
    
    data = {
        'Страна' : rating.keys(),
        'Рейтинг' : rating.values()
    }
    df = pd.DataFrame(data)
    Workbook().save(rating_path)
    df.to_excel(rating_path, index=False)
    
    return prod

