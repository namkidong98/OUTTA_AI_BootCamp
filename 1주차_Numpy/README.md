# 배열 생성 및 배열 형태 변환
1. np.array(리스트 or 튜플): 리스트나 튜플을 ndarray로 바꾼다

2. ndarray.reshape(): 원하는 행, 열의 다차원 배열로 변환시킨다

3. np.zeros((shape), dtype=원하는 데이터타입): 원하는 shape과 데이터타입의 0만을 원소로 하는 ndarray를 만든다

4. np.ones((shape), dtype=원하는 데이터타입): 원하는 shape과 데이터타입의 1만을 원소로 하는 ndarray를 만든다

5. np.full((shape), number): 원하는 shape과 원하는 숫자(number)만을 원소로 하는 ndarray를 만든다

6. np.arange(start, stop, step): start이상 stop 미만이고 간격이 step인 배열을 생성

7. np.linspace(start, stop, n등분): start이상 stop '이하'를 n등분하여 배열 생성

8. np.random.choice(data, shape): 주어진 배열(data)에서 임의로 원소를 선택하여 배열 생성

9. np.random.shuffle(data): 주어진 배열의 순서 임의로 변경

10. np.random.rand(shape): [0, 1)에서 각 구간의 난수 수가 균등분포를 따르도록 샘플링

11. np.random.randn(shape): 난수가 표준정규분포를 따르도록 샘플링

12. np.random.randint(start, stop, (shape)): start이상 stop '미만'인 난수를 정수로 추출하여 주어진 shape에 따라 샘플링

<br>

# 배열 속성 확인
1. data.dtype: ndarray의 자료형 확인

2. data.ndim: ndarray의 차원 수 확인

3. data.shape: ndarray의 크기를 확인

4. data.size: ndarray의 원소의 개수를 확인

<br>

# 배열 연산
1. ndarray.astype('자료형'): 주어진 자료형으로 ndarray의 원소들의 자료형을 변환시킨다       ex) array = array.astype('int64')

2. ndarray.T: ndarray를 전치시킨다

3. ndarray.sort(): ndarray의 원소들을 행 별로 오름차순으로 정렬한다

4. ndarray.sort(axis=0): ndarray의 원소들을 '열' 별로 오름차순으로 정렬한다

5. ndarray1 + ndarray2: 같은 위치에 있는 원소끼리 덧셈 수행

6. ndarray1 - ndarray2: 같은 위치에 있는 원소끼리 뺄셈 수행

7. ndarray1 * ndarray2: 같은 위치에 있는 원소끼리 곱셈 수행

8. ndarray1 / ndarray2: 같은 위치에 있는 원소끼리 나눗셈 수행

9. ndarray1 @ ndarray2: 두 행렬의 곱을 계산(단, 'ndarray1의 열의 개수 == ndarray2의 행의 개수'에만 연산 가능)

10. np.dot(ndarray1, ndarray2): 두 행렬의 곱을 계산

11. np.sum(ndarray): ndarray의 모든 원소의 합을 계산
    <br> cf) np.sum(ndarray, axis=0): 열(column)별로 합을 계산
    <br> cf) np.sum(ndarray, axis=1): 행(row)별로 합을 계산

12. np.mean(ndarray): ndarray의 모든 원소의 평균을 계산

13. np.std(ndarray), np.var(ndarray): ndarray의 모든 원소의 표준편차, 분산을 계산

14. np.min(ndarray), np.max(ndarray): ndarray의 원소 중 최솟값, 최댓값을 반환

15. np.argmin(ndarray), np.argmax(ndarray): ndarray의 원소 중 최솟값, 최댓값의 인덱스를 반환 (인덱스는 0부터 시작)

16. np.cumsum(ndarray), np.cumprod(ndarray): ndarray의 누적합, 누적곱을 반환
    <br> cf) 누적합, 누적곱은 기존 배열과 동일한 크기의 배열이되 자신보다 이전 인덱스들을 더하거나(cumsum) 곱하여(cumprod) 현재 인덱스의 값을 계산한 배열이다

<br>

# 인덱싱과 슬라이싱
1. ndarray[row][column] == ndarray[row, column] : 0부터 시작하는 인덱스를 row와 column을 기준으로 넣어 ndarray 혹은 원소를 반환한다 (인덱싱)

2. ndarray[ start: stop , start : stop ] : row, column 순으로 인덱스를 start이상 stop미만을 적용하여 해당 범위의 ndarray를 반환한다 (슬라이싱)

3. ndarray[ : , : ] = np.nan : ndarray의 전체 원소를 결측치(NaN)으로 대체한다 (단, float인 경우에만 가능하므로 astype을 적용할 필요가 있다)

4. ndarray < 0 : 원소가 음수인가를 기준으로 ndarray의 모든 원소를 True / False 값으로 대체한 새로운 ndarray를 반환한다

5. ndarray[ 조건 ] = '숫자' : 조건에 부합하는 원소들, 즉 True가 반환되는 원소들만을 인덱싱하여 원하는 숫자를 대입한다
    <br> cf) ndarray[ ndarray < 0 ] = 0 : 0보다 작은 원소들에 0을 대입한다
