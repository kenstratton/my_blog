if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "tests"

from main.models import User, Post
from main import db
from main import key
from hashlib import sha256
import random, string

# Creates a name with random strings.
def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def run_db_test():
    success = 0
    # Create instance of User class
    try:
        user_name = randomname(6)
        password = '111111'
        hashed_password = sha256((user_name + password + key.SALT).encode('utf-8')).hexdigest()
        user = User(user_name, hashed_password)
        print(user,'\n',user.name,'\n',user.hashed_password,'\n')
        success += 1
    except Exception as e:
        print(e)

    # Insert User instance into database
    try:
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(name=user_name).first()
        print(user,'\n',user.name,'\n',user.hashed_password,'\n')
        success += 1
    except Exception as e:
        print(e)

    # Use class method of User class
    try:
        print(user.repr(),'\n')
        success += 1
    except Exception as e:
        print(e)

    # Create instance of Post class
    try:
        title = 'Hello'
        detail = 'World'
        post = Post(user.id, title, detail)
        print(post,'\n',post.title,'\n',post.detail,'\n')
        success += 1
    except Exception as e:
        print(e)

    # Insert User instance into database
    try:
        db.session.add(post)
        db.session.commit()
        post = Post.query.filter_by(user_id=user.id).first()
        print(post,'\n',post.title,'\n',post.detail,'\n')
        success += 1
    except Exception as e:
        print(e)

    # Update info of Post instance
    try:
        post.title = 'Hey'
        post.detail = 'Universe'
        db.session.commit()
        print(post,'\n',post.title,'\n',post.detail,'\n')
        success += 1
    except Exception as e:
        print(e)

    # Delete instance of Post
    try:
        db.session.delete(post)
        db.session.commit()
        post = Post.query.filter_by(user_id=user.id).first()
        print(post,'\n')
        success += 1
    except Exception as e:
        print(e)

    print(str(success) + '/7 completed.')