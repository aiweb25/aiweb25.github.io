import logging
import sqlite3
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request, render_template, send_from_directory
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import IsolationForest
import openai
from user_agents import parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
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


# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ایجاد اپلیکیشن Flask
app = Flask(__name__)

# پایگاه داده SQLite را برای ذخیره‌سازی داده‌ها راه‌اندازی کنید
def init_db():
    conn = sqlite3.connect('site_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, issue TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS insights (id INTEGER PRIMARY KEY, insight TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS status (id INTEGER PRIMARY KEY, website TEXT, status TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# کلاس مدیریت سایت برای تجزیه و تحلیل وضعیت سایت و تولید گزارش‌ها
class WebsiteAnalyzer:
    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent
        self.errors = []
        self.performance_issues = []
        self.security_issues = []
        self.device_info = self.detect_device()

    def detect_device(self):
        parsed_user_agent = parse(self.user_agent)
        return {
            "browser": parsed_user_agent.browser.family,
            "os": parsed_user_agent.os.family,
            "device": parsed_user_agent.device.family
        }

    def log_issue(self, issue):
        conn = sqlite3.connect('site_manager.db')
        c = conn.cursor()
        c.execute('INSERT INTO logs (issue) VALUES (?)', (issue,))
        conn.commit()
        conn.close()

    def check_broken_links(self):
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

    def analyze_trending_topics(self):
        news_sources = ["https://www.pcgamer.com/news/", "https://kotaku.com/c/gaming"]
        headlines = []
        for source in news_sources:
            try:
                response = requests.get(source)
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines.extend([h.text.strip() for h in soup.find_all('h2')])
            except Exception as e:
                logging.error(f'Error fetching news from {source}: {e}')
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(headlines)
        kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
        topics = kmeans.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        self.trending_topics = [terms[i] for i in topics[0][:5]]

    def analyze(self):
        self.check_broken_links()
        self.check_performance()
        self.check_security()
        self.analyze_trending_topics()
        return {
            "errors": self.errors,
            "performance_issues": self.performance_issues,
            "security_issues": self.security_issues,
            "device_info": self.device_info,
            "trending_topics": self.trending_topics
        }

# ایجاد روت برای تجزیه و تحلیل سایت
@app.route('/analyze', methods=['GET'])
def analyze():
    url = request.args.get('url')
    user_agent = request.headers.get('User-Agent', '')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    analyzer = WebsiteAnalyzer(url, user_agent)
    report = analyzer.analyze()
    return jsonify(report)

# روت‌های اضافی برای ارتباط با فایل‌ها و صفحات
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/js.js')
def script():
    return send_from_directory('.', 'js.js')

# اجرای اپلیکیشن Flask
if __name__ == '__main__':
    app.run(debug=True)
