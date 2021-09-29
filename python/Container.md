# 컨테이너(Container)

### 컨테이너란 ?

- 여러 개의 값을 저장할 수 있는 것 (객체)
- **시퀀스(sequence)형** : 순서가 있는(ordered) 데이터
  - 📌 순서가 있다 != 정렬되어 있다
  - 리스트(list), 튜플(tuple), 레인지(range), 문자형(string), 바이너리(binary)
- **비시퀀스(non-sequence)형** : 순서가 없는(unordered) 데이터
  - 세트(set), 딕셔너리(dictionary)



## 1. 시퀀스형

### 리스트(List)

- 순서가 있는 시퀀스로 인덱스를 통해 접근

- 인덱스는 0부터 시작

- 대괄호 `[]` 혹은 `list()`를 통해 생성

- 값에 대한 접근은 `list[i]`

- 중첩 리스트 예시

  - ```python
    a = [[1, 2], [3, 5]]
    a[0][1]
    # 2
    ```



### 튜플(Tuple)

- 튜플은 ⭐수정 불가능한(immutable) 시퀀스로 인덱스로 접근
- 소괄호 `()`혹은 `tuple()`을 통해 생성
- 값에 대한 접근은 `tuple(i)`
- 튜플은 일반적으로 파이썬 내부에서 활용됨
  - multiple assignment
  - 추후 함수에서 복수의 값을 반환하는 경우에도 활용
- 하나의 항목으로 구성된 튜플은 생성시 값 뒤에 쉼표를 붙여야 함
  - `a = (1, )`



### 레인지(range)

- 숫자의 시퀀스를 나타내기 위해 사용
- 기본형 : `range(n)`
  - 0부터 n-1까지의 숫자의 시퀀스
- 범위 지정 : `range(n, m)`
  - n부터 m-1까지의 숫자의 시퀀스
- 범위 및 스텝 지정 : `range(n, m, s)`
  - n부터 m-1까지 s 만큼 증가시키며 숫자의 시퀀스



### 시퀀스에서 활용하는 연산자/함수

- **Containment Test**

  - `in`
  - `not in` 

- **Contcatenation(+)**

  - 시퀀스 간의 concatenation(연결/연쇄)
  - range는 TypeError 발생

- **인덱싱 (indexing)**

  - 시퀀스의 특정 인덱스 값에 접근
  - 해당 인덱스가 없는 경우 IndexError

- **슬라이싱(slicing)**

  - 시퀀스를 특정 단위로 슬라이싱
  - [1, 2, 3, 5] [1`시작점(포함)`: 4`끝지점(미포함)`]
  - 시퀀스를 k간격으로 특정 단위로 슬라이싱 `[n, m, k]`

- **길이 `len()`**

  - 시퀀스의 길이

- **최소/최대 `max()` `min()`**

  - 시퀀스에서의 최솟/최댓값
  - 문자열은 ASCII 코드에 따름

- **count()**

  - 시퀀스에서의 특정 원소의 개수 (등장하지 않는 경우 0 반환)

  - ```python
    [1, 2, 1, 2, 4].count(1)
    # 2
    ```



## 2. 비시퀀스형

### 세트(Set)

- 순서가 없는 자료구조

- 중괄호 `{}` 혹은 `set()`을 통해 생성

  - 빈 세트를 만들기 위해서는 반드시 `set()`을 반드시 활용해야 함 📌 그렇지 않으면 딕셔너리로 인식

- 순서가 없어서 별도의 값에 접근할 수 없음

- 수학에서의 집합과 동일한 구조를 가짐

  - 집합 연산이 가능

  - 중복된 값이 존재하지 않음

    - 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음

      📌 단, 이후 순서가 무시되므로 순서가 중요한 경우 사용할 수 없음



### ⭐딕셔너리(Dictionary)

- key 와 value가 쌍으로 이뤄진 자료구조
- 중괄호 `{}` 혹은 `dict()`을 통해 생성
- index가 아닌 key를 통해 value에 접근
- ⭐ key는 변경 불가능한 데이터 (immutable)만 가능
  - string, integer, float, boolean, tuple, range
- value는 모든 값으로 설정 가능



### 3. 컨테이너 형변환

|                | string | list     | tuple    | range | set      | dictionary |
| -------------- | ------ | -------- | -------- | ----- | -------- | ---------- |
| **stirng**     |        | o        | o        | x     | o        | x          |
| **list**       | o      |          | o        | x     | o        | x          |
| **tuple**      | o      | o        |          | x     | o        | x          |
| **range**      | o      | o        | o        |       | o        | x          |
| **set**        | o      | o        | o        | x     |          | x          |
| **dictionary** | o      | o(key만) | o(key만) | x     | o(key만) |            |



### 4. 컨테이너 분류

- **변경 불가능한 데이터(immutable)**

  - 리터럴(literal) - 숫자(Number), 문자열(String), 참/거짓(Boolean)
  - range
  - tuple

- **변경 불가능한 데이터 복사**

  - ```python
    a = 20
    b = a
    b = 10
    # b = 10을 통해 재할당이 발생
    # a =20, b =10
    ```



- **변경 가능한 데이터(mutable)**

  - list
  - set
  - dictionary

- **변경 가능한 데이터 복사**

  - ```python
    num1 = [1, 2, 3, 4]
    num2 = num1
    num2[0] = 100 
    # 해당 리스트의 첫번째 원소 값이 변경됨
    # num1 = num2 = [100, 2, 3, 4]
    ```

-  **요약**

  - Sequence
    - 'String' ▶ immutable
    - (Tuple) ▶ immutable
    - Range() ▶ immutable
    - [List] ▶ mutable
  - 비 Sequence
    - {Set}▶ mutable
    - Dictionary {key : value}▶ mutable
