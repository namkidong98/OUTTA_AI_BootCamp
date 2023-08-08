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
