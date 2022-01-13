import pandas as pd
from .models import OverallData
import ssl, numpy

url_list = {
    'india_timeseries': "https://api.covid19tracker.in/data/csv/latest/case_time_series.csv"
}


def get_current_data():
    #   ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv(url_list['india_timeseries'])
    ind = len(df) - 1
    current_data = get_model_from_df(df, ind)

    if current_data.is_empty():
        return get_model_from_df(df, ind - 1)
    else:
        return current_data


def get_timeseries_data(range_type):
    #   ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv(url_list['india_timeseries'])

    end = len(df)
    if get_model_from_df(df, end-1).is_empty():
        end = end - 1
    start = 0
    if range_type == 'week':
        start = end - 7
    elif range_type == 'month':
        start = end - 30

    timeseries_data = []
    for row in range(start, end):
        timeseries_data.append(get_model_from_df(df, row))
    return timeseries_data


def get_model_from_df(df, row):
    date = df.loc[row, 'Date_YMD']
    total_confirmed = check_if_blank(df.loc[row, 'Total Confirmed'])
    total_recovered = check_if_blank(df.loc[row, 'Total Recovered'])
    total_deceased = check_if_blank(df.loc[row, 'Total Deceased'])
    daily_confirmed = check_if_blank(df.loc[row, 'Daily Confirmed'])
    daily_recovered = check_if_blank(df.loc[row, 'Daily Recovered'])
    daily_deceased = check_if_blank(df.loc[row, 'Daily Deceased'])

    data_entry = OverallData(
        date=date,
        total_confirmed=total_confirmed,
        total_deceased=total_deceased,
        total_recovered=total_recovered,
        daily_confirmed=daily_confirmed,
        daily_recovered=daily_recovered,
        daily_deceased=daily_deceased
    )

    return data_entry


def check_if_blank(str_entry):
    if str_entry == '' or numpy.isnan(str_entry):
        str_entry = '0'
    return str_entry
