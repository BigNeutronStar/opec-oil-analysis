import pandas as pd

countries = dates = daily_production = main = pd.DataFrame()
years = countries_list = list()

def read_data(databases_paths):
    global years, countries_list, countries, dates, daily_production
    
    countries = pd.read_excel(databases_paths['countries'])
    dates = pd.read_excel(databases_paths['dates'])
    daily_production = pd.read_excel(databases_paths['daily_production'])

    df = dates[['Дата']].copy()
    df['Дата'] = pd.to_datetime(df['Дата'], format='mixed', dayfirst=True).dt.year
    years = df['Дата'].unique()

    countries_list = countries['Страна']

def collect_to_main(path):
    global main
    main = pd.merge(daily_production, dates, on='date_id')
    main = pd.merge(main, countries, on='country_id')
    main.to_excel(path, index=False)
