import streamlit as st
from datetime import date
import soul_db  # 우리가 방금 만든 60갑자 DB 불러오기

# --- 설정 및 스타일 ---
st.set_page_config(page_title="Soul Data", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #E0E0E0; }
    h1 { color: #00FF94; text-shadow: 0 0 10px #00FF94; font-family: 'Courier New'; }
    .stButton > button { 
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        color: black; font-weight: bold; border: none; padding: 15px; width: 100%; font-size: 18px;
    }
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #333;
        border-top: 5px solid #00FF94;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin-top: 30px;
    }
    .korean-text { color: #555; font-size: 14px; margin-bottom: 5px;}
    .big-name { font-size: 40px; font-weight: bold; color: #fff; margin: 10px 0; }
    .keywords { color: #00FF94; font-size: 16px; letter-spacing: 1px; margin-bottom: 20px; }
    .desc-text { font-size: 16px; line-height: 1.6; color: #ccc; text-align: left; background: #111; padding: 20px; border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)

# --- 메인 화면 ---
st.title("SOUL DATA")
st.caption("Accessing the 60 Ancient Codes of Destiny...")

with st.container():
    name = st.text_input("YOUR NAME")
    b_date = st.date_input("BIRTH DATE", min_value=date(1920, 1, 1), value=date(2000, 1, 1))

    if st.button("DECODE MY SOUL"):
        if name:
            with st.spinner('Calculating 60 Pillars Algorithm...'):
                
                # [핵심 로직] 생년월일 -> 60갑자 인덱스(0~59) 변환
                # 기준일: 1900년 1월 1일 = 갑술일(Gap-Sul, 인덱스 10)
                base_date = date(1900, 1, 1)
                days_passed = (b_date - base_date).days
                
                # 60갑자는 60일마다 반복됨.
                # 1900.1.1이 인덱스 10번이었으므로, (경과일수 + 10) % 60 하면 오늘의 인덱스가 나옴
                soul_index = (days_passed + 10) % 60
                
                # DB에서 데이터 가져오기
                data = soul_db.get_60_pillar_data(soul_index)
                
                # 결과 출력
                st.markdown(f"""
                <div class="result-card">
                    <div class="korean-text">SOUL CODE #{soul_index}</div>
                    <div class="big-name">{data['name']}</div>
                    <div class="keywords">{'  •  '.join(data['keywords'])}</div>
                    <div class="desc-text">{data['desc']}</div>
                    <br>
                    <p style="color:#666; font-size:12px;">Capture this screen & Share</p>
                </div>
                """, unsafe_allow_html=True)
                
        else:
            st.error("Please enter your name to verify identity.")

# --- 푸터 ---
st.write("---")
st.markdown("<p style='text-align:center; color:#444;'>Soul Data Project © 2025</p>", unsafe_allow_html=True)
