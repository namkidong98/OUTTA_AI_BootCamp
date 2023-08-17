## 데이터 전처리 사용 함수 
- df = **df.rename( columns= { A : B, C : D ... } )** : 딕셔너리를 기준으로 데이터 프레임의 column명을 변경한다
```python
# 칼럼이름을 다루기 쉽게 tax(£) -> tax 로 변경
df = df.rename(columns={'tax(£)':'tax'})
```

- **df.describe()** : 데이터 프레임의 column별로 개수, 평균, 표준편차, 사분위수를 조회한다
![image](https://github.com/namkidong98/OUTTA_AI_BootCamp/assets/113520117/9cd83616-5076-4f7a-8703-8a6ebbf141cf)

<br>

- **데이터가 0인 열을 삭제하는 방법** : 0인 데이터를 np.NaN(결측치)로 바꾸고 dropna로 한번에 제거한다
```python
# tax와 enginSize에서 0인 값을 nan으로 바꾸고 삭제
df["engineSize"]=df["engineSize"].replace(0,np.nan) 
df["tax"]=df["tax"].replace(0,np.nan)

df.dropna(inplace = True)
```

- **df.duplicated().sum()** : 데이터 프레임에 중복된 행의 개수를 반환한다

- **df.drop_duplicates(keep='first', inplace=True)** : 데이터 프레임에서 중복된 행들 중 첫 번째만 남기고 그 외 중복된 행들은 제거하여 반영한다
  <br> cf) keep='last'는 중복된 행 중 마지막 행만 남긴다, keep 옵션이 없어도 중복된 행들 중 하나만 남기고 그 외 중복된 행들을 제거한다

- **데이터에서 조건에 부합하는 특정 행(row)만 삭제** : ex) df.drop(df[df['year'] == 2006].index, axis=0, inplace=True)

- **df.str.contains( ' 찾는 문자열 ' )** : 데이터 프레임의 문자열에서 찾는 문자열이 포함되어 있는 행을 반환한다
```python
df[(df['model'].str.contains('Ioniq')) & (df['mpg'] == 256.8)]
```

<br>

## 범주형 데이터 자료 변환
- **model을 그룹화하고 그룹마다 평균을 구해 내림차순으로 정렬하고 그룹마다 특정 숫자로 변환**
  1. .mean()을 적용하면 series로 반환되는데 이를 to_frame()을 적용해야 데이터 프레임으로 변환하여 sort_values를 적용할 수 있게 된다
  2. map과 딕셔너리를 사용해서 그룹화된 범주형 데이터를 숫자형 데이터로 변환한다
![image](https://github.com/namkidong98/OUTTA_AI_BootCamp/assets/113520117/c9b53fcd-d1a8-4922-8308-ae9348330785)

<br>

- **기존 데이터의 문자열을 처리한 후 반영하는 방법** : for문으로 데이터 프레임의 데이터를 가져와서 처리하고 새로운 리스트에 더한 다음 assign함수를 사용한다
```python
model_name = []
for i in df['model']:
    model_name.append(i.strip())

df = df.assign(model=model_name)
```
