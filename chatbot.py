from flask import Flask, request, jsonify
import sqlite3
from flask import Flask, send_from_directory, render_template_string
import time
import threading
from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# 📌 نمایش صفحه اصلی سایت
@app.route('/')
def home():
    return send_from_directory(os.getcwd(), "index.html")  # لود از پوشه فعلی

# 📌 API بهینه‌سازی سایت
@app.route('/optimize')
def optimize():
    return jsonify({"message": "Website optimization started!"})

# 📌 سرو کردن فایل‌های استاتیک (CSS, JS, Images)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(os.getcwd(), path)  # لود همه فایل‌های پوشه فعلی

# 📌 فشرده‌سازی CSS و JS (حل مشکل escape sequence)
@app.route('/compress')
def compress():
    os.system("find . -type f -name '*.css' -exec gzip {} ';'")
    os.system("find . -type f -name '*.js' -exec gzip {} ';'")
    return jsonify({"message": "Compression completed!"})

if __name__ == '__main__':
    app.run(debug=True)


class AIWebsiteOptimizer:
    def __init__(self):
        pass

    def start_monitoring(self):
        # اجرای تابع به صورت زمانبندی شده هر 60 ثانیه
        self.schedule_task()

    def schedule_task(self):
        # اجرای تابع در هر 60 ثانیه
        threading.Timer(60.0, self.run_tasks).start()

    def run_tasks(self):
        self.scan_website()
        self.optimize_performance()
        self.enhance_security()
        self.adjust_ui_for_devices()
        # بعد از 60 ثانیه دوباره وظایف اجرا می‌شوند
        self.schedule_task()

    def scan_website(self):
        print("Scanning website for issues...")
        # تحلیل مبتنی بر AI برای وضعیت وبسایت، عملکرد، و SEO

    def optimize_performance(self):
        print("Optimizing website speed and efficiency...")
        # کشینگ مبتنی بر AI، بهینه‌سازی تصاویر و متعادل‌سازی بار

    def enhance_security(self):
        print("Enhancing website security and threat detection...")
        # دیوار آتش مبتنی بر AI، حفاظت از DDoS و اسکن آسیب‌پذیری‌ها

    def adjust_ui_for_devices(self):
        print("Adjusting UI for all screen sizes and devices...")
        # طراحی واکنش‌گرا و تنظیمات چیدمان مبتنی بر AI

# راه‌اندازی برنامه
optimizer = AIWebsiteOptimizer()
optimizer.start_monitoring()


app = Flask(__name__)

# مسیر برای نمایش index.html
@app.route('/')
def home():
    return render_template_string(open('index.html').read())  # بارگذاری مستقیم فایل HTML از پوشه اصلی

# نمایش فایل CSS
@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css', mimetype='text/css')

# نمایش فایل JavaScript
@app.route('/script.js')
def js():
    return send_from_directory('.', 'script.js', mimetype='application/javascript')

# نمایش favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico', mimetype='image/x-icon')

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)

def get_response(user_message):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT response FROM responses WHERE question = ?", (user_message,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "متوجه نشدم! لطفاً دقیق‌تر بپرس."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip()
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

# دیتابیس ساده برای ذخیره سوالات و پاسخ‌ها
chat_db = {
    "سلام": "سلام! چطور می‌تونم کمکت کنم؟",
    "چه خبر؟": "هیچ خبری ندارم! ولی می‌تونم کمکت کنم."
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chat_db.get(user_message, "متوجه نشدم، لطفاً دوباره تلاش کن.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
import sqlite3

# ایجاد دیتابیس و جدول
conn = sqlite3.connect('chat_db.db')
c = conn.cursor()

# ایجاد جدول سوالات و پاسخ‌ها
c.execute('''
    CREATE TABLE IF NOT EXISTS chat_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        response TEXT NOT NULL
    )
''')

# اضافه کردن سوالات و پاسخ‌ها
c.execute('INSERT INTO chat_responses (question, response) VALUES (?, ?)', ('سلام', 'سلام! چطور می‌تونم کمکت کنم؟'))
c.execute('INSERT INTO chat_responses (question, response) VALUES (?, ?)', ('چه خبر؟', 'هیچ خبری ندارم!'))

# ذخیره تغییرات و بستن ارتباط
conn.commit()
conn.close()
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# تابع برای جستجوی پاسخ از دیتابیس
def get_response(user_message):
    conn = sqlite3.connect('chat_db.db')
    c = conn.cursor()
    c.execute('SELECT response FROM chat_responses WHERE question = ?', (user_message,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "متوجه نشدم، لطفاً دوباره تلاش کن."

# روت چت
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# تابع برای جستجوی پاسخ از دیتابیس
def get_response(user_message):
    conn = sqlite3.connect('chat_db.db')
    c = conn.cursor()
    c.execute('SELECT response FROM chat_responses WHERE question = ?', (user_message,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "متوجه نشدم، لطفاً دوباره تلاش کن."

# روت چت
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

# دیتابیس ساده برای ذخیره سوالات و پاسخ‌ها
chat_db = {
    "سلام": "سلام! چطور می‌تونم کمکت کنم؟",
    "چه خبر؟": "هیچ خبری ندارم! ولی می‌تونم کمکت کنم."
    
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chat_db.get(user_message, "متوجه نشدم، لطفاً دوباره تلاش کن.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
import sqlite3

# ایجاد دیتابیس و جدول
conn = sqlite3.connect('chat_db.db')
c = conn.cursor()

# ایجاد جدول سوالات و پاسخ‌ها
c.execute('''
    CREATE TABLE IF NOT EXISTS chat_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        response TEXT NOT NULL
    )
''')

# اضافه کردن سوالات و پاسخ‌ها
c.execute('INSERT INTO chat_responses (question, response) VALUES (?, ?)', ('سلام', 'سلام! چطور می‌تونم کمکت کنم؟'))
c.execute('INSERT INTO chat_responses (question, response) VALUES (?, ?)', ('چه خبر؟', 'هیچ خبری ندارم!'))

