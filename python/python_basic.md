# 파이썬 기초

### Python 특징

- 인터프리터 언어 (Interpreter)
  - 소스코드를 컴파일하지 않고 , 한 줄씩 소스코드를 읽어서 **바로 실행**
  - 컴파일 언어에 비해 느릴 수 있지만 빌드 과정이 없이 바로 실행 가능

* 객체 지향 프로그래밍(OOP : Object Oriented Programming)
* 동적타이핑 (Dynamic Typing)
  * 변수에 별도의 타입 지정이 필요 없음



### 코드 스타일 가이드 

* 코드를 '어떻게 작성할지'에 대한 가이드 라인 

  * [PEP8](https://www.python.org/dev/peps/pep-0008/) - 파이썬에서 제안하는 스타일 가이드
  * [Google Style guide](https://google.github.io/styleguide/pyguide.html) 등 기업, 오픈소스 등에서 사용되는 스타일 가이드
  * 변수 선언시 띄어쓰기, 들여쓰기, 문자열에서 `"` `'` 사용의 통일 등을 명시

*  한 줄 주석 표현시 `#`

  ```python
  # 주석(comment) 입니다.
  
  #print('hello')
  print('hello')
  ```

* 특수형태의 주석 `"""`

  ```python
  def foo():
      """이 함수는 foo 입니다
      docstring으로 함수나 클래스의 기능을 설명합니다."""
  ```

* 코드는 1줄에 1문장(statement)이 원칙

  * 기본적으로 파이썬에서는 세미콜론(;)을 작성하지 않음
  * 한 줄로 표기할 때는 세미콜론(;)을 작성할 수 있음



### 변수 (Variable)

- 변수는 할당 연산자 `=` 를 통해 값을 ⭐**할당** (assignment)
- type()  
  - 변수에 할당된 값의 타입을 반환
- id()  
  - 변수에 할당된 값(객체)의 고유한 아이덴티티(identitiy) 값이며, 메모리 주소 

```python
# 값은 값 동시 할당
x = y = 1004
# 다른 값 동시에 할당
x, y = 1, 2
```

- 값 swap 2가지 방법

  - ```python
    # 임시 변수(tmp) 활용
    x, y = 10, 20
    tmp = x
    x = y
    y =tmp
    print(x,y)
    ```

  - ```python
    # ⭐Pythonic !!!
    x, y = 10, 20
    y, x = x, y
    ```

- 변수 이름 규칙

  - 영문 알파벳, 언더스코어(_), 숫자

  - 첫 글자에 숫자가 올 수 없음

  - 길이제한이 없고, 대소문자 구별

  - 다음의 키워드는 예약어로 사용 불가

    ['False', 'None', 'True', '\__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

  - 내장함수나 모듈 등의 이름으로도 만들면 안됨



### 데이터 타입

- **숫자(Number)**

  - 정수(int) : 오버플로(overflow)가 발생하지 않음

    - 진수표현
      - 2진수 : 0b ex) `ob10`
      - 8진수 : 0o
      - 16진수 : 0x

  - 실수(float)

    - Floating Point Rounding Error  : 부동소수점에서 실수 연산 과정에서 발생

    - ```python
      num1 = 0.1 * 3
      num2 = 0.3
      
      num1과 num2의 비교
      
      # 1. 임의의 작은 수 사용
      print(abs(num1-num2) <= 1e-10)
      
      # 2. system상의 machine epslion
      # epslion(그리스어의 알파벳 중 다섯 번째로 ε으로 쓰며, 영어의 E에 해당한다. 수학에서는 매우 작은 수를 의미하는 기호로 자주 쓰인다.2.220446049250313e-16)
      import sys
      num1 = 0.1 * 3
      num2 = 0.3
      print(abs(num1-num2) <= sys.float_info.epsilon)
      
      # 3. math 모듈 활용 (python 3.5 이상)
      import math
      num1 = 0.1 * 3
      num2 = 0.3
      print(math.isclose(num1, num2))
      ```

  - 허수(complex)

    - 허수부를  j로 표현

- **문자열(String)**

  - 모든 문자는 str 타입

  - 작은 따옴표 `'` 나 큰 따옴표 `"` 를 활용하여 표기 하나 소스코드 내에서 하나의 문장부호를 선택하여 유지

  - 이스케이프 시퀀스(Escape Sequence)

    - 문자열 내에서 특정 문자나 조작을 위해서 역슬래시`\`를 활용하여 구분

    - `\n` 줄 바꿈

    - `\t` 탭

    - `\r` 캐리지리턴

    - `\0` 널(Null)

    - `\\` 역슬래시(`\`)

    - 

      ```python
      print('글을 쓰다가 엔터를 쓰고싶다면\n탭을쓰고 싶다면 탭/t탭')
      ```

  - ⭐ String Interpolation

    ```python
    name = '철수'
    # %-formatting
    print('안녕, %s야' % name)
    
    # str.format()
    print('안녕, {}야'.format(name))
    
    # f-strings (python 3.6+)
    print(f'안녕, {name}야')
    ```

- **참/거짓(Boolean)**

  - True / False 값을 가진다.  📌True의 T 와 False의 F는 대문자로 입력 
  - 비교/논리 연산을 수행함에 있어서 활용됨
  - ⭐ False 값 = `0`, `0.0`, `()`, `[]`, `{}`, `''`, `None`

- **None**

  - 값이 없음을 표현하기 위한 타입인 NoneType



### 타입 변환

- **암시적 타입 변환(Implicit)**

  - 사용자가 의도하지 않고, 파이썬 내부적으로 타입 변환 하는 경우

- **명시적 타입 변환(Explicit)**

  - 사용자가 특정 함수를 활용하여 의도적으로 타입 변환 하는 경우
  - Int
    - str*, float ▶ Int
  - Float
    - str*, int ▶ Int
  - Str
    - int, float, list, tuple, dict

  📌`*`형식에 맞는 문자열만 가능



### 연산자

- **산술 연산자**

  - `/` 나누기 ▶ 결과가 항상 float
  - `//` 몫
  - `**` 거듭제곱
  - `divmod(5, 2)` ▶ (quotient(몫), remainder(나머지))

- **비교 연산자**

  - 값을 비교하며, True / False 값을 리턴함
  - `is` 객체 아이덴티티(OOP)
  - `is not` 객체 아이덴티티가 아닌 경우

- **논리 연산자**

  - `AND`, `OR`, `Not`
  - 일반적으로 비교연산자와 함께 사용됨
  - ⭐ **단축평가** : 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
    - and 연산에서 첫번째 값이 False인 경우 무조건 False
    - or 연산에서 첫번째 값이 True인 경우 무주건 True

- **복합 연산자**

  - ```python
    num = num +1
    ```

  - ```python
    num += 1
    ```

- **기타 연산자**

  - Concatenation (연속)

    - 자료형 끼리도 + 가능하다. ▶ 결합

  - Containment Test 

    - ```python
      'a' in 'apple'
      True
      ```

  - Identity

    - is 연산자를 통해 동일한 객체(object)인지 확인 가능
    - ⭐ 파이썬에서 -5 부터 256까지 숫자의 id는 동일
    - ⭐ 특정 변수가 비어있는지 확인하기 위해서는 x == none 보다는 x is None을 쓰는 것을 권장

  - Indexing / Slicing

    - []를 통해 값을 접근하고, [:]를 통해 슬라이싱 가능

    - ```python
      'hello, ssafy!'[0]
      # 결과 'h'
      'hello, ssafy!'[1:5]
      # 결과 'ello'
      ```

- **연산자 우선순위**

  - ()
  - Slicing
  - Indexing
  - **
  - 단항 연산자
  - 산술 연산자 `*` `/` `%`
  - 산술 연산자 `+` `-`
  - 비교 연산자, in, is
  - not
  - and
  - or

