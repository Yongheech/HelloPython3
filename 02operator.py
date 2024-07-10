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
#
# print(f'''한빛전자에 1분기매출액은{seles}이고
# 1분기매입액은{buys}이기에 한빛전자의 1분기
# 수익액은{profit}입니다.
# ''')

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



