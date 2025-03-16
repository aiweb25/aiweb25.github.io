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

// scripts.js
document.getElementById("optimizeButton").addEventListener("click", function() {
    document.getElementById("status").innerText = "در حال انجام بهینه‌سازی...";
    
    // ارسال درخواست به سرور برای اجرای بهینه‌سازی
    fetch("/optimize_website", {
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

const express = require('express');
const app = express();
const port = 3000;

// مسیر سرو کردن فایل‌های استاتیک سایت
app.use(express.static('public'));

// روت اصلی
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

// شروع سرور در پورت 3000
app.listen(port, () => {
  console.log(`Server is running at http://127.0.0.1:${port}`);
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