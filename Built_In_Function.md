## Built In Function (내장 함수) 공부

#### ⭐ 하루에 3개씩 !

[내장함수](https://docs.python.org/3/library/functions.html)

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




### 4. bin(x)

- Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If *x* is not a Python `int`) object, it has to define an `__index__()`method that returns an integer. Some examples:
  - 정수를 《0b》 가 앞에 붙은 이진 문자열로 변환합니다. 결과는 올바른 파이썬 표현식입니다. *x* 가 파이썬 `int` 객체가 아니라면, 정수를 돌려주는 `__index__()` 메서드를 정의해야 합니다. 몇 가지 예를 들면:

```python'
bin(3)
'0b11'
bin(-10)
'-0b1010'
```

​	접두어 `0b`가 필요하다면 2번째 인자로 `'#b'` 필요하지 않다면 `'b'` 를 입력한다.

```
⭐format(14, '#b'), format(14, 'b')
('0b1110', '1110')
f'{14:#b}', f'{14:b}'
('0b1110', '1110')
```



### 5. *class* list([iterable])

- Rather than being a function, `list` is actually a mutable sequence type, as documented in [Lists](https://docs.python.org/3/library/stdtypes.html#typesseq-list) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).
  - 함수이기보다, [리스트](https://docs.python.org/ko/3/library/stdtypes.html#typesseq-list) 와 [시퀀스 형 — list, tuple, range](https://docs.python.org/ko/3/library/stdtypes.html#typesseq) 에 문서화 된 것처럼, `list` 는 실제로는 가변 시퀀스 형입니다.



### 6. *class* set([iterable])

- Return a new [`set`] object, optionally with elements taken from *iterable*. `set` is a built-in class. See [`set`] and [Set Types — set, frozenset] for documentation about this class.

  For other containers see the built-in [`frozenset`], [`list`], [`tuple`], and [`dict`] classes, as well as the `collections`

  - 새 `set` 객체를 돌려줍니다. 선택적으로 *iterable* 에서 가져온 요소를 갖습니다. `set` 은 내장 클래스입니다. 이 클래스에 대한 설명서는 `set`및 [집합 형 — set, frozenset] 을 보세요.

    다른 컨테이너의 경우 내장 `frozenset`, `list`, `tuple` 및 `dict`) 클래스와 `collections` 모듈을 보세요.

