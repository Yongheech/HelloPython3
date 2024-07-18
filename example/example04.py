# 51 구구단

print('''
         Multtiplication Table
      1   2   3   4   5   6   7   8   9
---------------------------------------
1 |   1   2   3   4   5   6   7   8   9
2 |   2   2   3   4   5   6   7   8   9
3 |   3   2   3   4   5   6   7   8   9
4 |   4   2   3   4   5   6   7   8   9
5 |   5   2   3   4   5   6   7   8   9
6 |   6   2   3   4   5   6   7   8   9
7 |   7   2   3   4   5   6   7   8   9
8 |   8   2   3   4   5   6   7   8   9
9 |   9   2   3   4   5   6   7   8   9

''')

print('''
       Multtiplication Table
      1   2   3   4   5   6   7   8   9
---------------------------------------

''')
for i in range(1, 9+1): # 행
        print(f'{i} |   1   2   3   4   5   6   7   8   9')

print('''
       Multtiplication Table
      1   2   3   4   5   6   7   8   9
---------------------------------------
''')
for i in range(1, 9+1): # 행
    print(f'{i} |', end='')
    for j in range(1, 9+1):
      print(f'{i * j:4d}',end='' )
    print()

# 33

cardno = input('카드번호는?')

result = '잘못된 카드 번호입니다'
if cardno[:2] == '35':
    if cardno == '356317': result = 'JCB카드 NH농협카드'
    elif cardno == '356901':result = 'JCB카드 신한카드'
    elif cardno == '356912':result = 'JCB카드 KB국민카드'
elif cardno[:1] == '4':
    if cardno == '404825':result = '비자카드 비씨카드'
    elif cardno == '438677':result = '비자카드 신한카드'
elif cardno[:1] == '5':
    if cardno == '515594':result = '마스터카드 신한카드'
    elif cardno == '524353':result = '마스터카드 외환카드'
    elif cardno == '540926':result = '마스터카드 KB국민카드'

print(result)

# 16 개선하기 - 리스트/반복문/함수
price = 34_560
paid = 50_000
charge = paid - price

charges = []
moneys = [50000, 10000, 5000, 1000, 100, 50, 10]

for money in moneys:
    charges.append(charge // money)
    charge %= money

result = f'''
금액 : {price:,} 원
지불금액 : {paid:,}원
잔돈 : {(paid - price):,}원
------------------
'''
for idx, m in enumerate(moneys):
    result += f'{m}원 : {charges[idx]} 장/개\n'

print(result)


def compute_charge(price, paid):
    charges = []
    moneys = [50000, 10000, 5000, 1000, 100, 50, 10]

    charge = paid - price
    for money in moneys:
        charges.append(charge // money)
        charge %= money

    result = f'''
    금액 : {price:,} 원
    지불금액 : {paid:,}원
    잔돈 : {(paid - price):,}원
    ------------------
    '''
    for idx, m in enumerate(moneys):
        result += f'{m}원 : {charges[idx]} 장/개\n'

    print(result)


# 잔돈 구하는 함수 호출 및 테스트
price = int(input('지불해야 할 금액은? '))
paid = int(input('받은금액은? '))
compute_charge(price,paid)

# 26 - 세금 계산 computeTax

def computeTax(isMarried, salary):
    tax = 0
    if isMarried == 0:
        tax = salary * 0.1
        if salary >= 3000:
            tax = salary * 0.25
    elif isMarried == 1:
        tax = salary * 0.15
        if salary >= 6000:
            tax = salary * 0.35

    print(f'''
    결혼여부 : {isMarried}, 연봉 : {salary},
    세금 : {tax:,}''')

# 데이터 입력 및 함수 호출
isMarried = int(input('결혼여부는? 0:미혼, 1:기혼'))
salary = int(input('연봉은?'))
computeTax(isMarried, salary)

# 27 - 윤년 구분 isLeapYear
# 1992, 2000, 2020 (윤)
# 1900, 2100 (윤x)

def isLeapYear(year):

    isLeap = '윤년아님!'

    cond1 = (year % 4 == 0 and year % 100 != 0)
    cond2 = (year % 400 == 0)
    if cond1 or cond2 : isLeap = '윤년 맞음!@@'

    print(f'{year} 년은 {isLeap} ')

year = int(input('년도는?'))
isLeapYear(year)

