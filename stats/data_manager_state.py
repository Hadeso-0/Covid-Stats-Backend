import pandas, ssl
from .models import CovidStats, StateInfo
from .enums import RegionType

url_list = {
    'state_timeseries': "https://data.covid19bharat.org/csv/latest/states.csv",
    'state_current': "https://api.covid19tracker.in/data/csv/latest/state_wise.csv",
    'state_info': "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/csv/states.csv",
    'district_timeseries': "https://data.covid19bharat.org/csv/latest/districts.csv",
    'district_current': "https://data.covid19bharat.org/csv/latest/district_wise.csv"
}


def get_state_info_list():
    initialize_state_info()
    return StateInfo.objects.all()


def get_state_info(code):
    initialize_state_info()
    return StateInfo.objects.get(state_code=code)


def get_all_state_data():
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['state_current'])

    data_list = []
    for index in range(len(df)):
        data_list.append(get_state_model_from_df(df, index))
    return data_list


def get_state_date(code):
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['state_timeseries'])

    gk = df.groupby('State')
    state_df = gk.get_group(get_state_name_from_code(code)).iloc[-3:]

    data_list = []
    for index, row in state_df.iterrows():
        data_list.append(get_state_timeseries_from_df(state_df, index, False))

    for i in range(1, len(data_list)):
        data_list[i].daily_confirmed = data_list[i].total_confirmed - data_list[i - 1].total_confirmed
        data_list[i].daily_recovered = data_list[i].total_recovered - data_list[i - 1].total_recovered
        data_list[i].daily_deceased = data_list[i].total_deceased - data_list[i - 1].total_deceased
        data_list[i].daily_active = data_list[i].total_active - data_list[i - 1].total_active

    current_data = data_list[len(data_list) - 1]
    if current_data.daily_confirmed == 0:
        return data_list[len(data_list) - 2]
    return current_data


def get_state_timeseries(code):
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['state_timeseries'])

    gk = df.groupby('State')
    state_df = gk.get_group(get_state_name_from_code(code))

    data_list = []
    for ind, row in state_df.iterrows():
        data_list.append(get_state_timeseries_from_df(state_df, ind, False))

    size = len(data_list)

    data_list[0].daily_confirmed = data_list[0].total_confirmed
    data_list[0].daily_recovered = data_list[0].total_recovered
    data_list[0].daily_deceased = data_list[0].total_deceased
    data_list[0].daily_active = data_list[0].total_active

    for i in range(1, size):
        data_list[i].daily_confirmed = data_list[i].total_confirmed - data_list[i - 1].total_confirmed
        data_list[i].daily_recovered = data_list[i].total_recovered - data_list[i - 1].total_recovered
        data_list[i].daily_deceased = data_list[i].total_deceased - data_list[i - 1].total_deceased
        data_list[i].daily_active = data_list[i].total_active - data_list[i - 1].total_active

    return data_list


def get_district_data_list(code):
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['district_current'])
    gk = df.groupby('State_Code')

    state_df = gk.get_group(code)

    data_list = []
    for index, row in state_df.iterrows():
        data_list.append(get_district_model_from_df(state_df, index))

    return data_list


def get_district_data(code, name):
    ssl._create_default_https_context = ssl._create_unverified_context
    state_name = get_state_name_from_code(code)

    df = pandas.read_csv(url_list['district_timeseries'])

    gk1 = df.groupby('State')
    state_df = gk1.get_group(state_name)
    gk2 = state_df.groupby('District')
    district_df = gk2.get_group(name).iloc[-2:]

    data_list = []
    for index, row in district_df.iterrows():
        data_list.append(get_state_timeseries_from_df(district_df, index, True))

    size = len(data_list)

    for i in range(1, size):
        data_list[i].daily_confirmed = data_list[i].total_confirmed - data_list[i - 1].total_confirmed
        data_list[i].daily_recovered = data_list[i].total_recovered - data_list[i - 1].total_recovered
        data_list[i].daily_deceased = data_list[i].total_deceased - data_list[i - 1].total_deceased
        data_list[i].daily_active = data_list[i].total_active - data_list[i - 1].total_active

    return data_list[len(data_list) - 1]


def get_district_data_timeseries(code, name):
    state_name = get_state_name_from_code(code)

    df = pandas.read_csv(url_list['district_timeseries'])

    gk1 = df.groupby('State')
    state_df = gk1.get_group(state_name)
    gk2 = state_df.groupby('District')
    district_df = gk2.get_group(name)

    data_list = []
    for index, row in district_df.iterrows():
        data_list.append(get_state_timeseries_from_df(district_df, index, True))

    size = len(data_list)

    data_list[0].daily_confirmed = data_list[0].total_confirmed
    data_list[0].daily_recovered = data_list[0].total_recovered
    data_list[0].daily_deceased = data_list[0].total_deceased
    data_list[0].daily_active = data_list[0].total_active

    for i in range(1, size):
        data_list[i].daily_confirmed = data_list[i].total_confirmed - data_list[i - 1].total_confirmed
        data_list[i].daily_recovered = data_list[i].total_recovered - data_list[i - 1].total_recovered
        data_list[i].daily_deceased = data_list[i].total_deceased - data_list[i - 1].total_deceased
        data_list[i].daily_active = data_list[i].total_active - data_list[i - 1].total_active

    return data_list


def get_state_model_from_df(df, index):
    region_type = RegionType.STATE.name
    name = df.loc[index, 'state']
    code = get_state_code_from_name(name)
    confirmed = check_if_blank(df.loc[index, 'confirmed'])
    recovered = check_if_blank(df.loc[index, 'recovered'])
    deceased = check_if_blank(df.loc[index, 'deceased'])
    active = check_if_blank(df.loc[index, 'active'])

    data_entry = CovidStats(
        region_type=region_type,
        state_code=code,
        state_name=name,
        total_confirmed=confirmed,
        total_recovered=recovered,
        total_deceased=deceased,
        total_active=active
    )

    return data_entry


def get_state_timeseries_from_df(df, index, is_district):
    state_name = df.loc[index, 'State']
    state_code = get_state_code_from_name(state_name)

    if is_district:
        region_type = RegionType.DISTRICT.name
        district_name = df.loc[index, 'District']
    else:
        region_type = RegionType.STATE.name
        district_name = ""

    date_of_stat = df.loc[index, 'Date']

    total_confirmed = check_if_blank(df.loc[index, 'Confirmed'])
    total_recovered = check_if_blank(df.loc[index, 'Recovered'])
    total_deceased = check_if_blank(df.loc[index, 'Deceased'])

    other = check_if_blank(df.loc[index, 'Other'])

    total_active = int(total_confirmed) - (int(total_recovered) + int(total_deceased) + int(other))

    data_entry = CovidStats(
        region_type=region_type,
        state_code=state_code,
        state_name=state_name,
        district_name=district_name,
        date_of_stat=date_of_stat,
        total_confirmed=total_confirmed,
        total_recovered=total_recovered,
        total_deceased=total_deceased,
        total_active=total_active
    )

    return data_entry


def get_district_model_from_df(df, index):
    region_type = RegionType.DISTRICT.name
    name = df.loc[index, 'District']
    state_code = df.loc[index, 'State_Code']
    state_name = df.loc[index, 'State']

    confirmed = check_if_blank(df.loc[index, 'Confirmed'])
    recovered = check_if_blank(df.loc[index, 'Recovered'])
    deceased = check_if_blank(df.loc[index, 'Deceased'])
    active = check_if_blank(df.loc[index, 'Active'])

    data_entry = CovidStats(
        region_type=region_type,
        state_code=state_code,
        state_name=state_name,
        district_name=name,
        total_confirmed=confirmed,
        total_recovered=recovered,
        total_deceased=deceased,
        total_active=active
    )

    return data_entry


def get_state_name_from_code(code):
    initialize_state_info()
    state_info = StateInfo.objects.get(state_code=code)
    return state_info.state_name


def get_state_code_from_name(name):
    initialize_state_info()
    state_info = StateInfo.objects.get(state_name=name)
    return state_info.state_code


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
            state_code=code,
            state_name=ind_df.loc[index, 'name']
        )
        state_info.save()


def check_if_blank(str_entry):
    if str_entry == '' or str_entry is None:
        str_entry = '0'
    return str_entry
