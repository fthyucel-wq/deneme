import os
from dotenv import load_dotenv

# Environment değişkenlerini yükle
load_dotenv()

def chat_without_api():
    """API key olmadan basit sohbet asistanı (demo)"""
    print("=" * 50)
    print("🤖 Yapay Zeka Asistanı (Demo Modu)")
    print("=" * 50)
    print("Not: Bu demo modudur. OpenAI API key olmadan çalışır.")
    print("Asistanla sohbet etmek için yazın. Çıkmak için 'çık' yazın.\n")
    
    # Basit cevap veritabanı
    responses = {
        "merhaba": "Merhaba! Ben yapay zeka asistanıyım. Sana nasıl yardımcı olabilirim?",
        "adın ne": "Benim özel bir adım yok, bana Asistan diyebilirsin! 😊",
        "nasılsın": "Harika, teşekkür ederim! Senden nasılsın?",
        "saati kaç": "Şu anda tam saati bilmek için API key gerekli, ancak kendi saatini kontrol edebilirsin! 🕐",
        "joke": "Neden bilgisayar doktor olmak istedi? Çünkü virüs kovalamak istiyordu! 😄",
        "şaka": "İki yazılımcı ♾️ ve NULL arasında fark nedir? Sonsuz döngüde fark yoktur! 😆",
        "yardım": """
Yapabileceklerim:
- 💬 Seninle sohbet etmek
- 😂 Şaka anlatmak
- 📚 Bilgi vermek
- ❓ Sorularını cevaplamak

API key ekledikten sonra daha fazla şey yapabileceğim!
        """,
        "api key": """
API key eklemek için:
1. https://platform.openai.com/api-keys adresine git
2. Yeni bir API key oluştur
3. .env dosyasını aç
4. OPENAI_API_KEY=your_key_here şeklinde yapıştır
5. assistant.py'ı yeniden çalıştır

Daha sonra sınırsız imkanlar olacak! 🚀
        """,
    }
    
    while True:
        # Kullanıcı girdisi
        user_input = input("👤 Siz: ").strip().lower()
        
        # Çıkış kontrolü
        if user_input in ['çık', 'exit', 'quit']:
            print("\n👋 Görüşmek üzere!")
            break
        
        # Boş girdiye karşı kontrol
        if not user_input:
            print("Lütfen bir şeyler yazın.\n")
            continue
        
        # Cevap ara
        response = None
        
        # Tam eşleşme kontrol et
        if user_input in responses:
            response = responses[user_input]
        else:
            # Kısmi eşleşme kontrol et
            for key, value in responses.items():
                if key in user_input:
                    response = value
                    break
        
        # Eğer cevap bulunduysa göster
        if response:
            print(f"\n🤖 Asistan: {response}\n")
        else:
            print(f"""
🤖 Asistan: Bu soruya cevap vermek için OpenAI API key gerekli.
Şu anda demo modundayım ve sınırlı cevaplar verebiliyorum.

Deneyin: 'yardım', 'şaka', 'api key', 'merhaba'
""")

if __name__ == "__main__":
    chat_without_api()