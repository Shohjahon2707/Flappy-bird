from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("▶ Играть в Flappy Bird", web_app={"url": "https://ТВОЙ_САЙТ/index.html"})]
    ])
    await update.message.reply_text("Готов к полёту? 🐤", reply_markup=keyboard)

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    await update.message.reply_text(f"🏆 Твой результат: {data}")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7235231537:AAHkGnoawgU1MV4LI8dwNypCvXM03ezMeag").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    print("Бот запущен...")
    app.run_polling()
