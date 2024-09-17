import os
import dj_database_url
from .base import *

DEBUG = os.getenv('DEBUG', 'True') == 'True'

INSTALLED_APPS += [
    'storages'
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

# AWS S3 Credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'eu-north-1')

# S3 settings
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Cache files for 1 day
}

# Static files (CSS, JavaScript, images)
AWS_STATIC_LOCATION = 'staticfiles'
STATICFILES_STORAGE = 'devjobs_portal.storages.StaticStorage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'

# Media files (uploads)
AWS_MEDIA_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'devjobs_portal.storages.MediaStorage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'