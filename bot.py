import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔐 Ваш API-ключ бота
TOKEN = "8550146768:AAHfgRi2WhEHeUBvXC-nJMlHLMqB47GheEc"

async def start(update: Update, context: CallbackContext):
    """Обработчик команды /start"""
    try:
        await update.message.reply_text(
            '🛍️ Добро пожаловать в магазин!\n\n'
            'Используйте команды:\n'
            '/catalog - посмотреть товары\n'
            '/support - связаться с нами\n'
            '/help - помощь'
        )
        logger.info(f"Пользователь {update.effective_user.first_name} запустил бота")
    except Exception as e:
        logger.error(f"Ошибка в start: {e}")

async def catalog(update: Update, context: CallbackContext):
    """Показывает каталог товаров"""
    try:
        catalog_text = (
            '🏪 **Наш каталог:**\n\n'
            '📱 iPhone 13 - 1000 руб\n'
            '💻 MacBook Air - 2000 руб\n'
            '⌚ Apple Watch - 500 руб\n'
            '🎧 AirPods Pro - 300 руб\n\n'
            '💎 **Для заказа напишите:** @manager_account\n'
            '📞 **Или используйте команду:** /support'
        )
        await update.message.reply_text(catalog_text, parse_mode='Markdown')
        logger.info(f"Пользователь {update.effective_user.first_name} запросил каталог")
    except Exception as e:
        logger.error(f"Ошибка в catalog: {e}")

async def support(update: Update, context: CallbackContext):
    """Связь с поддержкой"""
    try:
        support_text = (
            '📞 **Служба поддержки**\n\n'
            '💬 По вопросам заказов: @manager_account\n'
            '🛠 Технические вопросы: @tech_support\n'
            '⏰ Время работы: 10:00 - 20:00\n\n'
            'Мы ответим в течение 15 минут!'
        )
        await update.message.reply_text(support_text, parse_mode='Markdown')
        logger.info(f"Пользователь {update.effective_user.first_name} запросил поддержку")
    except Exception as e:
        logger.error(f"Ошибка в support: {e}")

async def help_command(update: Update, context: CallbackContext):
    """Помощь по командам"""
    try:
        help_text = (
            '❓ **Доступные команды:**\n\n'
            '/start - начать работу\n'
            '/catalog - посмотреть товары\n'
            '/support - связаться с поддержкой\n'
            '/help - эта справка\n\n'
            '🛒 **Как сделать заказ:**\n'
            '1. Посмотрите товары в /catalog\n'
            '2. Напишите нам через /support\n'
            '3. Уточните детали заказа'
        )
        await update.message.reply_text(help_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Ошибка в help: {e}")

def main():
    """Основная функция"""
    try:
        logger.info("Запуск бота...")
        
        # Создаем приложение
        application = Application.builder().token(TOKEN).build()
        
        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("catalog", catalog))
        application.add_handler(CommandHandler("support", support))
        application.add_handler(CommandHandler("help", help_command))
        
        # Запускаем бота
        logger.info("Бот запускается...")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Ошибка запуска бота: {e}")

if __name__ == '__main__':
    main()
