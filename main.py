import telebot

# Вставь сюда токен от нового бота
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Обработчик медиафайлов
@bot.message_handler(content_types=['video', 'document', 'photo', 'audio', 'voice'])
def handle_media(message):
    if message.video:
        video_id = message.video.file_id
        bot.send_message(message.chat.id, f"Video file_id: {video_id}")

    if message.document:
        document_id = message.document.file_id
        bot.send_message(message.chat.id, f"Document file_id: {document_id}")

    if message.photo:
        photo_id = message.photo[-1].file_id  # Получаем последнее фото с наибольшим разрешением
        bot.send_message(message.chat.id, f"Photo file_id: {photo_id}")

    if message.audio:
        audio_id = message.audio.file_id
        bot.send_message(message.chat.id, f"Audio file_id: {audio_id}")

    if message.voice:
        voice_id = message.voice.file_id
        bot.send_message(message.chat.id, f"Voice file_id: {voice_id}")

# Запуск бота
if __name__ == '__main__':
    print('Bot started ✅')
    bot.infinity_polling(none_stop=True)