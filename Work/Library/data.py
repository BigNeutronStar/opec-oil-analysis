import pandas as pd

countries = dates = daily_production = main = pd.DataFrame()

def read_data(databases_paths):
    global countries, dates, daily_production, main
    main = pd.read_excel(databases_paths['main'])
    countries = pd.read_excel(databases_paths['countries'])
    dates = pd.read_excel(databases_paths['dates'])
    daily_production = pd.read_excel(databases_paths['daily_production'])

def collect_to_main(path):
    global main
    main = pd.merge(daily_production, dates, on='date_id')
    main = pd.merge(main, countries, on='country_id')
    main.to_excel(path, index=False)



