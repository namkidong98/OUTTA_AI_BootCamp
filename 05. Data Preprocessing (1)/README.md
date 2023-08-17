### 전처리에 사용된 함수
- df = **df.reset_index(drop = True)** : 데이터 프레임의 인덱스를 재설정한다
  <br> cf) drop = True : 기존의 인덱스를 삭제한다 (default는 false인데 그러면 기존 인덱스는 'index'열로 따로 유지된다)

- **df.isna().sum()** : 데이터 프레임의 column별로 결측치의 개수를 반환한다

- df = **df.drop( [ column1, column2, ...... ], axis=1 )** : 데이터 프레임의 특정 column들을 제거한다

- **df.dropna(inplace=True)** : 데이터 프레임 내에 결측치가 있는 행을 제거한다 (inplace=True로 기존 df에 변화를 반영)

- **df[ column ].value_counts()** : 특정 column에 있는 값들과 그 값들에 해당하는 데이터의 개수를 반환한다

- **df.map( ) : (1) 지정된 함수를 적용하여 값을 변환, (2) 딕셔너리를 적용하여 값을 변환

```python
# sex 열의 male을 0으로 변환, female을 1로 변환하고 자료형도 정수로 변환
df['sex'] = df['sex'].map({'male': 0, 'female': 1}).astype(int)

# embarked 열의 S는 0, C는 1, Q는 2로 변환하고 자료형도 정수로 변환
df['embarked'] = df['embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)

# age 열에 5를 더해 Adjusted_Age 열에 추가
df['Adjusted_Age'] = df['Age'].map(lambda x: x + 5)
```
