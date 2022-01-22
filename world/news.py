from newsapi import NewsApiClient
from .models import NewsArticle, GeneralData
import datetime

news_api = NewsApiClient(api_key="a5a55eafdde54c0eb6509599dcb5997a")


def get_top_headlines():
    update_top_headlines()
    headlines = NewsArticle.objects.all().order_by('-published_time')
    return headlines


def update_top_headlines():
    current_info = GeneralData.objects.all()
    if len(current_info) == 0:
        update_news_db()
        info = GeneralData(
            last_updated_time=datetime.datetime.now()
        )
        info.save()
    else:
        current_time = datetime.datetime.now()
        last_time = current_info[0].last_updated_time
        last_time = last_time.replace(tzinfo=None)
        difference = current_time - last_time
        duration_in_s = difference.total_seconds()
        duration_in_h = divmod(duration_in_s, 3600)[0]

        if duration_in_h >= 1:
            update_news_db()
            GeneralData.objects.all().delete()
            info = GeneralData(
                last_updated_time=datetime.datetime.now()
            )
            info.save()


def update_news_db():
    NewsArticle.objects.all().delete()
    news_dict = news_api.get_top_headlines(
        q='covid'
    )

    if news_dict['status'] == "ok":
        for article in news_dict['articles']:
            save_model_from_article(article)
    else:
        print("Error in Getting Headlines")


def save_model_from_article(article):
    news_article = NewsArticle(
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
