import os

class Config(object):
    KEY = os.environ.get('KEY') or 'where do your parsnips grow?'
