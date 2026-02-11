import os
import sys
from decouple import Config, RepositoryEnv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
env_file = BASE_DIR / ".env"
config = Config(RepositoryEnv(env_file))

ENV_ID = config("BLOG_ENV_ID", default="local")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    f"settings.env.{ENV_ID}"
)

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
