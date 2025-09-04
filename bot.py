import telebot
import openai

# API keys (⚠️ chỉ dùng test local, không up GitHub)
TELEGRAM_TOKEN = "8328759862:AAHDOXuSANBJ4QOezvBy2z2aahEkqG8OzDc"
OPENAI_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def reply_with_chatgpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response["choices"][0]["message"]["content"]
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"Lỗi: {str(e)}")

if __name__ == "__main__":
    print("✅ Bot Telegram đã khởi động...")
    bot.infinity_polling()
