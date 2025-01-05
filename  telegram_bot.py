from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Замените токен на токен вашего бота, выданный BotFather
BOT_TOKEN = '7451847396:AAEyGhKl1mXe44vMQvt_F5XcQsQa8H5KsxI'
APP_URL = 'https://mykytaa.github.io/Tapnad/'  # URL вашего приложения

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    # Клавиатура с кнопкой для мини-приложения
    keyboard = [
        [
            InlineKeyboardButton("Играть в Tap Game", web_app={'url': APP_URL}),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    update.message.reply_text(
        "Нажмите кнопку ниже, чтобы начать игру:",
        reply_markup=reply_markup
    )

# Основная функция запуска бота
def main() -> None:
    # Создаем экземпляр Updater
    updater = Updater(BOT_TOKEN)

    # Добавляем обработчик команды /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
