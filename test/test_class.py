from models.classes import User, Post
from models.database import db_session
import key
from hashlib import sha256

# Create instance of User class
try:
    user_name = Joseph
    password = '111111'
    hashed_password = sha256((user_name + password + key.SALT).encode('utf-8')).hexdigest()
    user = User(user_name, hashed_password)
except Exception as e:
    print(e)

# # Insert User instance into database
# try:

# except Exception as e:
#     print(e)

# # Use class method of User class
# try:

# except Exception as e:
#     print(e)

# # Create instance of Post class

# # Insert User instance into database
# try:

# except Exception as e:
#     print(e)

# # Update info of Post instance
# try:

# except Exception as e:
#     print(e)

# # Delete instances from database
# try:

# except Exception as e:
#     print(e)