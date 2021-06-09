import os

# Builds path named 'my_blog' that is through the same path with this module in local environment.
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///my_blog.db'
# Flask-SQLAlchemy tracks data logs.
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Output executed SQL in console logs.
SQLALCHEMY_ECHO = True
# Secret key of application 
SECRET_KEY = '\x17\xd4I\x03\xafX\xdf\xfc#g\x8f\x13\x1b\x82c\xc7I\xade\xfb\x8a\xa3\x1eG'