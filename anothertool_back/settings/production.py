from anothertool_back.settings.base import *
from decouple import config


SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['plabo.pythonanywhere.com',]
