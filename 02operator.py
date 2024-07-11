# 수식 expression
# 숫자, 변수, 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 피연산자 : 연산의 대상들을 의미

# 산술연산자
# 자료형 승격promotion

# 매출액 입력시 총합 출력
sales1 = int(input('1월달매출액은?'))
sales2 = int(input('2월달매출액은?'))
sales3 = int(input('3월달매출액은?'))
total = (sales1) + (sales2)+ (sales3)

print(f'1분기 전체 매출 : {total}')

# 1분기 수익 계산하기

seles = int(input('1분기매출액은?'))
buys = int(input('1분기매입액은?'))
profit = (seles) - (buys)

print(f'1분기수익액 : {profit}원')
# 방의 넓이 구하기

width = input('가로넓이는?')
length = input('세로넓이는?')
area = int(width) * int(length)

print(f'넓이 : {area}')

print(f''' 이 방의 가로넓이는{width}이고
이 방의 세로 넓이는{length}이다 그리하여
이 방의 전체 넓이는 {area} 이다.
''')

# 신체질량지수BMI 구하기

weight = float(input('몸무게(kg)'))
height = float(input('신장은(m)'))
bmi = int(weight / (height * height))

print(f'BMI : {bmi}')

# 홀짝 게임
coins = int(input('손안에 동전수를 입력하세요 :'))
result = coins % 2
print(f'{result}')

# 빵 나누기

breads = 97
divsor = 3
studs = 97 // 3
mods = 97 % 3

print(f'''
빵을 나누어 줄수 있는 학생수 : {studs}
남는 빵 갯수 : {mods}
''')

# 전염병 예상 감염자 구하기
# 1일차 -> 2명
# 2일차 -> 4명
# 3일차 -> 8명
# 4일차 -> 16명
# n일차 -> 2 ** n명

infectors = 2 ** 30
print(f'30일 이후 예상 감염자 수 : {infectors}')

# 할당 연산자
# 변수에 값을 대입하는 데 사용하는 연산자로 대입 연산자라고도 함
# 할당 연산자를 사용하면 계산과 동시에 결과값을 변수에 넣을 수 있음
# 할당 연산자의 종류는 다소 많지만
# 연산자 기호가 직관적이기 때문에 쉽게 이해할 수 있음
# 종류로는(=, +=, -+ ,*= , /= , %= , //=, **=)

# 논리 연산자
# 피연산자의 논리 자료형(True/False) 을 이용하는
# 연산자로 and, or, not이 있음


# 논리 연산자 단축식 평가
# and 연산
# 피연산자가 모두 True인 경우에만 결과가 True
# 피연산자가 하나라도 False이면 결과는 False

# or 연산
# or은 '또는' 이라는 뜻으로, 피연산자 중 하나라도
# True라면 결과값은 True

# not 연산
# not은 '부정'이라는 뜻으로, 피연산자의 현재 상태를 부정하는 연산자
# 피연산자가 True이면 결과로 False를 출력하고
# False이면 True를 출력

# 삼항 연산자
# 조건문을 한 줄로 표현할 수 있는 연산자
# 참일때값 if 조건식 else 거짓일때값

myScore = 75
result = '합격!' if myScore >= 90 else '불합격!'

print(result)

# 복리 계산기
money = 5_000_000
rate = 0.05
money = money + (money * rate) # 1년후 총 금액
money = money + (money * rate) # 2년후 총 금액
money = money + (money * rate) # 3년후 총 금액
money = money + (money * rate) # 4년후 총 금액
money = money + (money * rate) # 5년후 총 금액

print(f'5년 후 총 수령액 : {int(money):,} 원')

# 범퍼카 탑승
child = int(input('어린이의 신장을 입력하세요 :'))
isRide = (child >= 120)

print(f'{isRide}')

# 범퍼카 탑승 판별
child = int(input('어린이의 신장을 입력하세요 :'))
isRide = (child >= 120) & (child < 170)
print(f'{isRide}')
# 적자/흑자 판별
income = int(input('수입은?'))
outcome = int(input('지출은'))

result = '흑자'if income > outcome else '적자'
print(f'{result}')