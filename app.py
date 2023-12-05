
from settings.models import *
from django.conf import settings

if __name__ == '__main__' : 
    database_config = settings.DATABASES['sandbox']['NAME']
    print(database_config)
