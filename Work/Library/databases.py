import pandas as pd
import numpy as np
from openpyxl import Workbook

from .production_generator import generate_dailyproduction
from .rate_countries import form

prod_path="Work/Data/oil-production_db.xlsx"
price_path="Work/Data/oil-price_db.xlsx"
curr_path="Work/Data/currency-pair_db.xlsx"

path="Work/Data/db_test.xlsx"
date_path="Work/Data/date_db.xlsx"
rating_path="Work/Data/rating_db.xlsx"
daily_path="Work/Data/daily-production_db.xlsx"

Workbook().save(path)

production = pd.read_excel(prod_path)
price = pd.read_excel(price_path)
bd = pd.read_excel(path)

productions = form(production, rating_path)
rating = pd.read_excel(rating_path)

dates = date['Дата']
price = date['Цена за баррель']
currency = date['Курс рубля']
countries = np.array(production['Страна'])
ratings = np.array(rating['Рейтинг'])

years = list(production.head())[1:]
dates_count = [(dates.dt.year == year).sum() for year in years]

generate_dailyproduction(countries, dates, productions, dates_count, daily_path)
daily_production = pd.read_excel(daily_path)



