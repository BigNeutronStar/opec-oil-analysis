import pandas as pd
prod = pd.read_excel('./Work/Data/oil-production_db.xlsx')
bd = pd.read_excel('./Work/Data/db.xlsx')
dates = bd['Дата']
countries = prod['Страна']
res = []
# f = open('./Work/Data/file.txt', 'w')
for c in countries:
    for i in range(len(dates)):
        # f.write(c)
        # f.write('\n')
        res.append(c)
bd['Страна'] = res
print(list(bd['Страна']))
bd.to_excel('./Work/Data/db_test.xlsx')
