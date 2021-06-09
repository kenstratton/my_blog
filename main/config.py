import os

# Builds path named 'my_blog' that is through the same path with this module.
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///word_guessing_game.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SECRET_KEY = '\x17\xd4I\x03\xafX\xdf\xfc#g\x8f\x13\x1b\x82c\xc7I\xade\xfb\x8a\xa3\x1eG'