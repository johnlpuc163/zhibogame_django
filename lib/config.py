import os


def create_app(env):
    if env == 'local':
        os.environ["DJANGO_SETTINGS_MODULE"] = "zhibogame.settings_local"
    if env == 'prod':
        os.environ["DJANGO_SETTINGS_MODULE"] = "zhibogame.settings_prod"

    import django
    django.setup()
