from .models import AboutApp, Developer, DataSource


def get_about_app():
    about_list = AboutApp.objects.all()
    if len(about_list) == 0:
        return AboutApp()
    return about_list[0]


def get_developer_list():
    developers = Developer.objects.all().order_by('order')
    return developers


def get_source_list():
    sources = DataSource.objects.all()
    return sources
