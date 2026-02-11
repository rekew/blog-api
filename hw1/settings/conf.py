from decouple import Config, RepositoryEnv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env_file = BASE_DIR / '.env'
config = Config(RepositoryEnv(env_file))

ENV_ID = config('BLOG_ENV_ID', default='local')

SECRET_KEY = 'django-insecure-azg7x+709gluq^9u#7m6p3$xm%^y39y+yz7&+oyow@#5ow__cb'

DEBUG = True

ALLOWED_HOSTS = config(
    "BLOG_ALLOWED_HOSTS",
    default="",
    cast=lambda v: [s.strip() for s in v.split(",")]
)


DB_NAME = config("BLOG_DB_NAME", default="")
DB_USER = config("BLOG_DB_USER", default="")
DB_PASSWORD = config("BLOG_DB_PASSWORD", default="")
DB_HOST = config("BLOG_DB_HOST", default="")
DB_PORT = config("BLOG_DB_PORT", default="")
