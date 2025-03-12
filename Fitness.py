import openai  
import streamlit as st
openai.api_key = ""


import streamlit as st
import openai  
import time




client = openai.OpenAI(api_key=openai.api_key)

# Fitness chatbot için sistem mesajı
system_message = """
Sen sadece fitness, antrenman, beslenme, kas geliştirme ve spor konularında uzman bir asistansın.
Genel veya alakasız sorulara cevap verme.
Eğer kullanıcı alakasız bir şey sorarsa, şu cevabı ver:
"Ben sadece fitness ve spor hakkında bilgi verebilirim."
"""

# Streamlit 
st.set_page_config(page_title="Fitness Chatbot 🏋️", page_icon="💪", layout="wide")

# CSS
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff1a1a;
    }
    </style>
""", unsafe_allow_html=True)

# 🎨 Yan Panel 
with st.sidebar:
    st.image("https://imgur.com/C0Om1W5.png", width=200)  # Fitness logo ekleyelim
    st.title("⚙️ Ayarlar")
    st.write("Buradan OpenAI modelini seçebilirsiniz.")
    model = st.radio("Model Seç:", ["gpt-3.5-turbo", "gpt-4"], index=1)
    st.write("Yalnızca fitness ile ilgili sorular sorabilirsiniz!")

# Sayfa Başlığı
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>💪 Fitness Asistanı</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🏋️‍♂️ Fitness ve Antrenman Danışmanınız</h3>", unsafe_allow_html=True)

# Kullanıcı girdileri
st.write("Merhaba! Bana antrenman, beslenme veya spor hakkında sorular sorabilirsin. 🔥")
user_input = st.text_input("Sorunu buraya yaz ve 'Gönder' butonuna bas:", "")

if st.button("🔥 Gönder"):
    if user_input:
        with st.spinner("Yanıt hazırlanıyor... ⏳"):
            time.sleep(1)  # Simüle edilmiş gecikme

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content

        # Mesajı chat formatı
        st.markdown(f"""
        <div style="background-color:#5b5b5b;padding:15px;border-radius:10px;margin:10px 0;">
        <b>🤖 Fitness Bot:</b> {answer}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Lütfen bir soru girin!")



