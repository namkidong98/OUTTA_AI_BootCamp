## 프로젝트명 : 이커머스 프로젝트  

### 목표
올리브영 스킨케어 판매랭킹 100개 제품의 리뷰를 바탕으로 별점을 예측하고 유사한 제품을 추천하는 프로그램을 만든다  
### 프로젝트 기간
2023.08.13 ~ 2023.08.20
### 조원
2023 OUTTA AI BootCamp 데이터반 55조: 남기동, 고정훈, 최서희, 유지우

<br>

## 프로젝트 코드 요약
### 1. Data_Crawling
  1. BeautifulSoup을 이용한 정적 웹페이지 크롤링으로 판매 랭킹 상위 5개 제품의 링크를 저장한다
  2. 각각의 제품에 대해 100개의 리뷰로부터 데이터를 크롤링하는 customer_info() 함수를 작성한다
  3. Selenium 라이브러리를 활용한 동적 웹 크롤링으로 리뷰 페이지를 자동으로 넘겨가며 customer_info() 함수로 데이터를 크롤링한다
  4. 저장한 데이터를 엑셀 파일("After Crawling.xlsx")로 저장한다

### 2. Data_Preprocessing
  1. 결측값이 많은 행과 열을 제거하고 정가, 할인가의 필요 정보를 추출하고 자료형을 변경한다
  2. 기존 열(column)의 데이터를 세분화하고 상품명을 단순화한다
  3. 범주형 데이터를 수치형 데이터로 변환하기 위해 직접 함수를 작성하여 Label Encoding을 수행한다
  4. 범주형 데이터를 수치형 데이터로 변환하기 위해 get_dummies를 이용하여 One-Hot Encoding을 수행한다
  5. 전처리가 완료된 데이터 프레임을 엑셀 파일("After Data_Preprocessing.xlsx")로 저장한다
     
### 3. Product_Rating Prediction
  1. 불균형한 데이터를 SMOTE를 활용하여 sampling하고 StandardScaler로 scaling한다
  2. Grid Search로 최적의 파라미터를 찾아 Random Forest 모델을 훈련시키고 평가지표 함수로 성능을 확인한다
  3. 유사한 방식으로 KNN 모델을 훈련시키고 평가지표 함수로 성능을 확인한다

### 4. Recommend System 
  1. product_id를 기준으로 유저 데이터와 제품 데이터를 병합한다
  2. pivot_table을 활용하여 각 유저가 제품에 남긴 평점들로 이루어진 데이터 프레임을 만든다
  3. 2번의 데이터 프레임을 기반으로 cosine_similarity를 이용하여 유저 간 유사도를 계산한다
  4. 입력한 아이디의 유저와 비슷한 유저가 만족한 제품 추천하는 함수 만든다

