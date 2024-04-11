import numpy as np
import pandas as pd 
from openpyxl import Workbook

def generate_databases(countries, dates, productions, dates_count, daily_path):
    data = {
        'Дата' : dates.dt.strftime('%d.%m.%Y')
    }

    for c in countries:
        values = productions[c]
        res = []
        for mean, count in zip(values, dates_count):
            randoms = np.round(np.random.normal(mean, 50, count), 1)
            res = np.append(res, randoms)
        data[c] = res

    df = pd.DataFrame(data)
    Workbook().save(daily_path)
    df.to_excel(daily_path, index=False)
    
        
