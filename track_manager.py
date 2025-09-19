import os
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1
from telethon import types, functions
from yandex_client import ya_client
from utils import log

last_track = None

os.makedirs("music", exist_ok=True)

async def handle_current_track():
    from telegram_client import clientTelegram
    if clientTelegram is None:
        log("❌ Telegram клиент не авторизован")
        return

    sessions = await MediaManager.request_async()
    if not sessions:
        log("⚠️ Не удалось получить список сессий медиа")
        return

    current_session = sessions.get_current_session()
    if not current_session:
        log("🎧 Музыка сейчас не играет")
        return


    info = await current_session.try_get_media_properties_async()
    if not info:
        log("⚠️ Не удалось получить свойства медиа")
        return

    if not info.title or not info.artist:
        log("⚠️ У текущего медиа нет названия или артиста")
        return



    title, artist = info.title.strip(), info.artist.strip()
    log(f"▶️ Сейчас играет: {title} — {artist}")

    query = f"{title} {artist}"
    search_result = ya_client.search(query)
    if not search_result.tracks or not search_result.tracks.results:
        return

    candidates = [
        t for t in search_result.tracks.results
        if title.lower() in t.title.lower()
           and any(a.name.lower() in artist.lower() for a in t.artists)
    ]
    if not candidates:
        return

    best_match = candidates[0]
    file_path = f"music/{best_match.id}.mp3"

    if not os.path.exists(file_path):
        log(f"⬇️ Скачиваю: {best_match.title}")
        best_match.download(file_path, codec="mp3")
    else:
        log("✅ Уже в кэше")
    
    await send_to_saved(file_path, title, artist)

async def send_to_saved(file_path, title, artist):
    global last_track
    from telegram_client import clientTelegram
    audio = MP3(file_path, ID3=ID3)
    if not audio.tags:
        audio.add_tags()
    audio.tags.add(TIT2(encoding=3, text=title))
    audio.tags.add(TPE1(encoding=3, text=artist))
    audio.save()

    if last_track == file_path:
        log("ℹ️ Этот трек уже в аудиостатусе")
        return
    last_track = file_path
    duration = int(audio.info.length)
    uploaded_file = await clientTelegram.upload_file(file_path)

    media = types.InputMediaUploadedDocument(
        file=uploaded_file,
        mime_type="audio/mpeg",
        attributes=[types.DocumentAttributeAudio(duration=duration)]
    )
    doc = await clientTelegram(functions.messages.UploadMediaRequest(
        peer=types.InputPeerSelf(),
        media=media
    ))
    await clientTelegram(functions.account.SaveMusicRequest(id=doc.document, unsave=False))
    log(f"⭐ Добавлен в аудиостатус: {title} — {artist}")
