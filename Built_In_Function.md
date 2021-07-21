## Built In Function (내장 함수) 공부

#### ⭐ 하루에 3개씩 !



### 1. abs(x)

- Return the absolute value of a number.
  - 숫자의 절대값을 돌려줍니다.
- The argument may be an integer, a floating point number.
  If the argument is a complex number, its magnitude is returned.
  - 인자는 정수, 실수를 받는다 . 인자가 복소수면 그 크기가 반환된다.

```python
a = abs(3)
b = abs(-50)
c = abs(3+4j)
print(a, b, c)

# 3 50 5.0
```



### 2. all(iterable)

- Return `True` if all elements of the *iterable* are true (or if the iterable is empty). Equivalent to

  - *iterable* 의 모든 요소가 참이면 (또는 iterable 이 비어있으면) `True` 를 돌려줍니다. 다음과 동등합니다.

  ```python
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```

  ```
  📌AND 와 비슷한 의미
  # 리스트
  all([1,2,3,4,5]) : True
  
  #리스트 요소에 0이 있는 경우
  all([1,2,0,4,5]) : False
  
  #리스트가 비어있는 경우
  all([]) : True
  
  #문자열
  all('Sunghyun') : True
  
  #비어있는 문자열
  all('') : True
  
  #0이 있는 튜플
  all(('b', 2, 0, 'd')) : False
  
  ⭐#빈 문자열이 있는 튜플
  all(('a', '', 2, 3)) : False
  
  #비어있는 튜플
  all(()) : True
  
  📌 띄어쓰기가 있는 문자열은 True
  ```



### 3. any(iterable)

- Return `True` if any element of the *iterable* is true. If the iterable is empty, return `False`. Equivalent to

  - *iterable* 의 요소 중 어느 하나라도 참이면 `True` 를 돌려줍니다. iterable이 비어 있으면 `False` 를 돌려줍니다. 다음과 동등합니다.

  ```python
  def any(iterable):
      for element in iterable:
          if element:
              return True
      return False
  ```

  ```python
  📌 OR와 비슷한 의미
  
  # 리스트
  any([1,2,3,4,5]) : True
  
  # 리스트 요소에 0 -> False 이 있는 경우
  any([1,2,0,4,5]) : True
  
  # 리스트가 비어있는 경우
  any([]) : False
  
  # 문자열
  any('Sunghyun') : True
  
  # 비어있는 문자열
  any('') : False
  
  # 튜플
  any(('b', 3, 'a')) : True
  
  # 0이 있는 튜플
  any(('b', 2, 0, 'd')) : True
  
  ⭐# 0으로만 이루어진 튜플
  any((0, 0, 0, 0)) : False
  
  # 빈 문자열이 있는 튜플
  any(('a', '', 2, 3)) : True
  
  # 비어있는 튜플
  any(()) : False
  ```

  

