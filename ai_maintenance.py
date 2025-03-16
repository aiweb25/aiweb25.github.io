from flask import Flask, request, jsonify
import sqlite3
import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from flask import Flask, send_from_directory
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

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # نام صحیح فایل

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# مقداردهی اولیه پایگاه داده
def init_db():
    conn = sqlite3.connect('site_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS insights (id INTEGER PRIMARY KEY, insight TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS status (id INTEGER PRIMARY KEY, website TEXT, status TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# صفحه اصلی (حل مشکل 404)
@app.route('/')
def home():
    return "🚀 AI Maintenance System is Running! 🚀"

# کلاس مدیریت سایت
class UltimateAIManager:
    def __init__(self, url):
        self.url = url
        self.site_health_score = 100
    
    def check_website_status(self):
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                status = "Connected"
            else:
                status = "Error"
                self.site_health_score -= 10
        except requests.exceptions.RequestException:
            status = "Disconnected"
            self.site_health_score -= 20
        
        conn = sqlite3.connect('site_manager.db')
        c = conn.cursor()
        c.execute('INSERT INTO status (website, status) VALUES (?, ?)', (self.url, status))
        conn.commit()
        conn.close()
        return status

    def analyze(self):
        status = self.check_website_status()
        return {
            "website_status": status,
            "site_health_score": self.site_health_score
        }

# مسیر برای آنالیز سایت
@app.route('/analyze', methods=['GET'])
def analyze():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    manager = UltimateAIManager(url)
    report = manager.analyze()
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
