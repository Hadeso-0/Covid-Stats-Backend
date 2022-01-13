import pandas
from .models import StateData, StateTimeseriesData, StateInfo

url_list = {
    'state_timeseries': "https://api.covid19tracker.in/data/csv/latest/states.csv",
    'state_current': "https://api.covid19tracker.in/data/csv/latest/state_wise.csv",
    'state_info': "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/csv/states.csv"
}


def get_state_info_list():
    initialize_state_info()
    return StateInfo.objects.all()


def get_state_info(code):
    initialize_state_info()
    return StateInfo.objects.get(code=code)


def get_all_state_data():
    df = pandas.read_csv(url_list['state_current'])

    data_list = []
    for index in range(len(df)):
        data_list.append(get_state_model_from_df(df, index))
    return data_list


def get_state_date(code):
    df = pandas.read_csv(url_list['state_current'])

    gk = df.groupby('state')
    state_df = gk.get_group(get_state_name_from_code(code))

    for row, index in state_df.iterrows():
        return get_state_model_from_df(state_df, row)


def get_timeseries(code, range_type):
    df = pandas.read_csv(url_list['state_timeseries'])

    gk = df.groupby('state')
    state_df = gk.get_group(get_state_name_from_code(code))

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
        code=get_state_code_from_name(name),
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


def get_state_name_from_code(code):
    initialize_state_info()
    state_info = StateInfo.objects.get(code=code)
    return state_info.name


def get_state_code_from_name(name):
    initialize_state_info()
    state_info = StateInfo.objects.get(name=name)
    return state_info.code


def initialize_state_info():
    state_info_list = StateInfo.objects.all()
    if len(state_info_list) == 36:
        return

    df = pandas.read_csv(url_list['state_info'])
    gk = df.groupby('country_name')
    ind_df = gk.get_group('India')

    count = 0

    for index, row in ind_df.iterrows():
        count = count + 1
        code = ind_df.loc[index, 'state_code']
        print(f"Adding {count} - {code} in DB")
        state_info = StateInfo(
            code=code,
            name=ind_df.loc[index, 'name']
        )
        state_info.save()


def check_if_blank(str_entry):
    if str_entry == '' or str_entry is None:
        str_entry = '0'
    return str_entry
