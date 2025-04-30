import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# 저장된 모델 로드
model = load_model('trained_model.h5')

# 데이터 불러오기
df = pd.read_csv("dataset/All_Feature_Data.csv", encoding='cp949')

# 결측치 처리 (결측값을 0으로 대체)
df.fillna(0, inplace=True)

# 날짜(Date) 컬럼에서 개월(Month) 정보 추출
df['Date'] = pd.to_datetime(df['Date'])  # 날짜 형식으로 변환
df['Month'] = df['Date'].dt.month  # 개월 단위 데이터 추출
# 숫자형 데이터만 선택하여 평균값 계산 (GMSL과 Date 열 제외)
numeric_cols = df.select_dtypes(include=[np.number]).columns
numeric_cols = numeric_cols.drop(["GMSL", "Month"], errors="ignore")  # GMSL과 Month 제거
df_mean = df[numeric_cols].mean()

# 상위 숫자형 열 선택
top_10_cols = numeric_cols[:10]

# 나머지 숫자형 열의 평균값 설정
default_values = {col: df_mean[col] for col in numeric_cols if col not in top_10_cols}

# Streamlit 웹앱 시작
st.title("해수면 상승 예측")
st.write("상위 10개의 특성을 입력하세요. 개월 데이터는 슬라이더로 입력하며, GMSL은 예측됩니다.")

# 사용자 입력값을 저장할 딕셔너리
inputs = {}

# 개월 데이터 입력받기 (1월부터 12월)
month = st.sidebar.slider("Month (개월)", min_value=1, max_value=12, value=6)  # 기본값: 6월
inputs["Month"] = month

# 사이드바로 상위 10개 컬럼 슬라이더 입력받기
st.sidebar.header("상위 10개 변수 입력")
for col in top_10_cols:
    min_val = float(df[col].min())
    max_val = float(df[col].max())
    mean_val = float(df_mean[col])
    inputs[col] = st.sidebar.slider(f"{col}", min_value=min_val, max_value=max_val, value=mean_val)

# 나머지 숫자형 열은 평균값으로 자동 설정
for col, mean_val in default_values.items():
    inputs[col] = mean_val

# 입력값을 배열로 변환
input_values = np.array([list(inputs.values())])

# 모델 입력 형식에 맞게 변환 (LSTM 입력 형태로 reshape)
input_values = input_values.reshape(1, input_values.shape[1], 1)

# 버튼 추가 및 예측 결과 출력
if st.button("예측 실행"):
    # 예측 결과 생성
    prediction = model.predict(input_values)

    # 결과 출력
    st.subheader("예측 결과")
    st.write(f"예측된 GMSL(해수면 상승량): {prediction[0][0]:.2f}")
