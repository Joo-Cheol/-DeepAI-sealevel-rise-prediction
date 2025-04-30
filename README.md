# 🌊 Sea Level Rise Prediction with Deep Learning

> 딥러닝 모델을 이용하여 전 지구 평균 해수면 상승률(GMSL)을 예측하는 Streamlit 기반 웹 애플리케이션입니다.

---

## 📌 프로젝트 개요

이 프로젝트는 전 세계 기후 데이터를 기반으로 LSTM 모델을 학습하여  
미래의 해수면 상승량(GMSL)을 예측하는 웹 서비스를 제공합니다.

- 기후 변수 입력 → 실시간 GMSL 예측
- 상위 10개 변수는 슬라이더로 직접 입력
- 나머지 변수는 자동 평균값 보정
- Streamlit으로 손쉽게 웹 실행

---

## 📸 실행 화면 예시

### ▶ 앱 입력 화면

![입력화면 예시](https://raw.githubusercontent.com/Joo-Cheol/-DeepAI-sealevel-rise-prediction/main/images/app_input.png)

### ▶ 예측 결과 출력

![결과화면 예시](https://raw.githubusercontent.com/Joo-Cheol/-DeepAI-sealevel-rise-prediction/main/images/app_result.png)

> 위 이미지는 Streamlit 앱 실행 결과 예시입니다.

---

## 🚀 실행 방법

### 1. 환경 설정
```bash
pip install streamlit tensorflow pandas numpy
