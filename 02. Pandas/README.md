### Series 객체(object) 생성
- **obj = pd.Series(data, index = )** : data를 index와 연결지어 Series 객체 생성 (list, tuple, dictionary, ndarray 가능)

### Series 속성(attribute) 확인
- **obj.index** : Series 객체의 인덱스를 반환

- **obj.values** : Series 객체의 데이터를 반환

- **obj.isnull()** : Series 객체의 각 key(index)마다 결측치(NaN)이 있으면 True로 없으면 False로 반환

- **obj.notnull()** : isnull의 반대로 bool을 반환

### Series 데이터 선택
- **obj[ index명 ]** : 해당 인덱스 명의 value를 반환
    <br> cf) obj [ [ index1, index2, ... ] ] : 여러 개의 인덱스를 쓸 때는 리스트로 묶어서 사용

- **obj.loc[ index명 ]** : 해당 인덱스명의 value를 반환 (슬라이싱도 가능)

- **obj.iloc[ index number ]** : 해당 인덱스의 value를 반환 (슬라이싱도 가능)

### Series 데이터 연산
- **obj.sum(), obj.mean()** : 집계 함수 사용 가능

- **obj1 + obj2** : 같은 index명의 value들을 더한다 (결측치가 하나라도 있으면 결과도 결측치가 된다)

- **obj1.add(obj2, fill_value = 숫자)** : 결측치에 원하는 숫자를 기입한 후 연산을 수행한다


### DataFrame 속성 확인
- **df.info()** : 데이터 프레임의 행과 열 개수, 결측치 개수, dtype 등의 정보를 알려줌

- **df.columns** : 데이터 프레임의 column들의 이름을 list로 반환

- **df.index** : 데이터 프레임의 인덱스를 반환

- **df.head( 숫자 )**, **df.tail( 숫자 )** : 데이터 프레임의 상위 혹은 하위 지정한 숫자의 열을 보여줌(default 5개)

- **df.isnull()**, **df.isna()** : 데이터 프레임의 원소마다 결측치이면 True를 담은 새로운 데이터 프레임을 반환
    <br> cf) df.isnull().sum(axis = 0) : 데이터 프레임을 열 기준으로(axis=0) 결측치 개수를 보여줌
    <br> cf) df.notnull(), df.notna : 결측치이면 False, 결측치가 아니면 True를 담은 새로운 데이터 프레임을 반환

- **df.fillna('결측치 채울 값')** : 데이터 프레임 내의 결측치를 특정 값으로 채워 넣는다

- **df.dropna()** : 데이터 프레임 내의 결측치가 포함된 행을 삭제한다

### DataFrame 데이터 선택
- **df.set_index('특정 column명', inplace=True)** : 특정 column을 데이터 프레임의 index로 설정하고 inplace=True옵션으로 원본 데이터에 반영

- **df.loc['row 이름'], df.iloc[row 번호]** : 데이터 프레임의 특정 행(row)를 선택
    <br> cf) df.loc[ [ 'row1', 'row2' ] ] : row 여러 개를 선택할 때는 리스트로 묶어서 인자로 주어야 한다
    
- **df['column 이름']** : 데이터 프레임의 특정 열(column)을 선택
    <br> cf) df[ df['column'] == 'XXX' ] : 이처럼 df[] 안에 조건을 넣어서 해당 조건에 만족하는 부분만 새로운 데이터 프레임으로 반환 가능

- **df.loc['행 이름', '열 이름']** : 데이터 프레임의 행과 열을 선택

- **df.iloc[행 번호, 열 번호]** : 데이터 프레임의 행과 열을 선택

- **df['열 이름'][행 번호]** : 데이터 프레임의 행과 열을 선택

### DataFrame 데이터 수정
- **df.loc['새로운 행 이름'] = 데이터 값** : 데이터 프레임에 행(row)을 추가

- **df['새로운 열 이름'] = 데이터 값** : 데이터 프레임에 열(column)을 추가

- **df.drop(행 이름, axis = 0)** : 데이터 프레임의 특정 행(row)를 삭제

- **df.drop(열 이름, axis = 1)** : 데이터 프레임의 특정 열(column)을 삭제

- **df.replace( {dictionary} )** : 데이터 프레임의 특정 열 안에서 dictionary에 따라 값을 변환
    <br> cf) df['Legendary'].replace({True : 1, False : 0}, inplace=True) : legendary 열 내의 true는 1로, false는 0으로 대체하고 원본 데이터에 반영

- **df.sort_index(ascending = T/F)** : 데이터 프레임의 기존 index를 기준으로 오름차순(ascending=True), 내림차순 정렬한다

- **df.sort_values(기준 열, ascending = T/F)** : 데이터 프레임의 특정 column을 기준으로 오름차순(ascending=True), 내림차순 정렬한다
    <br> cf) df.sort_values(['Type 1', 'HP'], ascending=[True, True]) : 여러 column을 기준으로 할 때는 리스트로 묶어서 넣는다

### DataFrame 데이터 연산
- **df.describe()** : 데이터 프레임의 기술 통계량을 확인

- **df.apply( 함수 )** : 데이터 프레임에 함수를 적용한다

- **df.groupby( column명 )** : column을 기준으로 동일한 데이터끼리 그룹화한다

### csv 파일 관련
- **df = pd.read_csv( '파일경로/파일명.csv' )** : csv 파일을 읽어와서 df 변수에 저장

- **df.to_csv( '파일경로/파일명.csv' )** : 데이터 프레임 객체를 csv 파일로 저장한다 
