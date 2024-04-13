import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('./Work/Data/db.xlsx', sheet_name=0)
currency_pair = pd.read_excel('./Work/Data/currency-pair_db.xlsx')
oil_price = pd.read_excel('./Work/Data/oil-price_db.xlsx')


####### считывать из generated_data/date_db
currency_pair.boxplot(column='Course', grid=True)
plt.ylabel('1$/1Р')
plt.show()

####### считывать из generated_data/date_db
oil_price.boxplot(column='Price', grid=True)
plt.ylabel('Рубли')
plt.show()



### НЕ ДЕЛАТЬ

# ####### сдеать для средневной добычи по всем годам
# ####### считать дневную добычу из daily production для определенного года указанного и сделать график для нее в указанном году по странам
# df.boxplot(by='Страна', column='Добыча (1000 баррелей)', grid=True)
# plt.suptitle('')
# plt.show()
