import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    WERKZEUG_DEBUG_PIN = os.environ.get('WERKZEUG_DEBUG_PIN') or 'off'