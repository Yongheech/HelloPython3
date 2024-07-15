# 모듈
# 특정 기능을 수행하는 코드들의
# 코드 재사용 : 한번 작성한 코드를 여러 번 사용 가능
# 코드 관리 : 큰 프로젝트를 작은 모듈로 나눠 관리 가능
# 협업 : 여러 개발자가 각각 모듈을 개발하고 함께 사용

# 표준모듈 : 파이썬에서 기본적으로 제공하는 모듈, 바로 사용 가능
# 외부모듈 : 다른 조직, 개발자가 만든 모듈, 별도 설치 필요
# 사용자 정의 모듈 : 직접 만든 모듈

# 모듈 사용방법
# import 모듈명
# import 모듈명 as 별칭
# from 모둘명 import 함수명 as 별칭

# 난수 생성
import random
import random as rnd
from random import randint

# 1 ~ 10 사이 임의의 난수 생성
print(random.randint(1,10))
print(rnd.randint(1,10))
print(randint(1,10))
print(rnd.randint(1,45))

# 특정 범위의 숫자들 중에서 하나 추출 (표본추출)
# range (n, m) : n ~ m-1 사이의 정수들
print(rnd.sample(range(1, 46), 6))

# 날짜 시간 처리
import datetime as dt

print(dt.datetime.now())
print(dt.date.today())
print(dt.datetime.now()
      .strftime('%Y년-%m월-%d일 %H시:%M분:%S초'))

# operator 모듈
# 연산자 관련 모듈로 앞에서
# 학습한 산술, 비교 논리연산자를 대신 기능 (함수)을 가지고 있음
# 예를 들어 덧셈 연산자 '+' 는
# operator 모듈에 add() 함수로 정의되어 있음

# 긴급재난 지원금 대상자 판별

import operator as op
tgIncome = 4_000_000

income = int(input('월소득을 입력하세요 : '))
isOther = int(
      input('다른 지원금을 받고 있습니다까? 1: 받음 2: 받지 않음'))

# result = '수급대상자' if (income <= 4000000) \
#                    & (isOther == 2) else '수급 비대상자'

result = '수급대상자' if op.and_(op.le(income,tgIncome),
                            op.eq(isOther,2)) else '수급 비대상자'


# 수온 계산기

depth = float(input('수심을 입력하세요 (m): '))

temperature = 20
drop = 0.7

temperature = temperature - (depth // 10) * drop

print(f'수심 {depth}m에서의 수온은 {temperature:.2f}도 입니다.')


import operator as op

basetemp = 20

depps = int(input('수심을 입력하세요 : '))
#temp = basetemp - (depps // 10 * 0.7)
temp = (op.sub(basetemp,
        op.mul(op.floordiv(depps , 10) , 0.7)))

print(f'수심 {depps}m - 수온 {temp}℃')

# 자동차 주행거리 계산
import  operator as op

speed = int(input('주행속도:'))
time = int(input('주행시간:'))

# dist = speed * time
dist = op.mul (speed , time)


print(f'주행거리는 :{dist} Km')

# 컴퓨터 업무 수량 파악
# 3 * 8 = comp * time
# comp = 3 * 8 / time

worktime = int(input('근무시간을 입력하세요'))

# comp = 3 * 8 // worktime
# etcComp = 1 if (3 * 8 % worktime) > 0 else 0

expr1 = op. mul (3,8)
comp = op.floordiv(expr1 , worktime)
etcComp = 1 if (op.mod(expr1, worktime)  > 0) else 0

print(f'필요한 컴퓨터 : {comp + etcComp}')
