import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔐 Ваш API-ключ бота
TOKEN = "8550146768:AAHfgRi2WhEHeUBvXC-nJMlHLMqB47GheEc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    try:
        welcome_text = (
            '🌟 **Добро пожаловать в CryptoShop!** 🌟\n\n'
            '✨ *Мы предлагаем:*\n'
            '• Криптовалюты 💰\n' 
            '• NFT коллекции 🎨\n'
            '• Цифровые активы 🔮\n'
            '• Эксклюзивные товары 💎\n\n'
            '🚀 **Доступные команды:**\n'
            '/catalog - 📦 Посмотреть каталог\n'
            '/sell_nft - 🎨 Продать NFT\n'
            '/ton - 💎 Купить TON\n'
            '/support - 📞 Поддержка\n'
            '/help - ❓ Помощь\n\n'
            '⚡ *Быстро, безопасно, анонимно!*'
        )
        await update.message.reply_text(welcome_text, parse_mode='Markdown')
        logger.info(f"Пользователь {update.effective_user.first_name} запустил бота")
    except Exception as e:
        logger.error(f"Ошибка в start: {e}")
        await update.message.reply_text('❌ Произошла ошибка. Попробуйте позже.')

async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает каталог товаров"""
    try:
        catalog_text = (
            '🏪 **Наш каталог:**\n\n'
            '💎 **Криптовалюты:**\n'
            '⭐ TON Coin - от 1000 руб\n'
            '⭐ Bitcoin (BTC) - от 50000 руб\n'
            '⭐ Ethereum (ETH) - от 30000 руб\n'
            '⭐ USDT (TRC-20) - от 100 руб\n\n'
            '🎨 **NFT коллекции:**\n'
            '✨ CryptoPunks - от 50000 руб\n'
            '✨ Bored Ape - от 100000 руб\n'
            '✨ Art Blocks - от 20000 руб\n'
            '✨ Rarible - от 5000 руб\n\n'
            '📱 **Готовые продукты:**\n'
            '🚀 Telegram Mini Apps - от 15000 руб\n'
            '🤖 Telegram боты - от 5000 руб\n'
            '💻 Веб-сайты - от 10000 руб\n\n'
            '💫 **Для заказа используйте команды ниже!**'
        )
        await update.message.reply_text(catalog_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Ошибка в catalog: {e}")
        await update.message.reply_text('❌ Ошибка загрузки каталога.')

async def sell_nft(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Продажа NFT"""
    try:
        nft_text = (
            '🎨 **Продать NFT через нашего бота:**\n\n'
            '📋 *Требования к NFT:*\n'
            '✅ Уникальное цифровое искусство\n'
            '✅ Высокое качество изображения\n'
            '✅ Права на распространение\n'
            '✅ Метаданные и описание\n\n'
            '💼 *Процесс продажи:*\n'
            '1. Отправьте нам файл NFT\n'
            '2. Укажите цену и описание\n'
            '3. Мы разместим в нашем каталоге\n'
            '4. Получите 85% от продажи\n\n'
            '💰 *Комиссия:* всего 15%\n'
            '⚡ *Выплаты:* ежедневно\n\n'
            '📞 *Для начала продажи напишите:* @manager_account'
        )
        await update.message.reply_text(nft_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Ошибка в sell_nft: {e}")
        await update.message.reply_text('❌ Ошибка загрузки информации.')

async def ton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Покупка TON"""
    try:
        ton_text = (
            '💎 **Покупка TON Coin:**\n\n'
            '🚀 *Почему TON?*\n'
            '⭐ Официальная крипта Telegram\n'
            '⭐ Быстрые транзакции\n'
            '⭐ Низкие комиссии\n'
            '⭐ Растущий потенциал\n\n'
            '💰 *Доступные пакеты:*\n'
            '✨ 100 TON - 10,000 руб\n'
            '✨ 500 TON - 45,000 руб\n'
            '✨ 1000 TON - 85,000 руб\n'
            '✨ 5000 TON - 400,000 руб\n\n'
            '🔒 *Гарантии:*\n'
            '✅ Мгновенная доставка\n'
            '✅ Безопасная сделка\n'
            '✅ Поддержка 24/7\n\n'
            '🛒 *Для покупки напишите:* @ton_manager'
        )
        await update.message.reply_text(ton_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Ошибка в ton: {e}")
        await update.message.reply_text('❌ Ошибка загрузки информации.')

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Связь с поддержкой"""
    try:
        support_text = (
            '📞 **Служба поддержки CryptoShop**\n\n'
            '💎 *По вопросам покупки:*\n'
            '@crypto_manager - криптовалюты\n'
            '@nft_manager - NFT коллекции\n'
            '@ton_manager - TON Coin\n\n'
            '🛠 *Технические вопросы:*\n'
            '@tech_support - боты и сайты\n\n'
            '⏰ *Время работы:* 24/7\n'
            '⚡ *Среднее время ответа:* 5-15 минут'
        )
        await update.message.reply_text(support_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Ошибка в support: {e}")
        await update.message.reply_text('❌ Ошибка загрузки поддержки.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Помощь по командам"""
    try:
        help_text = (
            '❓ **Доступные команды:**\n\n'
            '🎯 *Основные:*\n'
            '/start - начать работу\n'
            '/catalog - посмотреть каталог\n'
            '/ton - купить TON Coin\n'
            '/sell_nft - продать NFT\n'
            '/support - связаться с поддержкой\n\n'
            '💼 *Процесс заказа:*\n'
            '1. Выберите товар в /catalog\n'
            '2. Напишите соответствующему менеджеру\n'
            '3. Уточните детали заказа\n'
            '4. Получите товар и подтверждение'
        )
        await update.message.reply_text(help_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Ошибка в help: {e}")
        await update.message.reply_text('❌ Ошибка загрузки справки.')

def main():
    """Основная функция"""
    try:
        logger.info("Запуск CryptoShop бота...")
        
        # Создаем приложение
        application = Application.builder().token(TOKEN).build()
        
        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("catalog", catalog))
        application.add_handler(CommandHandler("sell_nft", sell_nft))
        application.add_handler(CommandHandler("ton", ton))
        application.add_handler(CommandHandler("support", support))
        application.add_handler(CommandHandler("help", help_command))
        
        # Запускаем бота
        logger.info("Бот запускается...")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Ошибка запуска бота: {e}")

if __name__ == '__main__':
    main()
