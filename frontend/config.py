# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = 'y2BH8xD9pyZhDT5qkyZZRgjcJCMHdQ'
    WTF_CSRF_SECRET_KEY = 'VyOyqv5Fm3Hs3qB1AmNeeuvPpdRqTJbTs5wKvWCS'


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False

