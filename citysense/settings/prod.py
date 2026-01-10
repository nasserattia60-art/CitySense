from .base import *
import dj_database_url

DEBUG = os.getenv("DEBUG") == "True"
ALLOWED_HOSTS = [
    "citysense.up.railway.app",
    "localhost",
    "127.0.0.1",
]



DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

