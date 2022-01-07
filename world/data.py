import ssl, pandas
from .models import CountryData, CountryTimeseries, RegionData

url_list = {
    'country_timeseries': "https://covid19.who.int/WHO-COVID-19-global-data.csv",
    'country_current': "https://covid19.who.int/WHO-COVID-19-global-table-data.csv",
    'country_vaccine_data': "https://covid19.who.int/who-data/vaccination-data.csv",
    'vaccine_meta_data': "https://covid19.who.int/who-data/vaccination-metadata.csv"
}


def get_country_data(name):
    df = pandas.read_csv(url_list['country_current'])
    return get_country_model_from_df(df, name)


def get_country_data_list():
    df = pandas.read_csv(url_list['country_current'])

    data_list = []

    for index, row in df.iterrows():
        if index == 'Global':
            continue
        data_list.append(get_country_model_from_df(df, index))

    return data_list


def get_region_list():
    df = pandas.read_csv(url_list['country_current'])

    region_list = set()

    for index, row in df.iterrows():
        if index == 'Global':
            continue
        region_list.add(RegionData(df.loc[index, 'Name']))

    return list(region_list)


def get_region_wise_data(region):
    df = pandas.read_csv(url_list['country_current'])
    gk = df.groupby('Name')
    region_df = gk.get_group(region)

    index_list = []
    for index, row in region_df.iterrows():
        index_list.append(index)

    data_list = []
    for ind in index_list:
        data_list.append(get_country_model_from_df(region_df, ind))
    return data_list


def get_country_timeseries_data(name, range_type):
    df = pandas.read_csv(url_list['country_timeseries'])

    gk = df.groupby('Country')
    country_df = gk.get_group(name)

    index_list = []
    for index, row in country_df.iterrows():
        index_list.append(index)

    if range_type == 'week':
        index_list = index_list[-7:]
    elif range_type == 'month':
        index_list = index_list[-30:]

    data_list = []
    for ind in index_list:
        data_list.append(get_country_timeseries_model_from_df(country_df, ind))
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


def get_country_timeseries_model_from_df(df, index):
    date = df.loc[index, 'Date_reported']
    total_confirmed = check_if_blank(df.loc[index, 'Cumulative_cases'])
    daily_confirmed = check_if_blank(df.loc[index, 'New_cases'])
    total_deaths = check_if_blank(df.loc[index, 'Cumulative_deaths'])
    daily_deaths = check_if_blank(df.loc[index, 'New_deaths'])

    timeseries_data = CountryTimeseries(
        date=date,
        total_confirmed=total_confirmed,
        daily_confirmed=daily_confirmed,
        total_deaths=total_deaths,
        daily_deaths=daily_deaths
    )

    return timeseries_data


def check_if_blank(str):
    if str == '':
        str = '0'
    return str
