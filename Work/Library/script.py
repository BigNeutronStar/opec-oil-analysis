import pandas as pd
prod = pd.read_excel('./Work/Data/oil-production_db.xlsx')
dates = pd.read_excel('./Work/Data/db.xlsx', sheet_name=1)['Дата']
bd = pd.read_excel('./Work/Data/db_test.xlsx')
countries = prod['Страна']
res = []
# f = open('./Work/Data/file.txt', 'w')
for c in countries:
    for i in range(len(dates)):
        # f.write(c)
        # f.write('\n')
        res.append(c)
bd['Страна'] = res
bd.to_excel('./Work/Data/db_test.xlsx')
