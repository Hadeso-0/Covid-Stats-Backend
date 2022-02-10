import pandas as pd
from .models import CovidStats
import numpy
import ssl
from .enums import RegionType

url_list = {
    'india_timeseries': "https://api.covid19tracker.in/data/csv/latest/case_time_series.csv"
}


def get_overall_data():
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv(url_list['india_timeseries'])
    ind = len(df) - 1
    data = get_model_from_df(df, ind)
    if data.daily_confirmed == 0:
        return get_model_from_df(df, ind - 1)
    return data


def get_timeseries_data():
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv(url_list['india_timeseries'])

    start = 0
    end = len(df)

    timeseries_data = []
    for row in range(start, end):
        timeseries_data.append(get_model_from_df(df, row))

    if timeseries_data[-1].daily_confirmed == 0:
        timeseries_data.pop()

    return timeseries_data


def get_model_from_df(df, row):
    date_of_stat = df.loc[row, 'Date_YMD']
    total_confirmed = int(check_if_blank(df.loc[row, 'Total Confirmed']))
    total_recovered = int(check_if_blank(df.loc[row, 'Total Recovered']))
    total_deceased = int(check_if_blank(df.loc[row, 'Total Deceased']))
    daily_confirmed = int(check_if_blank(df.loc[row, 'Daily Confirmed']))
    daily_recovered = int(check_if_blank(df.loc[row, 'Daily Recovered']))
    daily_deceased = int(check_if_blank(df.loc[row, 'Daily Deceased']))

    total_active = total_confirmed - (total_recovered + total_deceased)
    daily_active = daily_confirmed - (daily_recovered + daily_deceased)

    region_type = RegionType.INDIA.name

    data_entry = CovidStats(
        region_type=region_type,
        date_of_stat=date_of_stat,
        total_confirmed=total_confirmed,
        daily_confirmed=daily_confirmed,
        total_recovered=total_recovered,
        daily_recovered=daily_recovered,
        total_deceased=total_deceased,
        daily_deceased=daily_deceased,
        total_active=total_active,
        daily_active=daily_active
    )

    return data_entry


def check_if_blank(str_entry):
    if str_entry == '' or numpy.isnan(str_entry):
        str_entry = '0'
    return str_entry
