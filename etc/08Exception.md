# 📘 예외처리 및 파일 입출력

## 구문 오류 (Syntax Errors)
- 문법 오류, 파싱 오류
- `""`을 빼먹는다던가, `;`를 빼먹는다던가...

## 예외 (Exceptions)
- 문법적으로는 올바른 프로그램이 수행 도중 예상치 못한 입력값이 들어와 비정상적인 상황으로 종료되는 경우
- 인터프리터는 예외 상황이 발생하면 어느 함수의 어느 부분에서 예외 상황이 발생했는지 출력해주고 프로그램을 종료시킴

# 🛠️ 예외처리

## `try - except` 문
```python
try:
    예외 발생할 우려가 있는 코드
except 예외타입:
    예외가 발생할 경우 실행되는 코드
```

- **어떤 예외 상황에 의해서 `except`가 실행되었는지 알고 싶으면?**
    1. `Exception as e` 문법을 통해 `Exception` 변수를 선언
    2. `e` 값을 출력하여 오류의 종류를 알 수 있음
    ```python
    try:
        b = 2/0
        a = 1 + 'hundred'
    except ZeroDivisionError:  # 구체적인 예외처리
        print("0으로 나누는 오류")
    except TypeError:  # 구체적인 예외처리
        print("지원하지 않은 연산자를 사용하는 오류")
    except Exception as e:  # 보편적인 예외처리
        print("error:", e)

    # 출력:
    # error: division by zero
    # error: unsupported operand type(s) for +: 'int' and 'str'
    ```

## `try - except - else` 문
```python
try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print("0으로 나누는 오류")
except ValueError:
    print("입력값이 정수나 실수가 아닙니다")
except:
    print("10 2와 같이 두 정수를 입력하세요")
else:  # 정상적인 값이 들어오면 처리될 프로그램
    print("{}/{}={}".format(a, b, result))
```

## `try - except - finally` 문
- **try**: 먼저 실행되어 예외가 발생하지 않으면 `except`로 건너뛰고, 예외가 발생하면 오류를 확인하여 `except`의 매칭되는 부분으로 넘겨줌
- **except**: 예외가 발생했을 때 처리할 내용을 담음
- **else**: 예외가 발생하지 않을 때 실행하게 되는 블록
- **finally**: 예외의 발생 여부와 상관없이 항상 실행되는 블록

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("0으로 나누는 오류 발생")
    else:
        print("결과:", result)
    finally:
        print("수행 완료")

divide(100, 2)
divide(100, 0)
```

## `raise` 문
- 예외를 강제로 발생시킬 수 있음

```python
def get_ans(ans):
    if ans in ['예', '아니오']:  # 입력값이 '예' 또는 '아니오'
        print("정상적인 입력")
    else:
        raise ValueError('입력을 확인하세요')  # 강제로 ValueError 발생시킴

while True:
    try:
        ans = input('예/아니오 중 하나를 입력하세요:')
        get_ans(ans)
        break
    except Exception as e:
        print("error:", e)
```

# 📂 파일 입출력

#### 파일: 컴퓨터의 저장 장치 내에 데이터를 저장하기 위해 사용하는 논리적인 단위
- 하드디스크나 외장디스크 같은 저장 장치에 저장한 후 필요할 때 다시 불러 사용 가능
- 필요에 따라 수정하는 것도 가능
- `.py`, `.txt`, `.doc`, `.hwp`, `.pdf`와 같은 확장자를 붙여 파일의 종류를 구분

#### 경로: 컴퓨터 저장 장치 내의 파일 위치

#### 파일을 열고 사용한 후 닫는 단계
1. **파일 열기**
2. **파일의 읽기, 쓰기 또는 파일의 내용 수정**
3. **파일 닫기**

## 📄 파일 쓰기와 모드
```python
f = open("hello.txt", 'w')
f.write("Hello World!")
f.close()
```

|모드|의미|
|--|--|
|`r`|읽기 전용 모드, 파일이 있어야 함|
|`w`|쓰기 전용 모드, 파일 없어도 됨|
|`a`|쓰기 모드로 열어 기존 파일 뒤에 새로 작성된 내용 추가, 파일 없어도 됨|
|`x`|쓰기 모드로 열어, 파일을 새로 만들기 위해 사용함. 파일 없어야 함|
|`+`|읽기 쓰기 모드. ex) `r+` 읽기 모드로 열어 쓰기까지 가능|

|파일 모드|의미|
|--|--|
|`t`|텍스트 파일 형식으로 열거나 생성|
|`b`|이진 파일 형식으로 파일을 열거나 생성|

```python
f = open("hello.txt", 'wt')  # 파일을 텍스트로 열기
```

- `f.write()` 만으로는 줄바꿈이 이루어지지 않으며, `\n`을 입력해야 파일 내 줄바꿈이 이루어짐
- `f.close()`로 버퍼의 내용을 디스크로 보내고 버퍼 크기만큼 메모리가 비워지게 됨

## 📖 파일 읽기
```python
f = open("hello.txt", "r")
s = f.read()  # 파일 전체를 읽음. f.read(5)면, 5글자만 읽음
print(s)
f.close()
```

- `readline()`: 파일의 내용을 줄 단위로 읽음 (`\n` 포함하니, 출력 시엔 `end=""` 써주기!)
    - 한 번 실행 시 첫 번째 줄, 한 번 더 실행 시 두 번째 줄...

## 📄 파일 추가하기
```python
f = open("hello.txt", 'a+')  # 파일 추가 읽기 모드로 열기
f.write("Hello World!")  # Hello World가 추가됨
f.close()
```

> 내부에 한글이 포함되어 있을 시 오류가 발생할 수 있음. `f = open(fname, 'r', encoding="UTF8")`

## 🔍 `with` 문법
```python
with open("hello.txt", 'w') as f:  # 파일 열기와 닫기를 자동 수행!
    f.write("Hello World!")
```