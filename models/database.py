from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# builds path named 'my_blog' that is through the same path with this module.
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'my_blog.db')
# builds database with the path defined above.
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
# An instance for connecting database
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
# Creates a base object and insert info of database into it
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.classes
    Base.metadata.create_all(bind=engine)