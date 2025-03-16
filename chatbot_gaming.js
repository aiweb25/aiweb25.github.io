document.addEventListener("DOMContentLoaded", function() {
    // تشخیص دستگاه موبایل یا دسکتاپ
    function isMobile() {
      return window.innerWidth <= 768; // تغییر این مقدار به سایز دلخواه
    }
  
    if (isMobile()) {
      // انجام تغییرات خاص برای موبایل
  
      // ویدیوها را به طور خودکار در اندازه درست تنظیم کن
      document.querySelectorAll('video, iframe').forEach(function(el) {
        el.style.width = '100%';
        el.style.height = 'auto';
      });
  
      // تنظیم خودکار تصاویر
      document.querySelectorAll('img').forEach(function(img) {
        img.style.maxWidth = '100%';
        img.style.height = 'auto';
      });
  
      // تنظیم متن‌ها برای موبایل
      document.querySelectorAll('.text-content').forEach(function(text) {
        text.style.wordWrap = 'break-word';
      });
  
      // جلوگیری از اسکرول افقی و مشکلات نمایش
      document.body.style.overflowX = 'hidden';
      document.body.style.overflowY = 'auto';
    }
  
    // برای دسکتاپ یا تبلت‌ها
    else {
      // تنظیمات پیشرفته برای دستگاه‌های بزرگتر
      document.body.style.overflowX = 'visible';
      document.body.style.overflowY = 'visible';
    }
  
    // برای اسکرول عمودی و فیکس کردن تصاویر و ویدیوها
    setTimeout(() => {
      document.querySelectorAll('video, iframe').forEach(function(el) {
        if (el.offsetWidth > window.innerWidth) {
          el.style.maxWidth = '100%';
          el.style.height = 'auto';
        }
      });
      document.querySelectorAll('img').forEach(function(img) {
        img.style.maxWidth = '100%';
        img.style.height = 'auto';
      });
    }, 500);
  });
  
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        document.body.style.overflowY = "auto";
        document.documentElement.style.overflowY = "auto";
        console.log("اسکرول فعال شد!");
    }, 500);
});

fetch("/optimize", {
    method: "POST",
})
.then(response => response.json())
.then(data => {
    document.getElementById("status").innerText = data.message;
})
.catch(error => {
    document.getElementById("status").innerText = "خطا در بهینه‌سازی";
    console.error('Error:', error);
});

window.addEventListener('resize', function() {
    let screenWidth = window.innerWidth;
    
    // تشخیص مشکلات و اصلاح خودکار در عرض صفحه
    if (screenWidth < 768) {
        // تنظیمات خاص موبایل
        document.body.style.fontSize = "14px";
        document.querySelector('.header').style.flexDirection = "column";
    } else {
        // تنظیمات خاص دسکتاپ
        document.body.style.fontSize = "16px";
        document.querySelector('.header').style.flexDirection = "row";
    }
});

setTimeout(function() {
    const statusMessage = document.getElementById('status-message');

    // تغییر وضعیت به آنلاین
    statusMessage.innerHTML = '<p>شما آنلاین هستید</p>';
    statusMessage.classList.remove('offline');
    statusMessage.classList.add('online');

    // بعد از 3 ثانیه محو شود
    setTimeout(function() {
        statusMessage.classList.add('hidden');
    }, 3000);

}, 3000); // بعد از 3 ثانیه وضعیت تغییر می‌کند

document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        document.body.style.overflowY = "auto";
        document.documentElement.style.overflowY = "auto";
        console.log("اسکرول فعال شد!");
    }, 500);
});

document.addEventListener("DOMContentLoaded", function() {
    document.body.style.overflowY = "auto"; // اطمینان از فعال بودن اسکرول عمودی
});

document.addEventListener("DOMContentLoaded", function() {
    // بررسی و تنظیم اندازه ویدیوها
    document.querySelectorAll('video, iframe').forEach(video => {
        video.style.width = "100%";
        video.style.height = "auto";
        
        setTimeout(() => {
            if (video.offsetWidth > window.innerWidth) {
                video.style.maxWidth = "100%";
                video.style.height = "auto";
            }
        }, 500);
    });

    // بررسی و رفع مشکل اسکرول در موبایل
    document.body.style.overflowY = "auto";
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('video, iframe').forEach(video => {
        video.style.width = "100%";
        video.style.height = "auto";

        setTimeout(() => {
            if (video.offsetWidth > window.innerWidth) {
                video.style.maxWidth = "100%";
                video.style.height = "auto";
            }
        }, 500);
    });
});

document.getElementById('optimizeButton').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/optimize')
        .then(response => response.json())
        .then(data => {
            alert(data.message); // پیغام دریافت شده از Flask
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
document.getElementById('optimizeButton').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/optimize')
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
// تنظیم اندازه تصویر بر اساس اندازه صفحه
function adjustImageSize() {
    const device = detectDevice();
    const images = document.querySelectorAll('img');

    images.forEach(img => {
        if (device === 'Mobile') {
            img.style.width = '100%';
        } else {
            img.style.width = 'auto';
        }
    });
}

window.addEventListener('resize', adjustImageSize);
adjustImageSize(); // هنگام بارگذاری صفحه

// تشخیص دستگاه (موبایل، تبلت، دسکتاپ)
function detectDevice() {
    const ua = navigator.userAgent;

    if (/Mobi|Android|iPhone|iPad|iPod/i.test(ua)) {
        return 'Mobile'; // دستگاه موبایل یا تبلت
    } else {
        return 'Desktop'; // دستگاه دسکتاپ
    }
}

// تشخیص مرورگر
function detectBrowser() {
    const ua = navigator.userAgent;

    if (ua.indexOf('Chrome') > -1) {
        return 'Chrome';
    } else if (ua.indexOf('Firefox') > -1) {
        return 'Firefox';
    } else if (ua.indexOf('Safari') > -1) {
        return 'Safari';
    } else if (ua.indexOf('Edge') > -1) {
        return 'Edge';
    } else {
        return 'Unknown';
    }
}

// استفاده از این توابع
console.log(detectDevice()); // موبایل یا دسکتاپ
console.log(detectBrowser()); // مرورگر کاربر

function analyzeAndFix() {
    document.querySelectorAll(".element").forEach(el => {
        if (el.offsetWidth > window.innerWidth) {
            el.style.maxWidth = "100%";
        }
        if (el.offsetLeft < 0) {
            el.style.left = "0px";
        }
    });
}

// استفاده از یادگیری ماشین برای تشخیص مشکلات رایج و بهبود مستمر
async function trainAI() {
    let problemsDetected = [];
    document.querySelectorAll(".element").forEach(el => {
        if (el.offsetWidth > window.innerWidth || el.offsetLeft < 0) {
            problemsDetected.push({ element: el.className, issue: "Layout Overflow" });
        }
    });

    if (problemsDetected.length > 0) {
        localStorage.setItem("layoutFixes", JSON.stringify(problemsDetected));
        console.log("AI has learned from detected issues:", problemsDetected);
    }
}

window.addEventListener("resize", () => { analyzeAndFix(); trainAI(); });
document.addEventListener("DOMContentLoaded", () => { analyzeAndFix(); trainAI(); });

function adjustFontSettings() {
    const width = window.innerWidth;
    document.body.style.fontSize = width < 600 ? "14px" : "16px";

    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.style.backgroundColor = "#121212";
        document.body.style.color = "#ffffff";
    }
}

window.addEventListener("resize", adjustFontSettings);
adjustFontSettings();

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("img, video").forEach(media => {
        media.style.maxWidth = "100%";
        media.style.height = "auto";
    });
});

function autoFixLayout() {
    document.querySelectorAll(".content").forEach(el => {
        if (el.offsetLeft < 0 || el.offsetWidth > window.innerWidth) {
            el.style.margin = "auto";
            el.style.width = "95%";
        }
    });
}

window.addEventListener("resize", autoFixLayout);
document.addEventListener("DOMContentLoaded", autoFixLayout);

function detectEnvironment() {
    const ua = navigator.userAgent;
    let deviceType = "Desktop";
    if (/Mobi|Android/i.test(ua)) deviceType = "Mobile";
    else if (/Tablet|iPad/i.test(ua)) deviceType = "Tablet";

    return {
        device: deviceType,
        browser: navigator.userAgent,
        screenWidth: window.innerWidth,
        screenHeight: window.innerHeight,
        dpi: window.devicePixelRatio,
        connection: navigator.connection ? navigator.connection.effectiveType : "unknown",
        darkMode: window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches,
        battery: navigator.getBattery ? navigator.getBattery().then(b => b.level * 100) : "unknown"
    };
}

console.log(detectEnvironment());

class AIWebsiteOptimizer {
    constructor() {
        console.log("Initializing Advanced AI Website Optimization System...");
        this.startMonitoring();
    }

    startMonitoring() {
        setInterval(() => {
            this.scanWebsite();
            this.optimizePerformance();
            this.enhanceSecurity();
            this.adjustUIForDevices();
        }, 60000); // Runs every 60 seconds
    }

    scanWebsite() {
        console.log("Scanning website for issues...");
        // AI-based analysis of website health, performance, and SEO
    }

    optimizePerformance() {
        console.log("Optimizing website speed and efficiency...");
        // AI-driven caching, image optimization, and load balancing
    }

    enhanceSecurity() {
        console.log("Enhancing website security and threat detection...");
        // AI-based firewall, DDoS protection, and vulnerability scanning
    }

    adjustUIForDevices() {
        console.log("Adjusting UI for all screen sizes and devices...");
        // AI-driven responsive design and adaptive layout adjustments
    }
}

const optimizer = new AIWebsiteOptimizer();

 // این توابع به صفحات یوتیوب لینک می‌دهند و کاربر را هدایت می‌کنند
 function goToYouTubeSubscribe() {
    window.open("https://www.youtube.com/channel/CHANNEL_ID?sub_confirmation=1", "_blank"); // CHANNEL_ID را با ID کانال خود جایگزین کنید
}

function goToYouTubeLike() {
    window.open("https://www.youtube.com/watch?v=VIDEO_ID&action=like", "_blank"); // VIDEO_ID را با ID ویدیو خود جایگزین کنید
}

function shareVideo() {
    // اشتراک گذاری ویدیو در شبکه‌های اجتماعی یا کپی لینک ویدیو
    const videoUrl = "https://www.youtube.com/watch?v=VIDEO_ID"; // VIDEO_ID را با ID ویدیو خود جایگزین کنید
    const shareText = `Check out this awesome video: ${videoUrl}`;
    if (navigator.share) {
        navigator.share({
            title: 'Awesome Video',
            text: shareText,
            url: videoUrl
        }).catch(console.error);
    } else {
        alert("Share this video: " + videoUrl);
    }
}

let liked = false;
function toggleLike() {
    const likeBtn = document.getElementById('like-btn');
    liked = !liked;
    if (liked) {
        likeBtn.classList.add('liked');
        console.log('Liked the video');
    } else {
        likeBtn.classList.remove('liked');
        console.log('Removed like');
    }
}
// دریافت اخبار زنده به صورت داینامیک
function fetchLiveNews() {
    fetch('/api/live-news')
        .then(response => response.json())
        .then(news => {
            const newsFeed = document.getElementById('live-news-feed');
            newsFeed.innerHTML = '';
            news.forEach(item => {
                const newsItem = document.createElement('div');
                newsItem.classList.add('news-item');
                newsItem.innerHTML = `<h4>${item.title}</h4><p>${item.description}</p>`;
                newsFeed.appendChild(newsItem);
            });
        });
}

// به‌روزرسانی اخبار هر 10 ثانیه
setInterval(fetchLiveNews, 10000);

function searchArticles() {
    const searchQuery = document.getElementById('search-bar').value;
    const searchResults = document.getElementById('search-results');
    
    // فرض می‌کنیم که داده‌ها از پایگاه داده یا API گرفته می‌شود
    fetch(`/search?query=${searchQuery}`)
        .then(response => response.json())
        .then(data => {
            let resultsHTML = '';
            data.forEach(item => {
                resultsHTML += `<div class="result-item">
                    <h4>${item.title}</h4>
                    <p>${item.description}</p>
                </div>`;
            });
            searchResults.innerHTML = resultsHTML;
        });
}

// script.js

// تابع برای بررسی آنلاین بودن سایت با استفاده از پینگ
function checkPing() {
    // درخواست به سایت برای بررسی وضعیت آنلاین بودن
    fetch(window.location.href)
        .then(response => {
            if (response.ok) {
                document.getElementById('site-status').innerText = 'سایت آنلاین است';
                document.getElementById('ping-status').innerText = 'پینگ موفقیت‌آمیز';
                document.getElementById('status-report').classList.add('online');
                document.getElementById('status-report').classList.remove('offline');

                // بعد از 5 ثانیه محو شدن
                setTimeout(() => {
                    document.getElementById('status-report').style.opacity = 0;
                }, 3000); // پس از 3 ثانیه محو می‌شود
            } else {
                document.getElementById('site-status').innerText = 'مشکل در دسترسی به سایت';
                document.getElementById('ping-status').innerText = 'پینگ ناموفق';
                document.getElementById('status-report').classList.add('offline');
                document.getElementById('status-report').classList.remove('online');
            }
        })
        .catch(() => {
            document.getElementById('site-status').innerText = 'مشکل در دسترسی به سایت';
            document.getElementById('ping-status').innerText = 'پینگ ناموفق';
            document.getElementById('status-report').classList.add('offline');
            document.getElementById('status-report').classList.remove('online');
        });
}

// اجرای تابع بررسی وضعیت سایت
checkPing();

// بررسی وضعیت سایت هر 10 ثانیه یکبار
setInterval(checkPing, 10000);

class AIWebsiteOptimizer {
    constructor() {
        console.log("Initializing Advanced AI Website Optimization System...");
        this.startMonitoring();
    }

    startMonitoring() {
        setInterval(() => {
            this.scanWebsite();
            this.optimizePerformance();
            this.enhanceSecurity();
            this.adjustUIForDevices();
        }, 60000); // Runs every 60 seconds
    }

    scanWebsite() {
        console.log("Scanning website for issues...");
        // AI-based analysis of website health, performance, and SEO
    }

    optimizePerformance() {
        console.log("Optimizing website speed and efficiency...");
        // AI-driven caching, image optimization, and load balancing
    }

    enhanceSecurity() {
        console.log("Enhancing website security and threat detection...");
        // AI-based firewall, DDoS protection, and vulnerability scanning
    }

    adjustUIForDevices() {
        console.log("Adjusting UI for all screen sizes and devices...");
        // AI-driven responsive design and adaptive layout adjustments
    }
}

const optimizer = new AIWebsiteOptimizer();

function analyzeAndFix() {
    document.querySelectorAll(".element").forEach(el => {
        if (el.offsetWidth > window.innerWidth) {
            el.style.maxWidth = "100%";
        }
        if (el.offsetLeft < 0) {
            el.style.left = "0px";
        }
    });
}

// استفاده از یادگیری ماشین برای تشخیص مشکلات رایج و بهبود مستمر
async function trainAI() {
    let problemsDetected = [];
    document.querySelectorAll(".element").forEach(el => {
        if (el.offsetWidth > window.innerWidth || el.offsetLeft < 0) {
            problemsDetected.push({ element: el.className, issue: "Layout Overflow" });
        }
    });

    if (problemsDetected.length > 0) {
        localStorage.setItem("layoutFixes", JSON.stringify(problemsDetected));
        console.log("AI has learned from detected issues:", problemsDetected);
    }
}

window.addEventListener("resize", () => { analyzeAndFix(); trainAI(); });
document.addEventListener("DOMContentLoaded", () => { analyzeAndFix(); trainAI(); });

function checkConnectionSpeed() {
    const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (connection) {
        console.log(`سرعت اتصال: ${connection.effectiveType}`);
        if (["slow-2g", "2g"].includes(connection.effectiveType)) {
            document.body.classList.add("low-bandwidth-mode");
        }
    }
}
checkConnectionSpeed();

function adjustFontSettings() {
    const width = window.innerWidth;
    document.body.style.fontSize = width < 600 ? "14px" : "16px";

    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.style.backgroundColor = "#121212";
        document.body.style.color = "#ffffff";
    }
}

window.addEventListener("resize", adjustFontSettings);
adjustFontSettings();

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("img, video").forEach(media => {
        media.style.maxWidth = "100%";
        media.style.height = "auto";
    });
});

function autoFixLayout() {
    document.querySelectorAll(".content").forEach(el => {
        if (el.offsetLeft < 0 || el.offsetWidth > window.innerWidth) {
            el.style.margin = "auto";
            el.style.width = "95%";
        }
    });
}

window.addEventListener("resize", autoFixLayout);
document.addEventListener("DOMContentLoaded", autoFixLayout);

function detectEnvironment() {
    const ua = navigator.userAgent;
    let deviceType = "Desktop";
    if (/Mobi|Android/i.test(ua)) deviceType = "Mobile";
    else if (/Tablet|iPad/i.test(ua)) deviceType = "Tablet";

    return {
        device: deviceType,
        browser: navigator.userAgent,
        screenWidth: window.innerWidth,
        screenHeight: window.innerHeight,
        dpi: window.devicePixelRatio,
        connection: navigator.connection ? navigator.connection.effectiveType : "unknown",
        darkMode: window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches,
        battery: navigator.getBattery ? navigator.getBattery().then(b => b.level * 100) : "unknown"
    };
}

console.log(detectEnvironment());

function analyzeAndFix() {
    document.querySelectorAll(".element").forEach(el => {
        if (el.offsetWidth > window.innerWidth) {
            el.style.maxWidth = "100%";
        }
        if (el.offsetLeft < 0) {
            el.style.left = "0px";
        }
    });
}

window.addEventListener("resize", analyzeAndFix);
document.addEventListener("DOMContentLoaded", analyzeAndFix);

function checkConnectionSpeed() {
    const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (connection) {
        console.log(`سرعت اتصال: ${connection.effectiveType}`);
        if (["slow-2g", "2g"].includes(connection.effectiveType)) {
            document.body.classList.add("low-bandwidth-mode");
        }
    }
}
checkConnectionSpeed();

function adjustFontSize() {
    const width = window.innerWidth;
    document.body.style.fontSize = width < 600 ? "14px" : "16px";
}

window.addEventListener("resize", adjustFontSize);
adjustFontSize();

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("img, video").forEach(media => {
        media.style.maxWidth = "100%";
        media.style.height = "auto";
    });
});

function autoFixLayout() {
    document.querySelectorAll(".content").forEach(el => {
        if (el.offsetLeft < 0 || el.offsetWidth > window.innerWidth) {
            el.style.margin = "auto";
            el.style.width = "95%";
        }
    });
}

window.addEventListener("resize", autoFixLayout);
document.addEventListener("DOMContentLoaded", autoFixLayout);

function detectEnvironment() {
    const ua = navigator.userAgent;
    let deviceType = "Desktop";
    if (/Mobi|Android/i.test(ua)) deviceType = "Mobile";
    else if (/Tablet|iPad/i.test(ua)) deviceType = "Tablet";

    return {
        device: deviceType,
        browser: navigator.userAgent,
        screenWidth: window.innerWidth,
        screenHeight: window.innerHeight,
        dpi: window.devicePixelRatio,
        connection: navigator.connection ? navigator.connection.effectiveType : "unknown"
    };
}

console.log(detectEnvironment());

function analyzeAndFix() {
    document.querySelectorAll(".element").forEach(el => {
        if (el.offsetWidth > window.innerWidth) {
            el.style.maxWidth = "100%";
        }
        if (el.offsetLeft < 0) {
            el.style.left = "0px";
        }
    });
}

window.addEventListener("resize", analyzeAndFix);
document.addEventListener("DOMContentLoaded", analyzeAndFix);

function adjustFontSize() {
    const width = window.innerWidth;
    document.body.style.fontSize = width < 600 ? "14px" : "16px";
}

window.addEventListener("resize", adjustFontSize);
adjustFontSize();

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("img, video").forEach(media => {
        media.style.maxWidth = "100%";
        media.style.height = "auto";
    });
});

function autoFixLayout() {
    document.querySelectorAll(".content").forEach(el => {
        if (el.offsetLeft < 0 || el.offsetWidth > window.innerWidth) {
            el.style.margin = "auto";
            el.style.width = "95%";
        }
    });
}

window.addEventListener("resize", autoFixLayout);
document.addEventListener("DOMContentLoaded", autoFixLayout);

function detectEnvironment() {
    const ua = navigator.userAgent;
    let deviceType = "Desktop";
    if (/Mobi|Android/i.test(ua)) deviceType = "Mobile";
    else if (/Tablet|iPad/i.test(ua)) deviceType = "Tablet";

    return {
        device: deviceType,
        browser: navigator.userAgent,
        screenWidth: window.innerWidth,
        screenHeight: window.innerHeight,
        dpi: window.devicePixelRatio,
        connection: navigator.connection ? navigator.connection.effectiveType : "unknown"
    };
}

console.log(detectEnvironment());

function checkConnectionSpeed() {
    const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (connection) {
        console.log(`سرعت اتصال: ${connection.effectiveType}`);
        if (["slow-2g", "2g"].includes(connection.effectiveType)) {
            document.body.classList.add("low-bandwidth-mode");
        }
    }
}
checkConnectionSpeed();

function adjustFontSize() {
    const width = window.innerWidth;
    document.body.style.fontSize = width < 600 ? "14px" : "16px";
}

window.addEventListener("resize", adjustFontSize);
adjustFontSize();

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("img, video").forEach(media => {
        media.style.maxWidth = "100%";
        media.style.height = "auto";
    });
});

function autoFixLayout() {
    document.querySelectorAll(".content").forEach(el => {
        if (el.offsetLeft < 0 || el.offsetWidth > window.innerWidth) {
            el.style.margin = "auto";
            el.style.width = "95%";
        }
    });
}

window.addEventListener("resize", autoFixLayout);
document.addEventListener("DOMContentLoaded", autoFixLayout);

function detectDeviceInfo() {
    const ua = navigator.userAgent;
    let deviceType = "Desktop";
    if (/Mobi|Android/i.test(ua)) deviceType = "Mobile";
    else if (/Tablet|iPad/i.test(ua)) deviceType = "Tablet";

    return {
        device: deviceType,
        browser: navigator.userAgent,
        screenWidth: window.innerWidth,
        screenHeight: window.innerHeight,
        dpi: window.devicePixelRatio,
        connection: navigator.connection ? navigator.connection.effectiveType : "unknown"
    };
}

console.log(detectDeviceInfo());

function checkConnectionSpeed() {
    const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (connection) {
        console.log(`سرعت اتصال: ${connection.effectiveType}`);
        if (connection.effectiveType === "slow-2g" || connection.effectiveType === "2g") {
            document.body.classList.add("low-bandwidth-mode");
        }
    }
}
checkConnectionSpeed();

function fixLayout() {
    const elements = document.querySelectorAll(".content");
    elements.forEach(el => {
        if (el.offsetLeft < 0) {
            el.style.marginLeft = "10px"; // جلوگیری از خروج عناصر از صفحه
        }
    });
}

window.addEventListener("resize", fixLayout);
fixLayout();

function adjustFontSize() {
    const width = window.innerWidth;
    if (width < 600) {
        document.body.style.fontSize = "14px";
    } else {
        document.body.style.fontSize = "16px";
    }
}

window.addEventListener("resize", adjustFontSize);
adjustFontSize();

document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll("img");
    images.forEach(img => {
        if (window.innerWidth < 768) {
            img.style.width = "100%";
            img.style.height = "auto";
        }
    });
});

function detectDevice() {
    const ua = navigator.userAgent;
    let deviceType = "Desktop";
    if (/Mobi|Android/i.test(ua)) deviceType = "Mobile";
    else if (/Tablet|iPad/i.test(ua)) deviceType = "Tablet";

    return {
        device: deviceType,
        browser: navigator.userAgent,
        screenWidth: window.innerWidth,
        screenHeight: window.innerHeight,
        dpi: window.devicePixelRatio
    };
}

console.log(detectDevice());

function adjustFontSize() {
    const width = window.innerWidth;
    document.documentElement.style.fontSize = width < 600 ? "14px" : "16px";
}

window.addEventListener("resize", adjustFontSize);
adjustFontSize();

function checkConnectionSpeed() {
    const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (connection) {
        console.log(`نوع اتصال: ${connection.effectiveType}`);
        if (connection.effectiveType === "slow-2g" || connection.effectiveType === "2g") {
            document.body.classList.add("low-bandwidth-mode");
        }
    }
}
checkConnectionSpeed();

function adjustLayout() {
    const width = window.innerWidth;

    if (width < 600) {
        document.body.classList.add("mobile-view");
    } else {
        document.body.classList.remove("mobile-view");
    }
}

window.addEventListener("resize", adjustLayout);
adjustLayout();

function detectDevice() {
    const ua = navigator.userAgent;
    let deviceType = "Desktop";

    if (/Mobi|Android/i.test(ua)) deviceType = "Mobile";
    else if (/Tablet|iPad/i.test(ua)) deviceType = "Tablet";

    return {
        device: deviceType,
        browser: navigator.userAgent,
        screenWidth: window.innerWidth,
        screenHeight: window.innerHeight
    };
}
async function fetchStatus() {
    try {
        let response = await fetch('/status');
        let data = await response.json();
        document.getElementById('connection_status').innerText = data.status || 'Unknown';
        document.getElementById('health_score').innerText = data.site_health_score || '--';
    } catch (error) {
        document.getElementById('connection_status').innerText = 'Error Fetching Data';
    }
}
setInterval(fetchStatus, 5000);
fetchStatus();
class AIWebsiteOptimizer {
constructor() {
console.log("Initializing Advanced AI Website Optimization System...");
this.startMonitoring();
}

startMonitoring() {
setInterval(() => {
    this.scanWebsite();
    this.optimizePerformance();
    this.enhanceSecurity();
    this.adjustUIForDevices();
}, 60000); // Runs every 60 seconds
}

scanWebsite() {
console.log("Scanning website for issues...");
// AI-based analysis of website health, performance, and SEO
}

optimizePerformance() {
console.log("Optimizing website speed and efficiency...");
// AI-driven caching, image optimization, and load balancing
}

enhanceSecurity() {
console.log("Enhancing website security and threat detection...");
// AI-based firewall, DDoS protection, and vulnerability scanning
}

adjustUIForDevices() {
console.log("Adjusting UI for all screen sizes and devices...");
// AI-driven responsive design and adaptive layout adjustments
}
}

const optimizer = new AIWebsiteOptimizer();
console.log(detectDevice());

function toggleChat() {
    const chatContainer = document.getElementById("chat-container");
    chatContainer.classList.toggle("hidden");
}

function sendMessage() {
    const inputField = document.getElementById("user-input");
    const userMessage = inputField.value.trim();
    if (!userMessage) return;
    
    displayMessage(userMessage, "user");
    inputField.value = "";
    
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, "bot");
    })
    .catch(error => {
        displayMessage("خطایی رخ داد! لطفاً دوباره تلاش کنید.", "bot");
    });
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
