import streamlit as st
from datetime import datetime

# --- 1. 앱 디자인 (스타일) ---
st.set_page_config(page_title="Soul Data", page_icon="🔮")

# 검은 배경에 네온 스타일 CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    h1 {
        color: #00FF94; /* 네온 그린 */
        text-align: center;
        font-family: sans-serif;
    }
    .stButton>button {
        background-color: #FF0055; /* 네온 핑크 */
        color: white;
        border-radius: 20px;
        width: 100%;
        border: none;
    }
    .result-box {
        border: 2px solid #00FF94;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
        background-color: #111;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 화면 구성 (UI) ---
st.title("SOUL DATA")
st.markdown("<h4 style='text-align: center; color: #888;'>The Blueprint of Your Fate</h4>", unsafe_allow_html=True)
st.write("---")

# 사용자 입력
name = st.text_input("Enter your Name")
col1, col2 = st.columns(2)
with col1:
    birth_date = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1))
with col2:
    birth_time = st.time_input("Time of Birth")

# --- 3. 로직 (임시 계산기) ---
def analyze_soul(year):
    # 간단한 예시 로직 (나중에 정밀한 만세력으로 교체 예정)
    elements = ["Metal", "Metal", "Water", "Water", "Wood", "Wood", "Fire", "Fire", "Earth", "Earth"]
    animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
    
    element = elements[year % 10]
    animal = animals[year % 12]
    return element, animal

# 분석 버튼
if st.button("ACCESS SOUL DATA"):
    if name:
        with st.spinner('Accessing Akashic Records...'):
            # 실제 계산 실행
            element, animal = analyze_soul(birth_date.year)
            
            # 결과 보여주기
            st.markdown(f"""
            <div class="result-box">
                <p style="color:#888;">Subject: {name}</p>
                <h2>{element} {animal}</h2>
                <p>Your hidden potential has been unlocked.</p>
                <hr style="border-color: #333;">
                <p style="font-size: 14px; color: #aaa;">
                You possess the energy of <b>{element}</b> combined with the spirit of the <b>{animal}</b>.
                This makes you a unique being in this universe.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("Analysis Complete.")
    else:
        st.warning("Please enter your name to proceed.")
