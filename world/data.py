import ssl, pandas
from .models import CountryData

url_list = {
    'country_timeseries': "https://covid19.who.int/WHO-COVID-19-global-data.csv",
    'country_current': "https://covid19.who.int/WHO-COVID-19-global-table-data.csv",
    'country_vaccine_data': "https://covid19.who.int/who-data/vaccination-data.csv",
    'vaccine_meta_data': "https://covid19.who.int/who-data/vaccination-metadata.csv"
}


def get_country_data(name):
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['country_current'])
    return get_country_model_from_df(df, name)


def get_country_data_list():
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['country_current'])

    data_list = []

    for index, row in df.iterrows():
        if index == 'Global':
            continue
        data_list.append(get_country_model_from_df(df, index))

    return data_list

def get_country_model_from_df(df, index):
    name = index
    if index == 'Global':
        who_region = "GLOBAL"
    else:
        who_region = df.loc[index, 'Name']
    total_confirmed = check_if_blank(df.loc[index, 'WHO Region'])
    daily_confirmed = check_if_blank(df.loc[index, 'Cases - newly reported in last 7 days per 100000 population'])
    total_deaths = check_if_blank(df.loc[index, 'Cases - newly reported in last 24 hours'])
    daily_deaths = check_if_blank(df.loc[index, 'Deaths - newly reported in last 7 days per 100000 population'])

    country_data = CountryData(
        name=name,
        who_region=who_region,
        total_confirmed=total_confirmed,
        daily_confirmed=daily_confirmed,
        total_deaths=total_deaths,
        daily_deaths=daily_deaths
    )

    return country_data


def check_if_blank(str):
    if str == '':
        str = '0'
    return str
