## 동적 웹 크롤링

### Selenium 
웹 애플리케이션을 자동으로 테스트하거나 웹페이지를 조작하기 위한 도구로 사용되는 프레임워크   
웹 브라우저를 제어하고 웹페이지 요소에 접근하여 상호작용하는 데에 사용   

```
from selenium import webdriver
          # 웹 드라이버(ex. Chrome)을 사용하기 위한 모듈, 다양한 브라우져를 지원

from selenium.webdriver.common.by import By
          # find_element 메소드에서 요소를 찾는 방법을 지정하기 위한 By 클래스

from selenium.webdriver.common.keys import Keys
          # 키보드의 특수 키를 나타내는 상수들을 제공, 웹 페이지 내에서 특수 키 이벤트를 시뮬레이트

from selenium.webdriver.chrome.service import Service
          # 웹 드라이버 서비스를 설정하고 관리
```

<br>

### WebDriver 관련 함수
- **driver = webdriver.Chrome('경로')** : ChromeDriver의 경로를 지정하고, WebDriver 인스턴스를 생성

- **driver.get(' URL ')** : Webdriver 객체가 메소드 get을 통해 URL을 탐색하여 웹 페이지를 연다

- **driver.quit()** : Webdriver를 종료하여 브라우져 창을 닫는다

- **driver.implicitly_wait( seconds )** : 웹 요소가 나타날 때까지 최대 지정한 시간만큼 대기하도록 설정
  <br> cf) import time, time.sleep( seconds ) : 그냥 지정한 시간만큼 대기하도록 설정
  
- **driver.maximize_window()** : 웹 드라이버로 연 페이지의 화면 최대화

<br>

### Keys 관련 함수
- **search_box = driver.find_element(By.NAME, ' input 요소의 name ')** : 검색어를 입력할 수 있는 input 요소를 찾는다

- **search_box.send_keys(' input ')** : input 요소(지금은 search_box)에 원하는 입력을 보냄, 그러나 단 입력에 그치므로 Keys.RETURN과 함께 쓰여야 한다

- **search_box.send_keys(Keys.RETURN)** : Keys.RETURN은 엔터 키를 나타내는 상수, send_keys() 메소드로 엔터 키를 시뮬레이트하고 검색을 실행

<br>

### find_element(s)
find_element 메소드는 옵션으로 특정 클래스(ex. By.Name)를 통해 웹페이지의 요소를 찾는다     
옵션으로 넣는 특정 클래스에 따라 요소를 찾는 방법을 지정할 수 있다   
find_element는 하나의 요소만 찾는 반면 find_elements는 해당하는 모든 요소를 찾는다

- **element = driver.find_element(By.ID, "element-id")** : 요소의 'id' 부분을 통해 검색 

- **element = driver.find_element(By.NAME, "element-name")** : 요소의 'name' 부분을 통해 검색

- **element = driver.find_element(By.CLASS_NAME, "element-class")** : 요소의 'class_name'을 통해 검색

- **element = driver.find_element(By.CSS_SELECTOR, "div.element-class")** : 요소의 'selector 복사된 내용'을 통해 검색
