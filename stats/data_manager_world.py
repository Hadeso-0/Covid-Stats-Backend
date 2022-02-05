import ssl, pandas, numpy
from .models import WhoRegionInfo, CountryInfo, CovidStats
from . import enums

url_list = {
    'country_timeseries': "https://covid19.who.int/WHO-COVID-19-global-data.csv",
    'country_current': "https://covid19.who.int/WHO-COVID-19-global-table-data.csv"
}


def get_global_data():
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pandas.read_csv(url_list['country_current'])
    return get_country_model_from_df(df, 'Global')


def get_region_info_list():
    initialize_data()
    data_list = WhoRegionInfo.objects.all()
    return data_list


def get_region_info(code):
    initialize_data()
    region_info = WhoRegionInfo.objects.get(region_code_who=code)
    return region_info


def get_region_data_list():
    data_list = []
    region_list = WhoRegionInfo.objects.all()
    for regionInfo in region_list:
        data_list.append(get_region_data(regionInfo.region_code_who))
    return data_list


def get_region_data(code):
    region_type = enums.RegionType.WHO_REGION.name
    region_name = get_region_name_from_code(code)

    countries_list = get_region_country_data_list(code)
    total_confirmed = 0
    daily_confirmed = 0
    total_deceased = 0
    daily_deceased = 0

    for country_data in countries_list:
        total_confirmed = total_confirmed + country_data.total_confirmed
        daily_confirmed = daily_confirmed + country_data.daily_confirmed
        total_deceased = total_deceased + country_data.total_deceased
        daily_deceased = daily_deceased + country_data.daily_deceased

    region_data = CovidStats(
        region_type=region_type,
        region_code_who=code,
        region_name_who=region_name,
        total_confirmed=total_confirmed,
        daily_confirmed=daily_confirmed,
        total_deceased=total_deceased,
        daily_deceased=daily_deceased
    )

    return region_data


def get_region_country_data_list(code):
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
    country_info = CountryInfo.objects.get(country_code=code)
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


def get_country_timeseries_data(code):
    df = pandas.read_csv(url_list['country_timeseries'])

    gk = df.groupby('Country_code')
    country_df = gk.get_group(code)

    data_list = []
    for index, row in country_df.iterrows():
        data_list.append(get_country_timeseries_model_from_df(country_df, index))

    return data_list


def get_country_model_from_df(df, index):
    if index == "Global":
        region_type = enums.RegionType.GLOBAL.name
        region_code_who = ""
        region_name_who = ""
        country_code = ""
        country_name = ""
    else:
        region_type = enums.RegionType.COUNTRY.name
        region_name_who = df.loc[index, 'Name']
        region_code_who = get_region_code_from_name(region_name_who)
        country_code = get_country_code_from_name(index)
        country_name = index

    total_confirmed = check_if_blank(df.loc[index, 'WHO Region'])
    daily_confirmed = check_if_blank(df.loc[index, 'Cases - newly reported in last 7 days per 100000 population'])
    total_deaths = check_if_blank(df.loc[index, 'Cases - newly reported in last 24 hours'])
    daily_deaths = check_if_blank(df.loc[index, 'Deaths - newly reported in last 7 days per 100000 population'])

    country_data = CovidStats(
        region_type=region_type,
        region_code_who=region_code_who,
        region_name_who=region_name_who,
        country_code=country_code,
        country_name=country_name,
        total_confirmed=total_confirmed,
        daily_confirmed=daily_confirmed,
        total_deceased=total_deaths,
        daily_deceased=daily_deaths
    )

    return country_data


def get_country_timeseries_model_from_df(df, index):
    region_type = enums.RegionType.COUNTRY.name
    region_code_who = df.loc[index, 'WHO_region']
    region_name_who = get_region_name_from_code(region_code_who)
    country_code = df.loc[index, 'Country_code']
    country_name = df.loc[index, 'Country']
    date = df.loc[index, 'Date_reported']
    total_confirmed = check_if_blank(df.loc[index, 'Cumulative_cases'])
    daily_confirmed = check_if_blank(df.loc[index, 'New_cases'])
    total_deaths = check_if_blank(df.loc[index, 'Cumulative_deaths'])
    daily_deaths = check_if_blank(df.loc[index, 'New_deaths'])

    timeseries_data = CovidStats(
        region_type=region_type,
        region_code_who=region_code_who,
        region_name_who=region_name_who,
        country_code=country_code,
        country_name=country_name,
        date_of_stat=date,
        total_confirmed=total_confirmed,
        daily_confirmed=daily_confirmed,
        total_deceased=total_deaths,
        daily_deceased=daily_deaths
    )

    return timeseries_data


# Number of Countries - 236
# Number of Regions - 7

def initialize_data():
    region_info_list = WhoRegionInfo.objects.all()
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
                country_code=code,
                country_name=name,
                region_code_who=region_code
            )
            print(f"Adding {code} in Country Data")
            country_info.save()

        WhoRegionInfo.objects.all().delete()
        for index, row in data_df.iterrows():
            country_name = index
            region_name = data_df.loc[index, 'Name']

            country_data = CountryInfo.objects.filter(country_name=country_name)
            if len(country_data) != 0:
                region_code = country_data[0].region_code_who

                region_info = WhoRegionInfo(
                    region_code_who=region_code,
                    region_name_who=region_name
                )
                print(f"Adding {region_code} in Country Data")
                region_info.save()

        country_list = CountryInfo.objects.all()
        for country in country_list:
            country.region_name_who = get_region_name_from_code(country.region_code_who)
            country.save()


def check_if_blank(entry):
    if entry == '' or numpy.isnan(entry):
        entry = '0'
    return entry


def get_region_name_from_code(code):
    initialize_data()
    region_info = WhoRegionInfo.objects.filter(region_code_who=code)
    if len(region_info) == 0:
        return ""
    return region_info[0].region_name_who


def get_region_code_from_name(name):
    initialize_data()
    region_info = WhoRegionInfo.objects.filter(region_name_who=name)
    if len(region_info) == 0:
        return ""
    return region_info[0].region_code_who


def get_country_name_from_code(code):
    initialize_data()
    country_info = CountryInfo.objects.filter(country_code=code)
    if len(country_info) == 0:
        return ""
    return country_info[0].country_name


def get_country_code_from_name(name):
    initialize_data()
    country_info = CountryInfo.objects.filter(country_name=name)
    if len(country_info) == 0:
        return ""
    return country_info[0].country_code
