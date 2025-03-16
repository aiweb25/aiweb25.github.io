from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

# 📌 نمایش صفحه اصلی سایت (index.html در همان پوشه)
@app.route('/')
def home():
    return send_file("index.html")

# 📌 API برای بهینه‌سازی سایت
@app.route('/optimize')
def optimize():
    return jsonify({"message": "Website optimization started!"})

# 📌 سرو کردن فایل‌های استاتیک (CSS, JS, Images) از پوشه اصلی
@app.route('/<path:filename>')
def serve_static(filename):
    if os.path.exists(filename):
        return send_file(filename)
    return "File not found", 404

# 📌 حل مشکل escape sequence در gzip
@app.route('/compress')
def compress():
    os.system("find . -type f -name '*.css' -exec gzip {} ';'")
    os.system("find . -type f -name '*.js' -exec gzip {} ';'")
    return jsonify({"message": "Compression completed!"})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
import threading

app = Flask(__name__)

class AIWebsiteOptimizer:
    def __init__(self):
        pass

    def start_monitoring(self):
        self.schedule_task()

    def schedule_task(self):
        threading.Timer(60.0, self.run_tasks).start()

    def run_tasks(self):
        self.scan_website()
        self.optimize_performance()
        self.enhance_security()
        self.adjust_ui_for_devices()
        self.schedule_task()

    def scan_website(self):
        print("Scanning website for issues...")
        # کد پایتون برای اسکن سایت و بررسی مشکلات

    def optimize_performance(self):
        print("Optimizing website speed and efficiency...")
        # کد پایتون برای بهینه‌سازی عملکرد سایت

    def enhance_security(self):
        print("Enhancing website security and threat detection...")
        # کد پایتون برای تقویت امنیت سایت

    def adjust_ui_for_devices(self):
        print("Adjusting UI for all screen sizes and devices...")
        # کد پایتون برای تنظیم طراحی سایت متناسب با دستگاه‌ها

# ایجاد API برای ارسال درخواست‌ها از سایت
@app.route('/optimize', methods=['GET'])
def optimize():
    optimizer = AIWebsiteOptimizer()
    optimizer.run_tasks()
    return jsonify({"status": "success", "message": "Optimization tasks started successfully!"})

if __name__ == '__main__':
    optimizer = AIWebsiteOptimizer()
    optimizer.start_monitoring()
    app.run(debug=True, port=5000)

from flask import Flask
import threading

app = Flask(__name__)

class AIWebsiteOptimizer:
    def __init__(self):
        pass

    def start_monitoring(self):
        self.schedule_task()

    def schedule_task(self):
        threading.Timer(60.0, self.run_tasks).start()

    def run_tasks(self):
        self.scan_website()
        self.optimize_performance()
        self.enhance_security()
        self.adjust_ui_for_devices()
        self.schedule_task()

    def scan_website(self):
        print("Scanning website for issues...")
        # کد پایتون برای اسکن سایت و بررسی مشکلات

    def optimize_performance(self):
        print("Optimizing website speed and efficiency...")
        # کد پایتون برای بهینه‌سازی عملکرد سایت

    def enhance_security(self):
        print("Enhancing website security and threat detection...")
        # کد پایتون برای تقویت امنیت سایت

    def adjust_ui_for_devices(self):
        print("Adjusting UI for all screen sizes and devices...")
        # کد پایتون برای تنظیم طراحی سایت متناسب با دستگاه‌ها

@app.route('/')
def home():
    return "Welcome to the AI Website Optimizer!"

if __name__ == '__main__':
    optimizer = AIWebsiteOptimizer()
    optimizer.start_monitoring()
    app.run(debug=True)

import time
import threading

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

from flask import Flask, send_from_directory, render_template_string

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
    
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    return jsonify({"message": "داده از سرور Flask دریافت شد!"})

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

# ذخیره تغییرات و بستن ارتباط
conn.commit()
conn.close()
from flask import Flask, request, jsonify
import sqlite3

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
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# مسیر برای صفحه اصلی سایت
@app.route('/')
def home():
    return render_template('index.html')  # صفحه HTML

# مسیر برای favicon (آیکون سایت)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico')  # آیکون سایت در همان پوشه

# مسیر برای فایل‌های استاتیک (CSS و JS)
@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')  # فایل CSS در همان پوشه

@app.route('/js.js')
def script():
    return send_from_directory('.', 'js.js')  # فایل JavaScript در همان پوشه

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, send_from_directory
import requests
from bs4 import BeautifulSoup

# تابع برای تحلیل سرعت سایت و بهینه‌سازی
def analyze_website(url):
    # بررسی سرعت بارگذاری
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # تشخیص فایل‌های سنگین یا دیر بارگذاری
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        if img_url:
            print(f"بررسی تصویر: {img_url}")
            # تحلیل اندازه و بهینه‌سازی تصاویر (به عنوان مثال)
            # شما می‌توانید از ابزارهای بهینه‌سازی برای تصاویر استفاده کنید

    # تحلیل مشکلات متا تگ‌ها (SEO)
    title_tag = soup.find('title')
    if title_tag:
        print(f"عنوان صفحه: {title_tag.text}")
    else:
        print("عنوان صفحه پیدا نشد!")

# تحلیل سایت شما
analyze_website('https://yourgamingnews.com')


app = Flask(__name__)

# صفحه اصلی
@app.route('/')
def home():
    return render_template('index.html')  # صفحه اصلی که باید در پوشه templates قرار گیرد

# درخواست برای favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico')  # آیکون که در ریشه پروژه قرار دارد

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    return jsonify({"message": f"Analyzing {url}..."}), 200

if __name__ == '__main__':
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')  # مسیر صحیح و بدون فاصله اضافی
def data():
    return "این مسیر به درستی کار می‌کند!"

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        
        if status_code == 200:
            print(f"✅ سایت {url} سالم است!")
        elif status_code == 404:
            print(f"⚠️ خطا! صفحه {url} یافت نشد (404).")
        elif status_code == 500:
            print(f"❌ خطای سرور در سایت {url} (500).")
        else:
            print(f"⚠️ کد وضعیت ناشناخته: {status_code}")

        # بررسی لینک‌های خراب داخل صفحه
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        for link in links:
            if link.startswith("http"):
                try:
                    link_response = requests.get(link, timeout=3)
                    if link_response.status_code == 404:
                        print(f"🚨 لینک خراب: {link}")
                except requests.exceptions.RequestException:
                    print(f"❌ خطا در بررسی لینک: {link}")

    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    return "این مسیر به درستی کار می‌کند!"

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        
        if status_code == 200:
            print(f"✅ سایت {url} سالم است!")
        elif status_code == 404:
            print(f"⚠️ خطا! صفحه {url} یافت نشد (404).")
        elif status_code == 500:
            print(f"❌ خطای سرور در سایت {url} (500).")
        else:
            print(f"⚠️ کد وضعیت ناشناخته: {status_code}")

        # بررسی لینک‌های خراب داخل صفحه
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        for link in links:
            if link.startswith("http"):
                try:
                    link_response = requests.get(link, timeout=3)
                    if link_response.status_code == 404:
                        print(f"🚨 لینک خراب: {link}")
                except requests.exceptions.RequestException:
                    print(f"❌ خطا در بررسی لینک: {link}")

    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import time
import openai

openai.api_key = "YOUR_API_KEY"


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    return "این مسیر به درستی کار می‌کند!"

if __name__ == '__main__':
    app.run(debug=True)


import subprocess

def generate_text(prompt, model="mistral", max_tokens=100):
    """ اجرای مدل زبانی محلی با ollama بدون نیاز به API """
    command = ["ollama", "run", model, prompt, "--max-tokens", str(max_tokens)]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

# تست مدل
print(generate_text("هوش مصنوعی چیست؟"))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    return "این مسیر به درستی کار می‌کند!"

# تابع بررسی وضعیت سایت
def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        
        if status_code == 200:
            print(f"✅ سایت {url} سالم است!")
        elif status_code == 404:
            print(f"⚠️ خطا! صفحه {url} یافت نشد (404).")
        elif status_code == 500:
            print(f"❌ خطای سرور در سایت {url} (500).")
        else:
            print(f"⚠️ کد وضعیت ناشناخته: {status_code}")

        # بررسی لینک‌های خراب داخل صفحه
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        for link in links:
            if link.startswith("http"):
                try:
                    link_response = requests.get(link, timeout=3)
                    if link_response.status_code == 404:
                        print(f"🚨 لینک خراب: {link}")
                except requests.exceptions.RequestException:
                    print(f"❌ خطا در بررسی لینک: {link}")

    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

# تابع بررسی سرعت لود سایت
def check_speed(url):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        load_time = time.time() - start_time
        print(f"⏳ سرعت لود سایت {url}: {load_time:.2f} ثانیه")
        
        if load_time > 3:
            print("⚠️ سایت کند است! پیشنهاد: بهینه‌سازی تصاویر و استفاده از CDN")
    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

# تست توابع بررسی سایت
check_website("https://example.com")
check_speed("https://example.com")

if __name__ == '__main__':
    app.run(debug=True)


def generate_blog_post(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "شما یک نویسنده هوش مصنوعی هستید."},
            {"role": "user", "content": f"یک مقاله حرفه‌ای درباره {topic} بنویس."}
        ]
    )
    return response["choices"][0]["message"]["content"]

print(generate_blog_post("بهترین تکنولوژی‌های 2025"))
from flask import Flask, request

app = Flask(__name__)

blocked_ips = set()

@app.before_request
def block_bad_ips():
    ip = request.remote_addr
    if ip in blocked_ips:
        return "⛔ دسترسی شما به این سایت مسدود شده است!", 403

@app.route('/')
def home():
    return "🚀 سایت در حال اجرا است!"

@app.route('/block_ip/<ip>')
def block_ip(ip):
    blocked_ips.add(ip)
    return f"🔴 IP {ip} مسدود شد!"

if __name__ == '__main__':
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        
        if status_code == 200:
            print(f"✅ سایت {url} سالم است!")
        elif status_code == 404:
            print(f"⚠️ خطا! صفحه {url} یافت نشد (404).")
        elif status_code == 500:
            print(f"❌ خطای سرور در سایت {url} (500).")
        else:
            print(f"⚠️ کد وضعیت ناشناخته: {status_code}")

        # بررسی لینک‌های خراب
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        for link in links:
            if link.startswith("http"):
                try:
                    link_response = requests.get(link, timeout=3)
                    if link_response.status_code == 404:
                        print(f"🚨 لینک خراب: {link}")
                except requests.exceptions.RequestException:
                    print(f"❌ خطا در بررسی لینک: {link}")

    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

# تست با آدرس سایت
check_website("https://example.com")
import time
import requests

def check_speed(url):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        load_time = time.time() - start_time
        print(f"⏳ سرعت لود سایت {url}: {load_time:.2f} ثانیه")
        
        if load_time > 3:
            print("⚠️ سایت کند است! پیشنهاد: بهینه‌سازی تصاویر، کاهش تعداد درخواست‌ها و استفاده از CDN")
    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

check_speed("https://example.com")
from selenium import webdriver

def test_responsive(url):
    driver = webdriver.Chrome()

    screen_sizes = [(1920, 1080), (1366, 768), (1024, 768), (768, 1024), (375, 667)]  
    for width, height in screen_sizes:
        driver.set_window_size(width, height)
        driver.get(url)
        print(f"✅ بررسی سایت در اندازه {width}x{height}")

    driver.quit()

test_responsive("https://example.com")
from flask import Flask, request

app = Flask(__name__)

blocked_ips = set()

@app.before_request
def block_bad_ips():
    ip = request.remote_addr
    if ip in blocked_ips:
        return "⛔ دسترسی شما به این سایت مسدود شده است!", 403

@app.route('/')
def home():
    return "🚀 سایت در حال اجرا است!"

@app.route('/block_ip/<ip>')
def block_ip(ip):
    blocked_ips.add(ip)
    return f"🔴 IP {ip} مسدود شد!"

if __name__ == '__main__':
    app.run(debug=True)
import openai

openai.api_key = "YOUR_API_KEY"

def generate_blog_post(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "شما یک نویسنده هوش مصنوعی هستید."},
            {"role": "user", "content": f"یک مقاله حرفه‌ای درباره {topic} بنویس."}
        ]
    )
    return response["choices"][0]["message"]["content"]

print(generate_blog_post("بهترین تکنولوژی‌های 2025"))
import requests
from bs4 import BeautifulSoup

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code

        if status_code == 200:
            print(f"✅ سایت {url} سالم است!")
        elif status_code in [404, 500, 403]:
            print(f"⚠️ خطا! صفحه {url} ارور {status_code} دارد.")

        soup = BeautifulSoup(response.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True)]

        for link in links:
            if link.startswith("http"):
                try:
                    if requests.get(link, timeout=3).status_code == 404:
                        print(f"🚨 لینک خراب: {link}")
                except requests.exceptions.RequestException:
                    print(f"❌ مشکل در بررسی لینک: {link}")

    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

check_website("https://example.com")
import time
import requests

def check_speed(url):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        load_time = time.time() - start_time
        print(f"⏳ سرعت لود سایت {url}: {load_time:.2f} ثانیه")

        if load_time > 3:
            print("⚠️ سایت کند است! پیشنهاد: فشرده‌سازی تصاویر، کاهش تعداد درخواست‌ها، استفاده از CDN")

    except requests.exceptions.RequestException:
        print(f"❌ سایت {url} در دسترس نیست!")

check_speed("https://example.com")
from flask import Flask, request

app = Flask(__name__)
blocked_ips = set()

@app.before_request
def block_bad_ips():
    ip = request.remote_addr
    if ip in blocked_ips:
        return "⛔ دسترسی شما مسدود شده است!", 403

@app.route('/block_ip/<ip>')
def block_ip(ip):
    blocked_ips.add(ip)
    return f"🔴 IP {ip} مسدود شد!"

if __name__ == '__main__':
    app.run(debug=True)
from bs4 import BeautifulSoup
import requests

def seo_analysis(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "❌ عنوان ندارد"
    description = soup.find("meta", attrs={"name": "description"})
    keywords = soup.find("meta", attrs={"name": "keywords"})

    print(f"🔍 عنوان: {title}")
    print(f"📌 توضیحات: {description['content'] if description else '❌ توضیحات ندارد'}")
    print(f"🏷️ کلمات کلیدی: {keywords['content'] if keywords else '❌ ندارد'}")

seo_analysis("https://example.com")
import openai

openai.api_key = "YOUR_API_KEY"

def generate_blog_post(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "شما یک نویسنده هوش مصنوعی هستید."},
            {"role": "user", "content": f"یک مقاله حرفه‌ای درباره {topic} بنویس."}
        ]
    )
    return response["choices"][0]["message"]["content"]

print(generate_blog_post("تکنولوژی‌های ۲۰۲۵"))
import pandas as pd

data = pd.read_csv("user_activity.csv")
most_viewed_pages = data['page'].value_counts()
print("📊 صفحات پر بازدید:")
print(most_viewed_pages)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_input = request.form["user_input"]
    response = f"🤖 پردازش شد: {user_input.upper()}"  # اینجا می‌توان پردازش هوش مصنوعی انجام داد
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_input = request.form["user_input"]
    response = f"🤖 پردازش شد: {user_input.upper()}"  # اینجا می‌توان پردازش هوش مصنوعی انجام داد
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/process", methods=["POST"])
def api_process():
    data = request.json
    user_input = data.get("text", "")
    response = {"result": f"🔍 تحلیل شد: {user_input.upper()}"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_input = request.form["user_input"]
    response = f"🤖 پردازش شد: {user_input.upper()}"  # اینجا می‌توان پردازش هوش مصنوعی انجام داد
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
    import requests
from bs4 import BeautifulSoup
import re
import time
import logging
import json
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AIWebsiteManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.device_compatibility_issues = []
        self.content_redundancy_issues = []

    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)  # لینک‌های داخلی را تکمیل کن
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        self.errors.append(f'Broken link: {link} (Status {res.status_code})')
                except requests.exceptions.RequestException:
                    self.errors.append(f'Unreachable link: {link}')
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی سرعت و عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                self.performance_issues.append(f'Page load time is slow: {load_time:.2f} seconds')
        except requests.exceptions.RequestException as e:
            self.errors.append(f'Performance issue: {e}')

    def check_seo(self):
        """ بررسی متا دیتا و سئو """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').text if soup.find('title') else 'No Title'
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No Description'
            if len(title) < 10 or len(description) < 50:
                self.errors.append('SEO Warning: Title or Description is too short')
        except Exception as e:
            logging.error(f'Error checking SEO: {e}')
    
    def check_device_compatibility(self):
        """ بررسی سازگاری با دستگاه‌های مختلف """
        device_resolutions = [(1920, 1080), (1366, 768), (768, 1024), (375, 667)]  # Desktop, Tablet, Mobile
        for width, height in device_resolutions:
            response = requests.get(self.url, headers={'User-Agent': f'Mozilla/5.0 (Width: {width}, Height: {height})'})
            if response.status_code != 200:
                self.device_compatibility_issues.append(f'Compatibility issue detected for {width}x{height}')
    
    def check_content_redundancy(self):
        """ بررسی تکرار محتوای سایت """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            content_list = [p.text.strip() for p in paragraphs if p.text.strip()]
            duplicate_content = set([content for content in content_list if content_list.count(content) > 1])
            if duplicate_content:
                self.content_redundancy_issues.append(f'Redundant content detected: {duplicate_content}')
        except Exception as e:
            logging.error(f'Error checking content redundancy: {e}')

    def report_issues(self):
        """ چاپ مشکلات شناسایی شده """
        issues = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Device Compatibility Issues': self.device_compatibility_issues,
            'Content Redundancy Issues': self.content_redundancy_issues
        }
        logging.info(json.dumps(issues, indent=4))

    def run_diagnostics(self):
        logging.info(f'Running diagnostics on {self.url} ...')
        self.check_broken_links()
        self.check_performance()
        self.check_seo()
        self.check_device_compatibility()
        self.check_content_redundancy()
        self.report_issues()

# اجرای برنامه
if __name__ == "__main__":
    website_url = "https://example.com"  # آدرس سایت خود را جایگزین کنید
    manager = AIWebsiteManager(website_url)
    manager.run_diagnostics()

    import requests
from bs4 import BeautifulSoup
import re
import time
import logging
import json
from urllib.parse import urljoin
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AIWebsiteManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.device_compatibility_issues = []
        self.content_redundancy_issues = []
        self.security_issues = []

    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        self.errors.append(f'Broken link: {link} (Status {res.status_code})')
                except requests.exceptions.RequestException:
                    self.errors.append(f'Unreachable link: {link}')
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی سرعت و عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                self.performance_issues.append(f'Page load time is slow: {load_time:.2f} seconds')
        except requests.exceptions.RequestException as e:
            self.errors.append(f'Performance issue: {e}')

    def check_seo(self):
        """ بررسی متا دیتا و سئو """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').text if soup.find('title') else 'No Title'
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No Description'
            if len(title) < 10 or len(description) < 50:
                self.errors.append('SEO Warning: Title or Description is too short')
        except Exception as e:
            logging.error(f'Error checking SEO: {e}')
    
    def check_device_compatibility(self):
        """ بررسی سازگاری با دستگاه‌های مختلف """
        device_resolutions = [(1920, 1080), (1366, 768), (768, 1024), (375, 667)]
        for width, height in device_resolutions:
            try:
                response = requests.get(self.url, headers={'User-Agent': f'Mozilla/5.0 (Width: {width}, Height: {height})'})
                if response.status_code != 200:
                    self.device_compatibility_issues.append(f'Compatibility issue detected for {width}x{height}')
            except Exception as e:
                logging.error(f'Error checking device compatibility: {e}')
    
    def check_content_redundancy(self):
        """ بررسی تکرار محتوای سایت """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            content_list = [p.text.strip() for p in paragraphs if p.text.strip()]
            duplicate_content = set([content for content in content_list if content_list.count(content) > 1])
            if duplicate_content:
                self.content_redundancy_issues.append(f'Redundant content detected: {duplicate_content}')
        except Exception as e:
            logging.error(f'Error checking content redundancy: {e}')
    
    def check_security_issues(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                self.security_issues.append('Security Warning: X-Frame-Options header missing')
            if 'Content-Security-Policy' not in response.headers:
                self.security_issues.append('Security Warning: Content-Security-Policy header missing')
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def report_issues(self):
        """ چاپ مشکلات شناسایی شده """
        issues = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Device Compatibility Issues': self.device_compatibility_issues,
            'Content Redundancy Issues': self.content_redundancy_issues,
            'Security Issues': self.security_issues
        }
        logging.info(json.dumps(issues, indent=4))

    def run_diagnostics(self):
        logging.info(f'Running diagnostics on {self.url} ...')
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_seo),
            threading.Thread(target=self.check_device_compatibility),
            threading.Thread(target=self.check_content_redundancy),
            threading.Thread(target=self.check_security_issues)
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.report_issues()

# اجرای برنامه
if __name__ == "__main__":
    website_url = "https://example.com"  # آدرس سایت خود را جایگزین کنید
    manager = AIWebsiteManager(website_url)
    manager.run_diagnostics()
    import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import nltk
from urllib.parse import urljoin
from flask import Flask, request, jsonify

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        self.errors.append(f'Broken link: {link} (Status {res.status_code})')
                except requests.exceptions.RequestException:
                    self.errors.append(f'Unreachable link: {link}')
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                self.performance_issues.append(f'Page load time is slow: {load_time:.2f} seconds')
        except requests.exceptions.RequestException as e:
            self.errors.append(f'Performance issue: {e}')
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                self.security_issues.append('Security Warning: X-Frame-Options header missing')
            if 'Content-Security-Policy' not in response.headers:
                self.security_issues.append('Security Warning: Content-Security-Policy header missing')
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text for h in soup.find_all('h2')]
                self.news_data.extend(headlines[:5])
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def report_status(self):
        """ تولید گزارش جامع از وضعیت سایت """
        report = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Security Issues': self.security_issues,
            'Latest Gaming News': self.news_data
        }
        return json.dumps(report, indent=4)
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return self.report_status()

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(json.loads(report))

if __name__ == '__main__':
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import nltk
from urllib.parse import urljoin
from flask import Flask, request, jsonify
import sqlite3
import hashlib
import os

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
        self.setup_database()
    
    def setup_database(self):
        """ ایجاد پایگاه داده برای ذخیره اطلاعات سایت """
        self.conn = sqlite3.connect('site_data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    
    def log_issue(self, issue):
        """ ذخیره مشکلات در پایگاه داده """
        self.cursor.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        self.conn.commit()
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        issue = f'Broken link: {link} (Status {res.status_code})'
                        self.errors.append(issue)
                        self.log_issue(issue)
                except requests.exceptions.RequestException:
                    issue = f'Unreachable link: {link}'
                    self.errors.append(issue)
                    self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                issue = f'Page load time is slow: {load_time:.2f} seconds'
                self.performance_issues.append(issue)
                self.log_issue(issue)
        except requests.exceptions.RequestException as e:
            issue = f'Performance issue: {e}'
            self.errors.append(issue)
            self.log_issue(issue)
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                issue = 'Security Warning: X-Frame-Options header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
            if 'Content-Security-Policy' not in response.headers:
                issue = 'Security Warning: Content-Security-Policy header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text for h in soup.find_all('h2')]
                self.news_data.extend(headlines[:5])
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def report_status(self):
        """ تولید گزارش جامع از وضعیت سایت """
        report = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Security Issues': self.security_issues,
            'Latest Gaming News': self.news_data
        }
        return json.dumps(report, indent=4)
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return self.report_status()

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(json.loads(report))

if __name__ == '__main__':
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import sqlite3
import hashlib
import os
import torch
import transformers
from transformers import pipeline
from flask import Flask, request, jsonify
from urllib.parse import urljoin
from datetime import datetime
import re

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
        self.sentiment_analysis_pipeline = pipeline("sentiment-analysis")
        self.setup_database()
    
    def setup_database(self):
        """ ایجاد پایگاه داده برای ذخیره اطلاعات سایت """
        self.conn = sqlite3.connect('site_data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    
    def log_issue(self, issue):
        """ ذخیره مشکلات در پایگاه داده """
        self.cursor.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        self.conn.commit()
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        issue = f'Broken link: {link} (Status {res.status_code})'
                        self.errors.append(issue)
                        self.log_issue(issue)
                except requests.exceptions.RequestException:
                    issue = f'Unreachable link: {link}'
                    self.errors.append(issue)
                    self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                issue = f'Page load time is slow: {load_time:.2f} seconds'
                self.performance_issues.append(issue)
                self.log_issue(issue)
        except requests.exceptions.RequestException as e:
            issue = f'Performance issue: {e}'
            self.errors.append(issue)
            self.log_issue(issue)
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                issue = 'Security Warning: X-Frame-Options header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
            if 'Content-Security-Policy' not in response.headers:
                issue = 'Security Warning: Content-Security-Policy header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text.strip() for h in soup.find_all('h2')]
                self.news_data.extend(headlines[:5])
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def analyze_sentiment(self):
        """ تحلیل احساسات کاربران نسبت به سایت """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = " ".join([p.text for p in soup.find_all('p')])
            sentiment = self.sentiment_analysis_pipeline(text_content[:1000])
            return sentiment
        except Exception as e:
            logging.error(f'Error analyzing sentiment: {e}')
            return []
    
    def detect_spam_comments(self):
        """ تشخیص نظرات اسپم در سایت """
        spam_keywords = ["free", "win money", "click here", "subscribe", "limited offer"]
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        comments = [comment.text for comment in soup.find_all('p')]
        spam_comments = [c for c in comments if any(keyword in c.lower() for keyword in spam_keywords)]
        return spam_comments
    
    def report_status(self):
        """ تولید گزارش جامع از وضعیت سایت """
        sentiment_result = self.analyze_sentiment()
        spam_comments = self.detect_spam_comments()
        report = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Security Issues': self.security_issues,
            'Latest Gaming News': self.news_data,
            'User Sentiment': sentiment_result,
            'Spam Comments Detected': spam_comments
        }
        return json.dumps(report, indent=4)
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return self.report_status()

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(json.loads(report))

if __name__ == '__main__':
    app.run(debug=True)
    import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import sqlite3
import hashlib
import os
import torch
import transformers
from transformers import pipeline
from flask import Flask, request, jsonify
from urllib.parse import urljoin
from datetime import datetime
import re
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
        self.sentiment_analysis_pipeline = pipeline("sentiment-analysis")
        self.setup_database()
    
    def setup_database(self):
        """ ایجاد پایگاه داده برای ذخیره اطلاعات سایت """
        self.conn = sqlite3.connect('site_data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    
    def log_issue(self, issue):
        """ ذخیره مشکلات در پایگاه داده """
        self.cursor.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        self.conn.commit()
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        issue = f'Broken link: {link} (Status {res.status_code})'
                        self.errors.append(issue)
                        self.log_issue(issue)
                except requests.exceptions.RequestException:
                    issue = f'Unreachable link: {link}'
                    self.errors.append(issue)
                    self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                issue = f'Page load time is slow: {load_time:.2f} seconds'
                self.performance_issues.append(issue)
                self.log_issue(issue)
        except requests.exceptions.RequestException as e:
            issue = f'Performance issue: {e}'
            self.errors.append(issue)
            self.log_issue(issue)
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                issue = 'Security Warning: X-Frame-Options header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
            if 'Content-Security-Policy' not in response.headers:
                issue = 'Security Warning: Content-Security-Policy header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text.strip() for h in soup.find_all('h2')]
                self.news_data.extend(headlines[:5])
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def analyze_trending_topics(self):
        """ تحلیل موضوعات داغ در گیمینگ """
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(self.news_data)
        kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
        topics = kmeans.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        trending_topics = [terms[i] for i in topics[0][:5]]
        return trending_topics
    
    def report_status(self):
        """ تولید گزارش جامع از وضعیت سایت """
        trending_topics = self.analyze_trending_topics()
        report = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Security Issues': self.security_issues,
            'Latest Gaming News': self.news_data,
            'Trending Topics': trending_topics
        }
        return json.dumps(report, indent=4)
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return self.report_status()

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(json.loads(report))

if __name__ == '__main__':
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import sqlite3
import hashlib
import os
import torch
import transformers
from transformers import pipeline
from flask import Flask, request, jsonify
from urllib.parse import urljoin
from datetime import datetime
import re
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
        self.sentiment_analysis_pipeline = pipeline("sentiment-analysis")
        self.setup_database()
    
    def setup_database(self):
        """ ایجاد پایگاه داده برای ذخیره اطلاعات سایت """
        self.conn = sqlite3.connect('site_data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    
    def log_issue(self, issue):
        """ ذخیره مشکلات در پایگاه داده """
        self.cursor.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        self.conn.commit()
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        issue = f'Broken link: {link} (Status {res.status_code})'
                        self.errors.append(issue)
                        self.log_issue(issue)
                except requests.exceptions.RequestException:
                    issue = f'Unreachable link: {link}'
                    self.errors.append(issue)
                    self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                issue = f'Page load time is slow: {load_time:.2f} seconds'
                self.performance_issues.append(issue)
                self.log_issue(issue)
        except requests.exceptions.RequestException as e:
            issue = f'Performance issue: {e}'
            self.errors.append(issue)
            self.log_issue(issue)
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                issue = 'Security Warning: X-Frame-Options header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
            if 'Content-Security-Policy' not in response.headers:
                issue = 'Security Warning: Content-Security-Policy header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text.strip() for h in soup.find_all('h2')]
                self.news_data.extend(headlines[:5])
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def analyze_trending_topics(self):
        """ تحلیل موضوعات داغ در گیمینگ """
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(self.news_data)
        kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
        topics = kmeans.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        trending_topics = [terms[i] for i in topics[0][:5]]
        return trending_topics
    
    def report_status(self):
        """ تولید گزارش جامع از وضعیت سایت """
        trending_topics = self.analyze_trending_topics()
        report = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Security Issues': self.security_issues,
            'Latest Gaming News': self.news_data,
            'Trending Topics': trending_topics
        }
        return json.dumps(report, indent=4)
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return self.report_status()

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(json.loads(report))

if __name__ == '__main__':
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import sqlite3
import hashlib
import os
import torch
import transformers
from transformers import pipeline
from flask import Flask, request, jsonify
from urllib.parse import urljoin
from datetime import datetime
import re
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from flask_cors import CORS
import random
import matplotlib.pyplot as plt

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)
CORS(app)  # فعال کردن CORS برای ارتباط با فرانت‌اند

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
        self.sentiment_analysis_pipeline = pipeline("sentiment-analysis")
        self.setup_database()
    
    def setup_database(self):
        """ ایجاد پایگاه داده برای ذخیره اطلاعات سایت """
        self.conn = sqlite3.connect('site_data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    
    def log_issue(self, issue):
        """ ذخیره مشکلات در پایگاه داده """
        self.cursor.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        self.conn.commit()
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        issue = f'Broken link: {link} (Status {res.status_code})'
                        self.errors.append(issue)
                        self.log_issue(issue)
                except requests.exceptions.RequestException:
                    issue = f'Unreachable link: {link}'
                    self.errors.append(issue)
                    self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                issue = f'Page load time is slow: {load_time:.2f} seconds'
                self.performance_issues.append(issue)
                self.log_issue(issue)
        except requests.exceptions.RequestException as e:
            issue = f'Performance issue: {e}'
            self.errors.append(issue)
            self.log_issue(issue)
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                issue = 'Security Warning: X-Frame-Options header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
            if 'Content-Security-Policy' not in response.headers:
                issue = 'Security Warning: Content-Security-Policy header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text.strip() for h in soup.find_all('h2')]
                self.news_data.extend(headlines[:5])
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def visualize_data(self):
        """ ایجاد نمودارهای بصری از داده‌ها """
        labels = ['Errors', 'Performance Issues', 'Security Issues']
        values = [len(self.errors), len(self.performance_issues), len(self.security_issues)]
        
        plt.figure(figsize=(6, 6))
        plt.bar(labels, values, color=['red', 'blue', 'orange'])
        plt.xlabel('Categories')
        plt.ylabel('Count')
        plt.title('Website Analysis Summary')
        plt.show()
    
    def report_status(self):
        """ تولید گزارش جامع از وضعیت سایت """
        report = {
            'Errors': self.errors,
            'Performance Issues': self.performance_issues,
            'Security Issues': self.security_issues,
            'Latest Gaming News': self.news_data,
        }
        return json.dumps(report, indent=4)
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return self.report_status()

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(json.loads(report))

if __name__ == '__main__':
    app.run(debug=True)
os.system(r"find /var/www/html -type f -name '*.css' -exec gzip {} \;")
os.system(r"find /var/www/html -type f -name '*.js' -exec gzip {} \;")
import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import sqlite3
import hashlib
import os
import torch
import transformers
from transformers import pipeline
from flask import Flask, request, jsonify
from urllib.parse import urljoin
from datetime import datetime
import re
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from flask_cors import CORS
import random
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)
CORS(app)  # فعال کردن CORS برای ارتباط با فرانت‌اند

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.setup_database()
    
    def setup_database(self):
        """ ایجاد پایگاه داده برای ذخیره اطلاعات سایت """
        self.conn = sqlite3.connect('site_data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, headline TEXT, sentiment TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    
    def log_issue(self, issue):
        """ ذخیره مشکلات در پایگاه داده """
        self.cursor.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        self.conn.commit()
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        issue = f'Broken link: {link} (Status {res.status_code})'
                        self.errors.append(issue)
                        self.log_issue(issue)
                except requests.exceptions.RequestException:
                    issue = f'Unreachable link: {link}'
                    self.errors.append(issue)
                    self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                issue = f'Page load time is slow: {load_time:.2f} seconds'
                self.performance_issues.append(issue)
                self.log_issue(issue)
        except requests.exceptions.RequestException as e:
            issue = f'Performance issue: {e}'
            self.errors.append(issue)
            self.log_issue(issue)
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                issue = 'Security Warning: X-Frame-Options header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
            if 'Content-Security-Policy' not in response.headers:
                issue = 'Security Warning: Content-Security-Policy header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ و تحلیل احساسات """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text.strip() for h in soup.find_all('h2')]
                
                for headline in headlines[:5]:
                    sentiment = self.sentiment_analyzer.polarity_scores(headline)
                    sentiment_label = "Positive" if sentiment['compound'] > 0 else "Negative" if sentiment['compound'] < 0 else "Neutral"
                    self.cursor.execute('INSERT INTO news (headline, sentiment) VALUES (?, ?)', (headline, sentiment_label))
                self.conn.commit()
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return {"message": "Analysis completed"}

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
import requests
from bs4 import BeautifulSoup
import time
import logging
import json
import threading
import sqlite3
import hashlib
import os
import torch
import transformers
from transformers import pipeline
from flask import Flask, request, jsonify
from urllib.parse import urljoin
from datetime import datetime
import re
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from flask_cors import CORS
import random
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# اپلیکیشن Flask برای تعامل با سایت
app = Flask(__name__)
CORS(app)  # فعال کردن CORS برای ارتباط با فرانت‌اند

class GamingAIManager:
    def __init__(self, url):
        self.url = url
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.news_data = []
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.setup_database()
    
    def setup_database(self):
        """ ایجاد پایگاه داده برای ذخیره اطلاعات سایت """
        self.conn = sqlite3.connect('site_data.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, headline TEXT, sentiment TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()
    
    def log_issue(self, issue):
        """ ذخیره مشکلات در پایگاه داده """
        self.cursor.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        self.conn.commit()
    
    def check_broken_links(self):
        """ بررسی لینک‌های خراب """
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            
            for link in links:
                if not link.startswith('http'):
                    link = urljoin(self.url, link)
                try:
                    res = requests.head(link, timeout=5)
                    if res.status_code >= 400:
                        issue = f'Broken link: {link} (Status {res.status_code})'
                        self.errors.append(issue)
                        self.log_issue(issue)
                except requests.exceptions.RequestException:
                    issue = f'Unreachable link: {link}'
                    self.errors.append(issue)
                    self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking broken links: {e}')
    
    def check_performance(self):
        """ بررسی عملکرد سایت """
        start_time = time.time()
        try:
            response = requests.get(self.url, timeout=10)
            load_time = time.time() - start_time
            if load_time > 3:
                issue = f'Page load time is slow: {load_time:.2f} seconds'
                self.performance_issues.append(issue)
                self.log_issue(issue)
        except requests.exceptions.RequestException as e:
            issue = f'Performance issue: {e}'
            self.errors.append(issue)
            self.log_issue(issue)
    
    def check_security(self):
        """ بررسی مسائل امنیتی """
        try:
            response = requests.get(self.url)
            if 'X-Frame-Options' not in response.headers:
                issue = 'Security Warning: X-Frame-Options header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
            if 'Content-Security-Policy' not in response.headers:
                issue = 'Security Warning: Content-Security-Policy header missing'
                self.security_issues.append(issue)
                self.log_issue(issue)
        except Exception as e:
            logging.error(f'Error checking security: {e}')
    
    def fetch_latest_gaming_news(self):
        """ دریافت جدیدترین اخبار گیمینگ و تحلیل احساسات """
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = [h.text.strip() for h in soup.find_all('h2')]
                
                for headline in headlines[:5]:
                    sentiment = self.sentiment_analyzer.polarity_scores(headline)
                    sentiment_label = "Positive" if sentiment['compound'] > 0 else "Negative" if sentiment['compound'] < 0 else "Neutral"
                    self.cursor.execute('INSERT INTO news (headline, sentiment) VALUES (?, ?)', (headline, sentiment_label))
                self.conn.commit()
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
    
    def run_analysis(self):
        """ اجرای تمامی بررسی‌ها به صورت همزمان """
        threads = [
            threading.Thread(target=self.check_broken_links),
            threading.Thread(target=self.check_performance),
            threading.Thread(target=self.check_security),
            threading.Thread(target=self.fetch_latest_gaming_news)
        ]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return {"message": "Analysis completed"}

# API برای کنترل و گزارش وضعیت سایت
@app.route('/analyze', methods=['GET'])
def analyze_website():
    website_url = request.args.get('url')
    if not website_url:
        return jsonify({"error": "Please provide a website URL"}), 400
    
    manager = GamingAIManager(website_url)
    report = manager.run_analysis()
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
import requests
import json
import os
from time import sleep

# مدل هوش مصنوعی برای تشخیص و حل مشکلات سایت
class SiteAI:
    def __init__(self, site_url):
        self.site_url = site_url
        self.issue_log = []

    def check_site_status(self):
        """ بررسی وضعیت سایت """
        try:
            response = requests.get(self.site_url)
            if response.status_code != 200:
                self.issue_log.append(f"مشکل در دسترسی به سایت: {self.site_url}")
                self.fix_issue('site_down')
            else:
                print(f"سایت {self.site_url} در دسترس است.")
        except requests.exceptions.RequestException as e:
            self.issue_log.append(f"خطا در ارتباط با سایت: {str(e)}")
            self.fix_issue('site_down')

    def fix_issue(self, issue_type):
        """ حل مشکلات خودکار """
        if issue_type == 'site_down':
            print("در حال تلاش برای رفع مشکل دسترسی به سایت...")
            # اقدامات خودکار برای رفع مشکل سایت
            # می‌توانید در این بخش از کد، اقداماتی مانند ریستارت سرور یا بررسی وضعیت DNS را اضافه کنید
            sleep(3)  # شبیه‌سازی زمان رفع مشکل
            print(f"مشکل {issue_type} رفع شد.")
            self.issue_log.append(f"مشکل {issue_type} رفع شد.")

    def analyze_user_behavior(self):
        """ تجزیه و تحلیل رفتار کاربران """
        # اینجا می‌توانید از داده‌های کاربران برای شناسایی مشکلات یا بهینه‌سازی تجربه استفاده کنید.
        pass

    def apply_updates(self):
        """ اعمال به‌روزرسانی‌های هوشمند """
        print("در حال اعمال به‌روزرسانی‌های جدید...")
        # به‌روزرسانی‌های پیشنهادی سیستم
        pass

# اجرای هوش مصنوعی برای سایت
site_ai = SiteAI('https://example.com')
site_ai.check_site_status()
site_ai.apply_updates()
import requests
import os
import time
import logging
import subprocess
import psutil
import json
from bs4 import BeautifulSoup
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# تنظیمات اولیه
SITE_URL = "https://example.com"  # آدرس سایت
LOG_FILE = "site_ai_log.txt"
SECURITY_CHECKS = ["sql_injection", "xss", "ddos_protection"]
DB_BACKUP_PATH = "/backups/site_backup.sql"

# پیکربندی لاگ‌گیری
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

class SmartSiteAI:
    def __init__(self, site_url):
        self.site_url = site_url
        self.issue_log = []

    def check_site_status(self):
        """ بررسی وضعیت سایت و در دسترس بودن آن """
        try:
            response = requests.get(self.site_url)
            if response.status_code != 200:
                self.log_issue(f"⚠️ خطای دسترسی به سایت: {self.site_url}")
                self.fix_issue('site_down')
            else:
                print(f"✅ سایت {self.site_url} در دسترس است.")
        except requests.exceptions.RequestException as e:
            self.log_issue(f"❌ خطای ارتباط با سایت: {str(e)}")
            self.fix_issue('site_down')

    def analyze_html(self):
        """ بررسی مشکلات احتمالی در ساختار HTML سایت """
        response = requests.get(self.site_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        errors = []
        if not soup.find("title"):
            errors.append("🚨 سایت عنوان (title) ندارد.")
        if not soup.find("meta", {"name": "description"}):
            errors.append("⚠️ سایت توضیحات متا ندارد.")
        if errors:
            self.log_issue("\n".join(errors))

    def fix_issue(self, issue_type):
        """ حل مشکلات به صورت خودکار """
        if issue_type == 'site_down':
            print("🔄 تلاش برای رفع مشکل دسترسی به سایت...")
            self.restart_server()

    def restart_server(self):
        """ راه‌اندازی مجدد سرور در صورت نیاز """
        os.system("systemctl restart apache2")
        logging.info("🔁 سرور مجدداً راه‌اندازی شد.")

    def check_security(self):
        """ بررسی امنیت سایت در برابر حملات SQL Injection و XSS """
        vulnerabilities = []
        for check in SECURITY_CHECKS:
            if check == "sql_injection":
                response = requests.get(f"{self.site_url}/?id=1' OR '1'='1")
                if "error" in response.text.lower():
                    vulnerabilities.append("⚠️ سایت ممکن است در برابر SQL Injection آسیب‌پذیر باشد.")
            if check == "xss":
                response = requests.get(f"{self.site_url}/?search=<script>alert('XSS')</script>")
                if "<script>" in response.text:
                    vulnerabilities.append("🚨 سایت نسبت به XSS آسیب‌پذیر است.")

        if vulnerabilities:
            self.log_issue("\n".join(vulnerabilities))
        else:
            print("✅ امنیت سایت در وضعیت مطلوب است.")

    def log_issue(self, message):
        """ ثبت مشکلات در لاگ و اطلاع‌رسانی """
        logging.info(message)
        self.issue_log.append(message)
        print(f"⚠️ {message}")

    def backup_database(self):
        """ پشتیبان‌گیری از پایگاه داده سایت """
        print("📂 در حال گرفتن بکاپ از پایگاه داده...")
        os.system(f"mysqldump -u root -p database_name > {DB_BACKUP_PATH}")
        logging.info("✅ بکاپ پایگاه داده انجام شد.")

    def monitor_cpu_usage(self):
        """ نظارت بر مصرف CPU و RAM سرور """
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        if cpu_usage > 85:
            self.log_issue(f"🔥 هشدار: مصرف CPU بالاست ({cpu_usage}%)")
        if ram_usage > 85:
            self.log_issue(f"⚡ هشدار: مصرف RAM بالاست ({ram_usage}%)")

    def optimize_website(self):
        """ بهینه‌سازی سایت برای افزایش سرعت و عملکرد """
        print("⚡ در حال بهینه‌سازی فایل‌های استاتیک سایت...")
        os.system("find /var/www/html -type f -name '*.css' -exec gzip {} \;")
        os.system("find /var/www/html -type f -name '*.js' -exec gzip {} \;")
        logging.info("✅ بهینه‌سازی فایل‌های استاتیک انجام شد.")

    def analyze_user_behavior(self):
        """ تجزیه و تحلیل رفتار کاربران با یادگیری ماشین """
        print("📊 در حال تحلیل رفتار کاربران...")
        data = np.array([
            [10, 5], [20, 10], [15, 7], [25, 12], [30, 15]
        ])
        labels = [0, 1, 0, 1, 1]

        model = RandomForestClassifier()
        model.fit(data, labels)

        prediction = model.predict([[18, 8]])  # نمونه داده برای تست
        print(f"🔮 پیش‌بینی رفتار کاربران: {'فعالیت بالا' if prediction[0] else 'فعالیت پایین'}")

    def apply_updates(self):
        """ نصب و بروزرسانی‌های موردنیاز سایت """
        print("🚀 در حال بررسی و نصب به‌روزرسانی‌های جدید...")
        os.system("apt update && apt upgrade -y")
        logging.info("✅ به‌روزرسانی‌های سیستم انجام شد.")

    def run_all_tasks(self):
        """ اجرای همه وظایف هوش مصنوعی سایت """
        self.check_site_status()
        self.analyze_html()
        self.check_security()
        self.monitor_cpu_usage()
        self.optimize_website()
        self.backup_database()
        self.analyze_user_behavior()
        self.apply_updates()

# اجرای سیستم هوش مصنوعی
site_ai = SmartSiteAI(SITE_URL)
site_ai.run_all_tasks()
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    return jsonify({"message": f"Analyzing {url}..."}), 200

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint for analyzing gaming news
@app.route('/analyze', methods=['GET'])
def analyze():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    # اینجا باید تحلیل‌های گیمینگ و اخبار رو انجام بدی
    # به عنوان مثال: می‌تونی تجزیه و تحلیل احساسات یا ترندهای اخبار گیمینگ رو انجام بدی.
    return jsonify({"message": f"Analyzing gaming news at {url}..."}), 200

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
import openai
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# API key for OpenAI GPT-3
openai.api_key = 'your_openai_api_key'  # Replace with your actual API key

@app.route('/analyze', methods=['GET'])
def analyze_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Request the content of the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = soup.get_text()

        # Use OpenAI API to analyze the content
        analysis = openai.Completion.create(
            engine="text-davinci-003",  # Replace with your model
            prompt=f"Analyze the following gaming news article and provide a summary: {article_text}",
            max_tokens=500
        )

        return jsonify({"message": analysis.choices[0].text.strip()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/')
def home():
    return render_template('index.html')
app.debug = False
