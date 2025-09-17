# telegram-audio
Большое спасибо @MarshalX (https://github.com/MarshalX/yandex-music-api).


Скрипт, который смотрит через `winsdk.windows.media.control` какой трек играет в системе (Windows), находит его в **Yandex Music API** и добавляет в **аудиостатус Telegram**.

---

## 🚀 Возможности
- Автоматически определяет текущий трек на Windows (Spotify, Яндекс.Музыка, VK Music и др.).
- Ищет песню в каталоге Яндекс.Музыки.
- Сохраняет трек в аудиостатус Telegram.
- Работает в фоне с обновлением статуса.

---

Известные недоработки: 
- Часть треков не может найти. Нужно больше API.
- Когда идет просмотр youtube/rutube/vk видео - пытается так же найти данную аудиозапись по названию видео.

## ⚙️ Установка

```bash
git clone https://github.com/lazukinegor/telegram-audio.git
cd telegram-audio
python -m venv .venv
source .venv\Scripts\activate      # Windows
pip install -r requirements.txt

```
Выставите свои данные в .env.example и переменуйте его в .env.
Получить токены API_ID, API_HASH https://my.telegram.org/apps.
Получить YA_TOKEN https://github.com/MarshalX/yandex-music-api/discussions/513.

**Дорожная карта**
- Добавить новые API
- Исключить видео из поиска
- Ускорить скрипт
- Добавить лог в кеш
- UI
