import os
from dotenv import load_dotenv
from yandex_music import Client

load_dotenv()
YA_TOKEN = os.getenv("YA_TOKEN")

ya_client = Client(YA_TOKEN).init()
