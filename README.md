# 🌊 Sea Level Rise Prediction with Deep Learning

![Project Cover](images/cover.png)

> 예측 모델을 통해 미래 해수면 상승률(GMSL)을 예측하는 딥러닝 기반 Streamlit 웹 애플리케이션입니다.

---

## 📖 프로젝트 소개

본 프로젝트는 전 세계 기후 데이터를 바탕으로 해수면 상승(GMSL)을 예측하기 위해  
LSTM 기반 딥러닝 모델을 설계하고, 사용자 인터페이스로 Streamlit 웹앱을 제공하는 프로젝트입니다.

- ✅ 기후 변수 기반 예측
- ✅ 월(Month) 슬라이더 및 상위 10개 변수 수동 입력
- ✅ 학습된 모델(`.h5`)로 실시간 예측
- ✅ 웹 앱 실행만으로 바로 예측 가능

---

## 🚀 Streamlit 앱 실행 방법

```bash
pip install streamlit tensorflow pandas numpy
streamlit run DeepLearning123.py
