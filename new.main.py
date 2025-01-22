import telebot
import time
from telebot import types

# Инициализация бота
API_TOKEN = '7914731438:AAFAsVPuuHL_nvoCKzB6d-CFCjwZatHeL0o'  # Замените на ваш токен бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик загрузки видео, документов и аудио
@bot.message_handler(content_types=['video', 'document', 'audio', 'photo'])
def handle_files(message):
    if message.video:
        file_id = message.video.file_id
        file_type = "Video"
    elif message.document:
        file_id = message.document.file_id
        file_type = "Document"
    elif message.audio:
        file_id = message.audio.file_id
        file_type = "Audio"
    elif message.photo:
        file_id = message.photo[-1].file_id  # Берем самое высокое качество изображения
        file_type = "Photo"

    # Отправляем сообщение с file_id пользователю
    bot.reply_to(message, f"{file_type} file_id: {file_id}")

# Обработчик команды /send_video для теста отправки видео
@bot.message_handler(commands=['send_video'])
def send_video(message):
    video_file_id = 'ВАШ_АКТУАЛЬНЫЙ_VIDEO_FILE_ID'  # Замените на полученный file_id
    bot.send_video(message.chat.id, video_file_id, caption="Вот ваше видео!")

# Обработчик команды /send_photo для теста отправки изображения
@bot.message_handler(commands=['send_photo'])
def send_photo(message):
    photo_file_id = 'ВАШ_АКТУАЛЬНЫЙ_PHOTO_FILE_ID'  # Замените на полученный file_id
    bot.send_photo(message.chat.id, photo=photo_file_id, caption="Вот ваше изображение")


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправьте мне видео, документ или аудио, и я верну вам их file_id.")

# Функция для запуска бота с обработкой ошибок и автоперезапуском
def start_bot():
    while True:
        try:
            print("Бот запущен...")
            bot.polling(none_stop=True, interval=2, timeout=10)
        except Exception as e:
            print(f"Ошибка: {e}. Перезапуск через 5 секунд...")
            time.sleep(5)

# Запуск бота
if __name__ == "__main__":
    start_bot()

