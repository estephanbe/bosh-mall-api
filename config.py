import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect DB
SQLALCHEMY_DATABASE_URI = 'postgres://tqxpnqkcoldjij:aa3e0864f28b3ecf8b5969b9a56b9dcd9187e2d1c7144637a51c445583819d93@ec2-54-211-77-238.compute-1.amazonaws.com:5432/dfo0orcohh03fi'
SQLALCHEMY_TRACK_MODIFICATIONS = False
