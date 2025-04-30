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

## 🧠 사용 기술

| 분류        | 기술 스택                              | 설명 |
|-------------|------------------------------------------|------|
| 언어        | Python 3.10                              | 전체 모델 개발 및 앱 구현 |
| 딥러닝      | TensorFlow, Keras                        | LSTM 기반 예측 모델 학습 |
| 데이터 처리 | Pandas, NumPy                            | 기후 데이터 로딩 및 전처리 |
| 웹앱 UI     | Streamlit                                | 사용자 인터페이스 제공 |
| 시각화      | Matplotlib, Seaborn (Jupyter 단계)       | 분석 및 리포트용 시각화 |
| 모델 파일   | `.h5` 형식 (Keras SaveModel)             | 학습된 모델 저장 및 로드 |
| 입력데이터  | `All_Feature_Data.csv` (cp949 인코딩)   | 입력용 기후 데이터셋 |


---

---


