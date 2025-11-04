import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота - УДАЛИТЕ ЭТОТ ТОКЕН ИЗ СООБЩЕНИЯ!
TOKEN = "8550146768:AAHfgRi2WhEHeUBvXC-nJMlHLMqB47GheEc"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📦 Каталог", callback_data='catalog')],
        [InlineKeyboardButton("💬 Поддержка", callback_data='support')]
    ]
    update.message.reply_text(
        '🛍️ Добро пожаловать в магазин!\n\n'
        'Выберите раздел:',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def catalog(update: Update, context: CallbackContext):
    query = update.callback_query
    products = [
        {"id": 1, "name": "📱 iPhone 13", "price": "1000 руб"},
        {"id": 2, "name": "💻 MacBook Air", "price": "2000 руб"}
    ]
    
    keyboard = []
    for product in products:
        keyboard.append([InlineKeyboardButton(
            f"{product['name']} - {product['price']}", 
            callback_data=f"product_{product['id']}"
        )])
    
    query.edit_message_text(
        "🏪 Наш каталог:\nВыберите товар:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    
    if data == 'catalog':
        catalog(update, context)
    elif data == 'support':
        query.edit_message_text("📞 Напишите нам: @your_support")
    elif data.startswith('product_'):
        product_id = data.split('_')[1]
        query.edit_message_text(f"✅ Товар {product_id} добавлен в заказ!\nМенеджер свяжется с вами.")

def main():
    if not TOKEN:
        logger.error("TELEGRAM_TOKEN не установлен!")
        return
    
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    
    # Простой запуск через поллинг (стабильнее)
    try:
        logger.info("Запускаем бота через поллинг...")
        updater.start_polling()
        logger.info("✅ Бот успешно запущен!")
    except Exception as e:
        logger.error(f"❌ Ошибка запуска: {e}")
    
    updater.idle()

if __name__ == '__main__':
    main()
