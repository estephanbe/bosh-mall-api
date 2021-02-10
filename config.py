import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect DB
SQLALCHEMY_DATABASE_URI = 'postgres://zsxjshvfglglbo:983edb782a09a4b023ea6c9c3f4ba38decbb998363171c29896d4e9bd895b271@ec2-35-174-118-71.compute-1.amazonaws.com:5432/d3gk75c78t670j'
SQLALCHEMY_TRACK_MODIFICATIONS = False
