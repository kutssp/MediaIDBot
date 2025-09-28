<p align="center">
  <img src="assets/file_id.png" alt="MediaIDBot Logo" width="200"/>
</p>

## 📌 MediaIDBot

**MediaIDBot** — это простой Telegram-бот для получения уникальных идентификаторов (`file_id`) медиафайлов, отправленных в чат.  
Поддерживаются все основные типы файлов: видео, документы, фото, аудио и голосовые сообщения.

---

## 🚀 Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/kutssp/MediaIDBot.git
   cd MediaIDBot
```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Получите токен у [BotFather](https://t.me/botfather) и укажите его в коде вместо `YOUR_BOT_TOKEN`.

---

## ▶️ Запуск

Запустите бота командой:

```bash
python main.py
```

После этого найдите своего бота в Telegram и отправьте ему медиафайл.
Бот вернёт вам `file_id`.

---

## 📂 Поддерживаемые форматы

* 🎥 **Видео** — `file_id` для загруженных видео
* 📄 **Документы** — `file_id` для файлов любого типа
* 🖼 **Фото** — `file_id` фото с наибольшим разрешением
* 🎵 **Аудио** — `file_id` музыкальных файлов
* 🎙 **Голосовые сообщения** — `file_id` voice-заметок

---

## 💡 Пример ответа

После отправки файла бот вернёт что-то вроде:

```
Video file_id: ABC123XYZ
Document file_id: DEF456UVW
Photo file_id: GHI789RST
Audio file_id: JKL012MNO
Voice file_id: PQR345JKL
```

---

## 📜 Лицензия

Проект распространяется под лицензией [MIT](LICENSE).

---

## 📬 Контакты

Если у вас есть вопросы или предложения:
[Telegram — @kutssp](https://t.me/kutssp)

```
```
