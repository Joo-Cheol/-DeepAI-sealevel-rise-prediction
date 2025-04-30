# 🌊 해수면 상승 예측 딥러닝 모델 (Streamlit 웹앱)

이 프로젝트는 딥러닝 모델을 기반으로 기후 데이터를 분석하여  
**GMSL (Global Mean Sea Level, 전 지구 평균 해수면)** 상승률을 예측하는 Streamlit 기반 웹 애플리케이션입니다.  
LSTM 모델과 전처리된 데이터셋을 이용해 예측을 수행하며, 사용자가 슬라이더로 직접 주요 기후 변수들을 조정하여 예측 결과를 실시간 확인할 수 있습니다.

---

## 📂 폴더 구조

DEEPLEARNING_CJC/ ├── dataset/ │ └── All_Feature_Data.csv # 예측 입력 데이터셋 (cp949 인코딩) ├── report/ │ ├── sea_report.html # 해수면 상승 분석 리포트 (HTML) │ └── [딥러닝 기반] ...hwp # 프로젝트 기술 보고서 (한글) ├── DeepLearning123.ipynb # 모델 개발 및 테스트용 노트북 ├── DeepLearning123.py # Streamlit 기반 예측 웹앱 ├── trained_model.h5 # 학습된 LSTM 모델 파일 ├── 딥러닝 산출물_20250325(최주철v0.1).pptx # 발표용 PPT
