import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

clientTelegram: TelegramClient | None = None

async def auth_telegram():
    global clientTelegram
    clientTelegram = TelegramClient(
        "session_name",
        API_ID,
        API_HASH,
        device_model="YandexMusicStatus",
        system_version="YandexMusicStatusTelegram",
        app_version="0.1.0",
        lang_code="ru"
    )
    await clientTelegram.start(
        phone=lambda: input("Введите номер телефона: "),
        password=lambda: input("Введите пароль 2FA: ")
    )
    return clientTelegram
