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

| 분류          | 기술 스택 / 도구                            | 설명 |
|---------------|----------------------------------------------|------|
| 언어          | Python 3.10                                  | 전체 모델 개발 및 웹앱 구현 |
| 딥러닝        | TensorFlow, Keras                            | LSTM 기반 예측 모델 학습 |
| 모델 구조     | LSTM (1D sequence input)                     | 시계열 기후 데이터를 위한 순환 신경망 구성 |
| 모델 저장     | `.h5` (Keras SaveModel 형식)                 | 학습된 모델 저장 및 추론에 사용 |
| 데이터 처리   | Pandas, NumPy                                | 결측값 대체, 평균값 처리, 슬라이더 UI 입력 적용 |
| 입력 데이터   | All_Feature_Data.csv (cp949 인코딩)         | 날짜 기반 기후 변수 데이터셋 |
| 전처리        | datetime, 평균 보정, 상위 변수 추출          | 사용자 입력 없이도 자동 처리 가능 |
| 웹앱 UI       | Streamlit                                    | 실시간 예측 결과 출력 웹 인터페이스 |
| 시각화 도구   | Matplotlib, Seaborn                          | Jupyter 기반 시각적 분석용 |
| 실행 도구     | Streamlit CLI, Jupyter Notebook              | 로컬 앱 실행 및 분석 환경 |
| 개발 환경     | VSCode, Windows 11 / Ubuntu 20.04            | 프로젝트 개발 및 테스트 환경 |
| 버전 관리     | GitHub                                       | 프로젝트 형상 관리 및 배포 |

---

## 🧪 모델 예측 성능 평가

모델의 예측 정확도는 다음과 같은 주요 회귀 평가 지표들을 기준으로 측정하였습니다:

| 지표   | 값       | 설명 |
|--------|----------|------|
| **RMSE** | 5.8725   | 비교적 낮은 값으로, 예측값과 실제값 간 오차가 크지 않음을 의미 |
| **MAE**  | 5.0258   | RMSE와 유사한 수준으로, 예측값의 평균적인 오차가 작음을 의미 |
| **R²**   | 0.9554   | 1에 가까운 값으로, 모델이 데이터를 잘 설명하고 있음을 의미 |
| **MAPE** | 1.9536   | 매우 낮은 백분율 오차로, 예측 정확도가 매우 높음을 의미 |

> 이 결과는 테스트셋에 대한 성능 기준이며, 모델이 일반화된 패턴을 잘 학습했음을 보여줍니다.

---
## 추가 섷명

> 본 프로젝트는 모델 구조부터 데이터 전처리, UI 구성까지 전 과정을 Python 기반으로 구현했으며,  
Streamlit을 활용해 누구나 쉽게 예측 모델을 실행하고 결과를 확인할 수 있도록 설계되었습니다.  
CSV 파일은 날짜 기반 데이터이며, 사용자 입력이 없는 변수는 평균값으로 자동 처리됩니다.

---
📘 참고 자료
NASA Sea Level Data: https://sealevel.nasa.gov

NOAA Climate Data: https://www.climate.gov

Keras LSTM Guide: https://keras.io/api/layers/recurrent_layers/lstm/
---
🙋 프로젝트 담당자
이름: 최주철

GitHub: https://github.com/Joo-Cheol/-DeepAI-sealevel-rise-prediction

email: wnrb15@naver.com




