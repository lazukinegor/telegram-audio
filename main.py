import asyncio
from telegram_client import auth_telegram
from track_manager import handle_current_track
from utils import log

async def main():
    await auth_telegram()
    log("🚀 Запущен мониторинг треков")
    while True:
        await handle_current_track()
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
