#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import openpyxl


# ### 엑셀 파일 생성하기
# 파일명, 시트명, 컬럼명을 정해줍니다.

# In[ ]:


#엑셀파일 생성
wb = openpyxl.Workbook("파일명.xlsx")        
ws = wb.create_sheet("시트명")             
ws.append(['브랜드','상품명','카테고리','정가','할인가','아이디','별점','피부정보','피부타입','피부고민','자극도'])  #컬럼명 제공


# In[ ]:


######################제공하는 코드 건드리지 마세요 #############################

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach',True)

#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# ### 올리브영 스킨케어 랭킹 링크를 main_url로 두고 5위까지 제품 상세 링크를 sub_url에 저장하기

# In[ ]:


main_url =

response = requests.get(main_url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

links = soup.select(" ") #빈칸채우기



#for반복문을 활용하여 5위까지 제품별 상세링크 sub_url에 저장
rank=

sub_url= []

for link in links:

    
    
    

time.sleep(1)

# 1위 인덱스 0,  2위 인덱스1, 3위 인덱스2, 4위 인덱스3, 5위 인덱스4


# ### 크롤링 함수 만들기
# 제품 상세 페이지에서 상단 제품정보(브랜드명,상품명,카테고리,정가,할인가)와  
# 하단의 리뷰고객 좌픅정보(아이디,별점,피부정보)와 우측정보(피부타입,피부고민,자극도)를 가져옵니다.  
# 위의 데이터를 엑셀에 계속 추가하는 함수를 만듭니다. 

# In[ ]:


def customer_info():

    for j in range(0,10,1):

        #브랜드
        try:
            brand = 
        except:
            brand ="없음"

        #상품명
        try:
            p_name =
        except:
            p_name="없음"

        #카테고리
        try:
            p_category = 
        except:
            p_category="없음"

        #정가
        try:
            price =
        except:
            price=0

        #할인가
        try:
            discount =
        except:
            discount=0

        #고객 아이디
        try:
            _id = 
        except:
            _id ="없음"

        #별점
        try:
            _star = 
        except:
            _star="없음"

        #고객 피부 정보
        try:
            _info = 
        except:
            _info = "없음"


        #피부 타입
        try:
            skin_type = 
        except:
            skin_type = "없음"
            
        #피부 고민
        try:
            skin_trouble = 
        except:
            skin_trouble = "없음"
        #자극도
        try:
            skin_irritation = 
        except:
            skin_irritation = "없음"
            
        #엑셀 데이터 쌓기
        ws.append([brand,p_name,p_category,price,discount,_id, _star, _info, skin_type, skin_trouble, skin_irritation])
        time.sleep(1)


# ### 웹페이지 해당 주소로 이동하여 크롤링함수를 실행하는 반복문을 만듭니다.
# 반복문에 들어가야 하는 것  
# 1. 리뷰버튼 클릭  
# 2. 화면 맨 아래까지 스크롤하기 (코드제공)
# 3. 10페이지 이하일 때 : 10페이지 크롤링 한 후 다음페이지 화살표 버튼 누르기 , 마지막 페이지인 경우 last_page==True
# 4. 11페이지부터 규칙을찾아 다음페이지로 이동하게 만들기, 마지막 페이지인 경우 last_page==True

# In[ ]:


#웹페이지 해당 주소 이동
for i in range(0,5):          #전체 제품을 한번에 크롤링하지 않고 나눠서 크롤링 할 경우 sub_url 인덱스 고려해서 range숫자 변경


    driver.implicitly_wait(5)  #웹페이지 로딩 될때까지 5초는 기다림
    driver.maximize_window()   #화면 최대화
    driver.get(sub_url[i])          
    time.sleep(3)


    #리뷰버튼 클릭
    rv = 
    rv.click()
    time.sleep(3)
    

    #리뷰 하단 끝까지 스크롤하는 함수 (빈칸없음.그대로 코드 사용가능)
    before_h = driver.execute_script("return window.scrollY")         #스크롤 전 높이
    #화면 맨아래까지 스크롤
    while True:
        driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

        time.sleep(1)

        #스크롤 후 높이
        after_h = driver.execute_script("return window.scrollY")

        #스크롤 값이 같으면 스크롤 멈춤
        if after_h == before_h:
            break
        before_h = after_h   

        

        
        
    last_page=False
    
    for k in range(1,101):  #100페이지 크롤링 한다고 했을 때 (상품당 최대 100페이지까지 있음)

        #마지막 페이지면 종료
        if last_page == True:
            break

        #페이지 숫자 10이하 일 때
        if k<11:
            try:    
                if k != 10:

                    

                elif k == 10:          #10페이지 크롤링 한 후에 다음페이지로 가는 화살표 버튼 클릭

                    
            except:
                   
                    

       #페이지 숫자 11이상 일 때  (규칙을 찾아 각 페이지 크롤링 후 다음 페이지로 이동하도록 코드 작성)        
        elif k>10 :

            try:



            except:
                   

                


# ### 크롤링한 결과를 엑셀에 저장 (상단에서 만든 엑셀 파일명고 동일하게)

# In[ ]:


wb.save("파일명.xlsx")       

