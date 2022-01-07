import pandas
from .models import StateData, StateTimeseriesData
import ssl

url_list = {
    'state_timeseries': "https://api.covid19tracker.in/data/csv/latest/states.csv",
    'state_current': "https://api.covid19tracker.in/data/csv/latest/state_wise.csv"
}


def get_all_state_data():
    df = pandas.read_csv(url_list['state_current'])

    data_list = []
    for index in range(len(df)):
        data_list.append(get_state_model_from_df(df, index))

    return data_list


def get_individual_state_date(state):
    df = pandas.read_csv(url_list['state_current'])

    gk = df.groupby('state')
    state_df = gk.get_group(state)

    for row, index in state_df.iterrows():
        return get_state_model_from_df(state_df, row)


def get_timeseries(state, range_type):
    df = pandas.read_csv(url_list['state_timeseries'])

    gk = df.groupby('state')
    state_df = gk.get_group(state)

    index_list = []
    for index, row in state_df.iterrows():
        index_list.append(index)

    if range_type == 'week':
        index_list = index_list[-7:]
    elif range_type == 'month':
        index_list = index_list[-30:]

    data_list = []

    for ind in index_list:
        data_list.append(get_state_timeseries_from_df(state_df, ind))

    return data_list


def get_state_model_from_df(df, index):
    name = df.loc[index, 'state']
    confirmed = check_if_blank(df.loc[index, 'confirmed'])
    recovered = check_if_blank(df.loc[index, 'recovered'])
    deceased = check_if_blank(df.loc[index, 'deceased'])
    active = check_if_blank(df.loc[index, 'active'])
    last_updated = df.loc[index, 'Last Updated']

    data_entry = StateData(
        name=name,
        confirmed=confirmed,
        recovered=recovered,
        deceased=deceased,
        active=active,
        last_updated=last_updated
    )

    return data_entry


def get_state_timeseries_from_df(df, index):
    date = df.loc[index, 'Date']
    confirmed = check_if_blank(df.loc[index, 'Confirmed'])
    recovered = check_if_blank(df.loc[index, 'Recovered'])
    deceased = check_if_blank(df.loc[index, 'Deceased'])
    active = int(confirmed) - (int(recovered) + int(deceased))

    data_entry = StateTimeseriesData(
        date=date,
        confirmed=confirmed,
        recovered=recovered,
        deceased=deceased,
        active=active
    )

    return data_entry


def check_if_blank(str):
    if str == '':
        str = '0'
    return str
