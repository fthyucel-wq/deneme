import os
from dotenv import load_dotenv
from openai import OpenAI

# Environment değişkenlerini yükle
load_dotenv()

# OpenAI istemcisini oluştur
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_assistant():
    """Basit sohbet asistanı"""
    print("=" * 50)
    print("🤖 Yapay Zeka Asistanı")
    print("=" * 50)
    print("Asistanla sohbet etmek için yazın. Çıkmak için 'çık' yazın.\n")
    
    # Konuşma geçmişi
    messages = [
        {
            "role": "system",
            "content": "Sen yardımcı, kibar ve bilgili bir yapay zeka asistanısın. Türkçe cevap ver."
        }
    ]
    
    while True:
        # Kullanıcı girdisi
        user_input = input("👤 Siz: ").strip()
        
        # Çıkış kontrolü
        if user_input.lower() in ['çık', 'exit', 'quit']:
            print("\n👋 Görüşmek üzere!")
            break
        
        # Boş girdiye karşı kontrol
        if not user_input:
            print("Lütfen bir şeyler yazın.\n")
            continue
        
        # Kullanıcı mesajını geçmişe ekle
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # OpenAI API'ye istek gönder
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            # Asistanın cevabı
            assistant_message = response.choices[0].message.content
            
            # Cevabı geçmişe ekle
            messages.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Cevabı göster
            print(f"\n🤖 Asistan: {assistant_message}\n")
            
        except Exception as e:
            print(f"\n❌ Hata: {str(e)}")
            print("Lütfen API key'inizi kontrol edin.\n")
            # Başarısız mesajı geçmişten kaldır
            messages.pop()

if __name__ == "__main__":
    chat_with_assistant()