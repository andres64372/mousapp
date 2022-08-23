from pathlib import Path

import environ

env = environ.Env(
    SECRET_KEY=(str, "sa4a4w8EyMfod7VUcC07A0OGZFQ7LqrMjwJU5qs7izrhYW89pIvdGjCsUV1BWI6GwGCxZuzkE8kpUA3uCckxPA"),
    DATABASE_URL=(str, "sqlite:///database.db")
)

SECRET_KEY = env("SECRET_KEY")
DATABASE_URL = env("DATABASE_URL")