import requests
from gtts import gTTS
import os
import pygame
import time
from datetime import datetime 

def asistan_konus(metin):
    print(metin)
    try:
        tts = gTTS(text=metin, lang='tr')
        dosya_adi = "asistan_ses.mp3"
        tts.save(dosya_adi)
        pygame.mixer.init()
        pygame.mixer.music.load(dosya_adi)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.quit()
        if os.path.exists(dosya_adi):
            os.remove(dosya_adi)
    except Exception as e:
        print(f"Ses hatası: {e}")

def tarih_saat_getir():
    """Şu anki tarih ve saat bilgisini Türkçe formatta hazırlar."""
    simdi = datetime.now()
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
    aylar = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
    
    gun_adi = gunler[simdi.weekday()]
    ay_adi = aylar[simdi.month]
    
    tarih_metni = f"Bugün {simdi.day} {ay_adi}, günlerden {gun_adi}. Saat şu an {simdi.hour} {simdi.minute}."
    return tarih_metni

def tavsiye_olustur(sicaklik, durum_kodu):
    tavsiye = ""
    if sicaklik < 0:
        tavsiye += "Dışarısı dondurucu, en kalın montunu giymelisin. "
    elif 0 <= sicaklik < 12:
        tavsiye += "Hava oldukça soğuk, sıkı giyinmeyi unutma. "
    elif 12 <= sicaklik < 20:
        tavsiye += "Hava biraz serin, üzerine bir ceket veya hırka alsan iyi olur. "
    elif 20 <= sicaklik < 28:
        tavsiye += "Hava gayet güzel, bir tişört yeterli olacaktır. "
    else:
        tavsiye += "Hava oldukça sıcak, bol su içmeyi unutma. "

    if 200 <= durum_kodu < 600:
        tavsiye += "Ayrıca dışarı çıkarken yanına mutlaka bir şemsiye al."
    return tavsiye

def hava_durumu_baslat():
    api_anahtari = "BURAYA_API_ANAHTARINIZI_YAZIN" 
   
    zaman_bilgisi = tarih_saat_getir()
    asistan_konus(f"Merhaba! {zaman_bilgisi} Hava durumu asistanı hizmetinizde. Hangi şehri öğrenmek istersiniz?")
   

    while True:
        sehir = input("\nŞehir (Çıkmak için 'çıkış'): ").strip()
        if sehir.lower() == "çıkış":
            asistan_konus("Görüşmek üzere, harika bir gün dilerim.")
            break
        if not sehir: continue

        url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_anahtari}&units=metric&lang=tr"
        
        try:
            cevap = requests.get(url)
            veri = cevap.json()

            if cevap.status_code == 200:
                sicaklik = int(veri['main']['temp'])
                durum = veri['weather'][0]['description']
                durum_kodu = veri['weather'][0]['id']
                
                tavsiye_mesaji = tavsiye_olustur(sicaklik, durum_kodu)
                
                print("\n" + "—"*40)
                print(f"📍 {sehir.upper()} | {sicaklik}°C")
                print(f"💡 {tavsiye_mesaji}")
                print("—"*40)

                tam_mesaj = f"{sehir} şehrinde hava {durum}. Sıcaklık {sicaklik} derece. {tavsiye_mesaji}"
                asistan_konus(tam_mesaj)
            else:
                asistan_konus(f"{sehir} isminde bir yer bulamadım.")
        except:
            asistan_konus("İnternet bağlantımda bir sorun var.")

if __name__ == "__main__":
    hava_durumu_baslat()