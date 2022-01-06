import pandas as pd
from .models import OverallData

url_list = {
    'india_timeseries': "https://api.covid19tracker.in/data/csv/latest/case_time_series.csv"
}


def get_timeseries_data(range_type):
    df = pd.read_csv(url_list['india_timeseries'])
    timeseries_data = []

    end = len(df)

    start = 0
    if range_type == 'week':
        start = end - 7
    elif range_type == 'month':
        start = end - 30

    for row in range(start, end):
        timeseries_data.append(get_model_from_df(df, row))
    return timeseries_data


def get_current_data():
    df = pd.read_csv(url_list['india_timeseries'])
    ind = len(df) - 1
    return get_model_from_df(df, ind)


def check_if_blank(str):
    if str == '':
        str = '0'
    return str


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
