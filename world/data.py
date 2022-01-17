import ssl, pandas, numpy
from .models import RegionInfo, CountryInfo, CountryData, CountryTimeseries

url_list = {
    'country_timeseries': "https://covid19.who.int/WHO-COVID-19-global-data.csv",
    'country_current': "https://covid19.who.int/WHO-COVID-19-global-table-data.csv",
    'country_vaccine_data': "https://covid19.who.int/who-data/vaccination-data.csv",
    'vaccine_meta_data': "https://covid19.who.int/who-data/vaccination-metadata.csv"
}


def get_region_info_list():
    initialize_data()
    data_list = RegionInfo.objects.all()
    return data_list


def get_region_info(code):
    initialize_data()
    region_info = RegionInfo.objects.get(code=code)
    return region_info


def get_region_data(code):
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['country_current'])

    gk = df.groupby('Name')
    region_df = gk.get_group(get_region_name_from_code(code))

    data_list = []
    for index, row in region_df.iterrows():
        data_list.append(get_country_model_from_df(region_df, index))
    return data_list


def get_country_info_list():
    initialize_data()
    data_list = CountryInfo.objects.all()
    return data_list


def get_country_info(code):
    initialize_data()
    country_info = CountryInfo.objects.get(code=code)
    return country_info


def get_country_data(code):
    df = pandas.read_csv(url_list['country_current'])
    if code == 'GLOBAL':
        return get_country_model_from_df(df, 'Global')
    return get_country_model_from_df(df, get_country_name_from_code(code))


def get_country_data_list():
    df = pandas.read_csv(url_list['country_current'])
    data_list = []
    for index, row in df.iterrows():
        data_list.append(get_country_model_from_df(df, index))
    return data_list


def get_country_timeseries_data(code, range_type):
    df = pandas.read_csv(url_list['country_timeseries'])

    gk = df.groupby('Country_code')
    country_df = gk.get_group(code)

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
    code = get_country_code_from_name(index)
    total_confirmed = check_if_blank(df.loc[index, 'WHO Region'])
    daily_confirmed = check_if_blank(df.loc[index, 'Cases - newly reported in last 7 days per 100000 population'])
    total_deaths = check_if_blank(df.loc[index, 'Cases - newly reported in last 24 hours'])
    daily_deaths = check_if_blank(df.loc[index, 'Deaths - newly reported in last 7 days per 100000 population'])

    country_data = CountryData(
        code=code,
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


# Number of Countries - 236
# Number of Regions - 7

def initialize_data():
    region_info_list = RegionInfo.objects.all()
    country_info_list = CountryInfo.objects.all()

    if len(country_info_list) != 236 or len(region_info_list) != 7:
        data_df = pandas.read_csv(url_list['country_current'])
        timeseries_df = pandas.read_csv(url_list['country_timeseries'])

        CountryInfo.objects.all().delete()
        country_gk = timeseries_df.groupby('Country_code')

        for code, group in country_gk:
            group_head = group.head(1)
            name = group_head['Country'].values[0]
            region_code = group_head['WHO_region'].values[0]

            country_info = CountryInfo(
                code=code,
                name=name,
                region_code=region_code
            )
            print(f"Adding {code} in Country Data")
            country_info.save()

        RegionInfo.objects.all().delete()
        for index, row in data_df.iterrows():
            country_name = index
            region_name = data_df.loc[index, 'Name']

            country_data = CountryInfo.objects.filter(name=country_name)
            if len(country_data) != 0:
                region_code = country_data[0].region_code

                region_info = RegionInfo(
                    code=region_code,
                    name=region_name
                )
                print(f"Adding {region_code} in Country Data")
                region_info.save()


def check_if_blank(entry):
    if entry == '' or numpy.isnan(entry):
        entry = '0'
    return entry


def get_region_name_from_code(code):
    initialize_data()
    region_info = RegionInfo.objects.filter(code=code)
    if len(region_info) == 0:
        return ""
    return region_info[0].name


def get_region_code_from_name(name):
    initialize_data()
    region_info = RegionInfo.objects.filter(name=name)
    if len(region_info) == 0:
        return ""
    return region_info[0].code


def get_country_name_from_code(code):
    initialize_data()
    country_info = CountryInfo.objects.filter(code=code)
    if len(country_info) == 0:
        return ""
    return country_info[0].name


def get_country_code_from_name(name):
    initialize_data()
    country_info = CountryInfo.objects.filter(name=name)
    if len(country_info) == 0:
        return ""
    return country_info[0].code
