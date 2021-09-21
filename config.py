import os

from dotenv import load_dotenv


base_dir = os.path.abspath(os.path.dirname(__file__))
instance_dir = os.path.join(base_dir, "instance")
load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "you-will-never-guess"
    JWT_SECRET_KEY = SECRET_KEY
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    ADMINS = ["andromia.software@gmail.com"]
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300
