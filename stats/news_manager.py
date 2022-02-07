from newsapi import NewsApiClient
from .models import NewsArticle, Properties
import datetime
from .enums import RegionType

news_api = NewsApiClient(api_key="a5a55eafdde54c0eb6509599dcb5997a")


def get_top_headlines(region):
    update_top_headlines(region)
    headlines = NewsArticle.objects.filter(region_type=region.name).order_by('-published_time')
    return headlines


def update_top_headlines(region):
    current_info = Properties.objects.all()
    if len(current_info) == 0:
        update_news_db(region)
        info = Properties()
        info.save()
        update_time(region)

    else:
        current_time = datetime.datetime.now()
        if region == RegionType.GLOBAL:
            last_time = current_info[0].world_news_last_updated_time
            if last_time is None:
                update_news_db(region)
                update_time(region)
                return
        else:
            last_time = current_info[0].india_news_last_updated_time
            if last_time is None:
                update_news_db(region)
                update_time(region)
                return

        last_time = last_time.replace(tzinfo=None)
        difference = current_time - last_time
        duration_in_s = difference.total_seconds()
        duration_in_h = divmod(duration_in_s, 3600)[0]

        if duration_in_h >= 1:
            update_news_db(region)
            update_time(region)


def update_time(region):
    current_properties = Properties.objects.all()
    props = current_properties[0]
    if region == RegionType.GLOBAL:
        props.world_news_last_updated_time = datetime.datetime.now()
    else:
        props.india_news_last_updated_time = datetime.datetime.now()
    props.save()


def update_news_db(region):
    NewsArticle.objects.filter(region_type=region.name).delete()
    if region == RegionType.GLOBAL:
        news_dict = news_api.get_top_headlines(
            q='covid'
        )
    else:
        news_dict = news_api.get_top_headlines(
            q='covid',
            country='in'
        )

    if news_dict['status'] == "ok":
        for article in news_dict['articles']:
            save_model_from_article(article, region)
    else:
        print("Error in Getting Headlines")


def save_model_from_article(article, region):
    news_article = NewsArticle(
        region_type=region.name,
        source_name=check_null(article['source']['name']),
        authors=check_null(article['author']),
        title=check_null(article['title']),
        description=check_null(article['description']),
        news_url=check_null(article['url']),
        news_image_url=check_null(article['urlToImage']),
        published_time=check_null(article['publishedAt']),
        content=check_null(article['content'])
    )
    print(f"New Article - {news_article.title} Added")
    news_article.save()


def check_null(value):
    if not value:
        return ""
    return value
