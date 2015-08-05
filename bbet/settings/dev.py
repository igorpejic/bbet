# Import some utility functions
from os.path import join
# Fetch our common settings
from common import *
import json

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

DB_FILE = normpath(join(PROJECT_ROOT, 'run', 'DB.json'))

with open(DB_FILE) as f:
    data = json.load(f)


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'billboardbet',
        'USER': data['user'],
        'PASSWORD': data['password'],
    }
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS
