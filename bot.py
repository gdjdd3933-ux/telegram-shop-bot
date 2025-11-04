import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔐 Ваш API-ключ бота
TOKEN = "8550146768:AAHfgRi2WhEHeUBvXC-nJMlHLMqB47GheEc"

async def start(update: Update, context):
    """Обработчик команды /start"""
    try:
        welcome_text = (
            '🌟 **Добро пожаловать в StarsShop!** 🌟\n\n'
            '✨ *Мы предлагаем:*\n'
            '• Telegram Stars ⭐\n' 
            '• Telegram Premium 👑\n'
            '• NFT коллекции 🎨\n'
            '• TON Coin 💎\n\n'
            '🚀 **Доступные команды:**\n'
            '/catalog - 📦 Посмотреть каталог\n'
            '/stars - ⭐ Купить Stars\n'
            '/premium - 👑 Купить Premium\n'
            '/support - 📞 Поддержка'
        )
        await update.message.reply_text(welcome_text)
        logger.info("Команда /start выполнена успешно")
    except Exception as e:
        logger.error(f"Ошибка в start: {e}")
        await update.message.reply_text('Привет! Добро пожаловать в StarsShop! 🎉')

async def catalog(update: Update, context):
    """Показывает каталог товаров"""
    try:
        catalog_text = (
            '🏪 **Наш каталог:**\n\n'
            '⭐ **Telegram Stars:**\n'
            '• 100 Stars - 500 руб\n'
            '• 500 Stars - 2000 руб\n'
            '• 1000 Stars - 3500 руб\n'
            '• 5000 Stars - 15000 руб\n\n'
            '👑 **Telegram Premium:**\n'
            '• 1 месяц - 500 руб\n'
            '• 3 месяца - 1200 руб\n'
            '• 12 месяцев - 3500 руб\n\n'
            '💎 **TON Coin:**\n'
            '• 100 TON - 10000 руб\n'
            '• 500 TON - 45000 руб\n\n'
            '📞 Для заказа: @manager_account'
        )
        await update.message.reply_text(catalog_text)
    except Exception as e:
        logger.error(f"Ошибка в catalog: {e}")
        await update.message.reply_text('Вот наш каталог! 📦')

async def stars(update: Update, context):
    """Покупка Stars"""
    try:
        stars_text = (
            '⭐ **Покупка Telegram Stars:**\n\n'
            'Stars - это внутренняя валюта Telegram для покупки цифровых товаров!\n\n'
            '💰 **Пакеты Stars:**\n'
            '✨ 100 Stars - 500 руб\n'
            '✨ 500 Stars - 2000 руб\n'
            '✨ 1000 Stars - 3500 руб\n'
            '✨ 5000 Stars - 15000 руб\n\n'
            '⚡ **Преимущества:**\n'
            '✅ Мгновенная доставка\n'
            '✅ Официальные Stars\n'
            '✅ Поддержка 24/7\n\n'
            '🛒 Для покупки: @stars_manager'
        )
        await update.message.reply_text(stars_text)
    except Exception as e:
        logger.error(f"Ошибка в stars: {e}")
        await update.message.reply_text('Информация о Stars ⭐')

async def premium(update: Update, context):
    """Покупка Premium"""
    try:
        premium_text = (
            '👑 **Telegram Premium:**\n\n'
            'Получите премиум возможности Telegram!\n\n'
            '🎁 **Что входит:**\n'
            '• Увеличенные лимиты\n'
            '• Эксклюзивные стикеры\n'
            '• Быстрые загрузки\n'
            '• Премиум значек\n\n'
            '💳 **Тарифы:**\n'
            '👑 1 месяц - 500 руб\n'
            '👑 3 месяца - 1200 руб\n'
            '👑 12 месяцев - 3500 руб\n\n'
            '📞 Для активации: @premium_manager'
        )
        await update.message.reply_text(premium_text)
    except Exception as e:
        logger.error(f"Ошибка в premium: {e}")
        await update.message.reply_text('Информация о Premium 👑')

async def support(update: Update, context):
    """Связь с поддержкой"""
    try:
        support_text = (
            '📞 **Служба поддержки StarsShop:**\n\n'
            '👨‍💼 Менеджеры:\n'
            '@stars_manager - Stars\n'
            '@premium_manager - Premium\n'
            '@crypto_manager - TON\n\n'
            '⏰ Работаем 24/7\n'
            '⚡ Ответ за 5-15 минут\n\n'
            '🌟 Мы всегда на связи!'
        )
        await update.message.reply_text(support_text)
    except Exception as e:
        logger.error(f"Ошибка в support: {e}")
        await update.message.reply_text('Напишите @manager_account')

async def handle_message(update: Update, context):
    """Обработка обычных сообщений"""
    try:
        await update.message.reply_text(
            'Используйте команды:\n'
            '/start - начало работы\n'
            '/catalog - каталог\n'
            '/stars - купить Stars\n'
            '/premium - купить Premium\n'
            '/support - поддержка'
        )
    except Exception as e:
        logger.error(f"Ошибка в handle_message: {e}")

def main():
    """Основная функция"""
    try:
        logger.info("Запуск бота StarsShop...")
        
        # Создаем приложение
        application = Application.builder().token(TOKEN).build()
        
        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("catalog", catalog))
        application.add_handler(CommandHandler("stars", stars))
        application.add_handler(CommandHandler("premium", premium))
        application.add_handler(CommandHandler("support", support))
        
        # Обработка текстовых сообщений
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # Запускаем бота
        logger.info("Бот запускается...")
        application.run_polling()
        logger.info("Бот успешно запущен!")
        
    except Exception as e:
        logger.error(f"Ошибка запуска бота: {e}")

if __name__ == '__main__':
    main()
