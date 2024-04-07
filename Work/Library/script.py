import pandas as pd
prod = pd.read_excel('./Work/Data/oil-production_db.xlsx')
date_id = pd.read_excel('./Work/Data/db.xlsx', sheet_name=1)
bd = pd.read_excel('./Work/Data/db_test.xlsx')

dates = list(pd.to_datetime(date_id['Дата'], format='%m.%d.%Y'))
price = list(date_id['Цена за баррель'])
curr = list(date_id['Курс рубля'])
countries = list(prod['Страна'])


dates_count = len(dates)
country_count = len(countries)

bd['date_id'] = list(range(dates_count)) * country_count
bd['Дата'] = dates * country_count
bd['Цена за баррель'] = price * country_count
bd['Курс рубля'] = curr * country_count

temp = list()
temp_id = list()
for c, i in countries:
        temp_id += [i] * dates_count
        temp += [c] * dates_count
bd['country_id'] = temp_id
bd['Страна'] = temp

# bd['Номер страны по добыче'] = []
# bd['Среднедневная добыча за год (1000 бар/д)'] = []


bd.to_excel('./Work/Data/db_test.xlsx')
