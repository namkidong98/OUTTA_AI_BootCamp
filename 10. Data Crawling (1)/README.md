## Robots.txt
- 웹 사이트 및 웹 페이지를 수집하는 로봇들의 무단 접근을 방지하기 위해 만들어진 로봇 배제 표준/국제 권고안
- 일부 스팸 봇이나 악성 목적을 지닌 가짜 클라이언트 로봇은 웹 사이트에 진짜 클라이언트처럼 접근
- 무단으로 웹 사이트 정보를 긁어가거나, 웹 서버에 부하를 줌 -> 이런 로봇들의 무분별한 접근을 통제하기 위해 마련
- "기존 사이트의 URL/robots.txt"로 확인할 수 있다
  
ex) www.danawa.com/robots.txt  

![image](https://github.com/namkidong98/OUTTA_AI_BootCamp/assets/113520117/66b8d96a-0078-41a2-8fb5-081876af5c84)

<br>

## User agent
- 웹 서버에 요청을 보내도 요청을 거부 당하는 경우 발생 -> 무단 봇으로 짐작하고 웹 서버에서 접근을 막는 것
- 우리가 스팸 봇이 아니라 사람이라는 것을 브라우저에게 알려줘야 함
-> 이때 브라우저에게 전달하는 것이 사용자 에이전트 정보

<br>

## 정적 웹 크롤링
### 헤더가 필요하지 않는 경우
```python
import requests               # HTTP 요청을 보내고 응답을 받는 데 사용되는 라이브러리
from bs4 import BeautifulSoup # HTML 및 XML 문서를 파싱하고 검색하거나 데이터 추출을 위한 라이브러리
import re                     # 정규표현식을 처리하는 라이브러리

#1. 링크를 request.get으로 가져오기 (header가 필요한 경우 headers 입력)
res = requests.get("https://www.gmarket.co.kr/n/best")

# res         : 한 번 res에 저장되면 select와 같은 처리를 할 때 해당 시점의 데이터를 기반으로 값을 반환한다(그 사이에 해당 사이트가 변경되어도 반영 X)
# res.content : 연결된 res를 통해 정보를 가져왔지만 parsing이 수행되기 이전이라 파악하기 어려운 상태의 데이터이다


#2. BeautifulSoup을 이용해 파싱하기
soup = BeautifulSoup(res.content, 'html.parser') # parsing을 통해 보다 파악하기 쉬운 형태의 데이터로 바뀌었다
```

<br>

### 헤더가 필요한 경우(User-Agent로 인식되도록 하여 접근 거부를 회피)
```python
# 헤더 없이 request.get을 실행하고 BeautifulSoup으로 파싱한 soup를 실행했을 때
# "This page can't be displayed. Contact support for additional information"이라는 표현이 나타나면
# soup으로 페이지의 데이터가 크롤링되지 않았음을, 접근이 거부되었음을 확인할 수 있다 --> 헤더가 필요한 상황

#header 입력
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

res = requests.get('https://danawa.com/', headers = headers)
soup = BeautifulSoup(res.content, 'html.parser')
```

<br>

### BeautifulSoup의 함수
- **soup.select_one(' selector 복사한 부분 ')** : 주어진 것과 매칭되는 데이터 하나만 추출한다
  
- **soup.select(' selector 복사한 부분 ')** : 주어진 것과 매칭되는 데이터 모두를 추출해 리스트 형태로 반환한다

- **item.text** : select로 추출해낸 리스트의 아이템에서 text만 추출한다

- **item.get_text()** : item.text와 동일하게 text만 추출한다

<br>

### re의 함수 (정규 표현식)
- **re.match( " 정규표현식 ", 문자열 )** : 문자열 처음부터 정규식과 매칭되는 패턴을 찾아서 반환

- **re.search( " 정규표현식 ", 문자열 )** : 문자열 전체를 검색해서 정규식과 매칭되는 패턴을 찾아서 반환

- **re.split( " 정규표현식 ", 문자열 )** : 찾은 정규표현식 패턴 문자열을 기준으로 문자열을 분리

- **re.sub( " 정규표현식 ", 문자열 )** : 찾은 정규표현식 패턴 문자열을 다른 문자열로 변경

- **re.findall( " 정규표현식 ", 문자열 )** : 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 반환
```
re.findall("\d.*원", "할인가 4,920원 2%")    # 정규표현식에서 'd'로 정수를 받고 
                                            # '.'으로 any 
                                            # '*'로 앞에 위치한, any를 뜻하는 '.'이 0이상 있다가
                                            # 끝에 '원'으로 끝나는 부분을 catch 한다
# 결과값: ['4,920원']
```
