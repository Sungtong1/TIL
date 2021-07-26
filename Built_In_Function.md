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

    다른 컨테이너의 경우 내장 `frozenset`, `list`, `tuple` 및 `dict`) 클래스와 `collections` 모듈을 보세요

### 7.  sum(iterable,/,start=0)

- Sums *start* and the items of an *iterable* from left to right and returns the total. The *iterable*’s items are normally numbers, and the start value is not allowed to be a string.

  For some use cases, there are good alternatives to `sum()`. The preferred, fast way to concatenate a sequence of strings is by calling `''.join(sequence)`. To add floating point values with extended precision, see `math.fsum()`. To concatenate a series of iterables, consider using `itertools.chain()`.

  - *start* 및 *iterable* 의 항목들을 왼쪽에서 오른쪽으로 합하고 합계를 돌려줍니다. *iterable* 의 항목은 일반적으로 숫자며 시작 값은 문자열이 될 수 없습니다.

    어떤 경우에는 `sum()`에 대한 좋은 대안이 있습니다. 문자열의 시퀀스를 연결하는 가장 선호되고 빠른 방법은 `''.join(sequence)` 를 호출하는 것입니다. 확장된 정밀도로 부동 소수점 값을 더하려면 `math.fsum()` 를 보세요. 일련의 이터러블들을 연결하려면 `itertools.chain()` 를 고려해보세요.


### 8. round(number[, ndigits])

- Return *number* rounded to *ndigits* precision after the decimal point. If *ndigits* is omitted or is `None`, it returns the nearest integer to its input.

  For the built-in types supporting [`round()`](https://docs.python.org/3/library/functions.html#round), values are rounded to the closest multiple of 10 to the power minus *ndigits*; if two multiples are equally close, rounding is done toward the even choice (so, for example, both `round(0.5)` and `round(-0.5)` are `0`, and `round(1.5)` is `2`). Any integer value is valid for *ndigits* (positive, zero, or negative). The return value is an integer if *ndigits* is omitted or `None`. Otherwise the return value has the same type as *number*.

  For a general Python object `number`, `round` delegates to `number.__round__`.

  ```
  NOTE : The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See Floating Point Arithmetic: Issues and Limitations for more information. 
  ```

  - *number* 를 소수점 다음에 *ndigits* 정밀도로 반올림한 값을 돌려줍니다. *ndigits* 가 생략되거나 `None` 이면, 입력에 가장 가까운 정수를 돌려줍니다.

    [`round()`](https://docs.python.org/ko/3/library/functions.html#round) 를 지원하는 내장형의 경우, 값은 10의 *-ndigits* 거듭제곱의 가장 가까운 배수로 반올림됩니다; 두 배수가 똑같이 가깝다면, 반올림은 짝수를 선택합니다 (예를 들어, `round(0.5)` 와 `round(-0.5)` 는 모두 `0` 이고, `round(1.5)` 는 `2` 입니다). 모든 정숫값은 *ndigits* 에 유효합니다 (양수, 0 또는 음수). *ndigits* 가 생략되거나 `None` 이면, 반환 값은 정수입니다. 그렇지 않으면 반환 값은 *number* 와 같은 형입니다.

    일반적인 파이썬 객체 `number` 의 경우, `round` 는 `number.__round__` 에 위임합니다.

    ```
    참고 : float에 대한 round() 의 동작은 예상과 다를 수 있습니다: 예를 들어, round(2.675, 2) 는 2.68 대신에 2.67 을 제공합니다. 이것은 버그가 아닙니다: 대부분의 십진 소수가 float로 정확히 표현될 수 없다는 사실로부터 오는 결과입니다. 자세한 정보는 부동 소수점 산술: 문제점 및 한계 를 보세요.
    ```

### 9. reversed(seq)

- Return a reverse iterator. *seq* must be an object which has a `__reversed__()`) method or supports the sequence protocol (the `__len__()` method and the `__getitem__()` method with integer arguments starting at `0`).
  - 역 이터레이터 를 돌려줍니다. *seq* 는 `__reversed__()` 메서드를 가졌거나 시퀀스 프로토콜`__len__()` 메서드와 `0` 에서 시작하는 정수 인자를 받는 `__getitem__()` 메서드)을 지원하는 객체여야 합니다.

