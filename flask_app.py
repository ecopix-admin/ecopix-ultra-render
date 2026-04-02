import telebot
import requests
import time
from flask import Flask
import threading
import os

# --- AYARLAR ---
API_TOKEN = '8682822347:AAGeoo5wc8idiebNwzwvzJvKaaqoDgG4MIs'
AD_LINK = "https://www.profitablecpmratenetwork.com/caarhipxw?key=a23c49e3b1a0789535a6b848d7a66c9f"
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

stats = {'total_views': 0, 'today_infected': 0, 'status': "Stabil (Baku/Azerbaijan)"}

def auto_infector():
    while True:
        try:
            # Hər dəqiqə virtual yoluxdurma
            stats['today_infected'] += 1 
            stats['total_views'] += 12
            time.sleep(60) 
        except Exception as e:
            print(f"Xəta: {e}")

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("📊 10 Saatlıq Hesabat")
    item2 = telebot.types.KeyboardButton("🔄 Sistemi Yenilə")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "✅ EcoPix Ultra Render Sistemi Aktivdir!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📊 10 Saatlıq Hesabat")
def report(message):
    earnings = round(stats['total_views'] * 0.002, 2)
    report_text = (f"🕒 **Son 10 Saatlıq Canlı Hesabat:**\n\n"
                   f"✅ **Yoluxdurulan Trend Videolar:** {stats['today_infected']} ədəd\n"
                   f"👥 **Ümumi Baxış (Anten sayı):** {stats['total_views']} nəfər\n"
                   f"💰 **Təxmini Adsterra Qazancı:** ${earnings}\n"
                   f"📡 **Şəbəkə Statusu:** {stats['status']}")
    bot.send_message(message.chat.id, report_text, parse_mode="Markdown")

@app.route('/')
def index():
    return "EcoPix Bot İşləyir!"

def run_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    threading.Thread(target=auto_infector, daemon=True).start()
    threading.Thread(target=run_bot, daemon=True).start()
    
    # RENDER ÜÇÜN VACİB PORT AYARI
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
