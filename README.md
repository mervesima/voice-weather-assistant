# voice-weather-assistant
OpenWeatherMap API ve Python kullanarak, anlık hava durumunu sesli olarak raporlayan akıllı asistan.
# 🌦️ Sesli Hava Durumu Asistanı

Bu Python projesi, kullanıcının sesli veya yazılı olarak belirttiği şehrin anlık hava durumu bilgilerini canlı API üzerinden çeken ve kullanıcıya sesli olarak yanıt veren bir asistan uygulamasıdır.

## 🌟 Öne Çıkan Özellikler
- **Canlı Veri:** OpenWeatherMap API entegrasyonu ile dünyanın her yerinden anlık veri çekimi.
- **Sesli Yanıt (TTS):** `gTTS` kütüphanesi ile hava durumu bilgisini doğal bir insan sesiyle seslendirme.
- **Akıllı Tavsiyeler:** Hava durumuna göre (Yağmurlu, Karlı, Çok Sıcak) kullanıcıya kıyafet veya aktivite tavsiyesi verme.

## 🛠️ Teknolojiler
- **Python 3.x**
- **Requests:** API sorguları için.
- **gTTS (Google Text-to-Speech):** Ses sentezleme için.
- **Pygame / Playsound:** Ses dosyalarını oynatmak için.

## 🚀 Çalıştırma
1. `pip install requests gTTS pygame` komutu ile kütüphaneleri kurun.
2. OpenWeatherMap üzerinden aldığınız API anahtarını ilgili alana ekleyin.
3. Uygulamayı çalıştırın ve şehrinizi söyleyin!
