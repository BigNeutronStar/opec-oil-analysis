import pandas as pd
import rating
prod = pd.read_excel('./Work/Data/oil-production_db.xlsx')
date_id = pd.read_excel('./Work/Data/db.xlsx', sheet_name=1)
bd = pd.read_excel('./Work/Data/db_test.xlsx')

dates = list(date_id['Дата'])
price = list(date_id['Цена за баррель $'])
curr = list(date_id['Курс рубля'])
countries = list(prod['Страна'])


dates_count = len(dates)
country_count = len(countries)

bd['date_id'] = list(range(1, dates_count + 1)) * country_count
bd['Дата'] = dates * country_count
bd['Цена за баррель'] = price * country_count
bd['Курс рубля'] = curr * country_count

rating.form()

temp = list()
temp_id = list()
temp_rate = list()
temp_prod = list()
for i in range(country_count):
        temp_id += [i + 1] * dates_count
        temp += [countries[i]] * dates_count
        temp_rate += [rating.get_rating(countries[i])] * dates_count
        temp_prod += [rating.get_production(countries[i])] * dates_count
bd['country_id'] = temp_id
bd['Страна'] = temp
bd['Номер страны по добыче'] = temp_rate
bd['Среднедневная добыча за год (1000 бар/д)'] = temp_prod


bd.to_excel('./Work/Data/db_test.xlsx')
