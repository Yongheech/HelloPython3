# 실전예제 1
email = 'gildong@abc.com'
name = '홍길동'
userid = 'gildong'
passwd = '1234'


# print(f'To.{email}')
# print('▶ 아이디 및 비밀번호 확인')
# print(f'{name} 고객님 안녕하세요.' )
# print(f'{name} 고객님의 아이디와 비밀번호는 아래와 같습니다.')
# print(f' 아이디 : {userid}')
# print(f' 비밀번호 : {passwd}')


print(f'''To.{email}')
▶ 아이디 및 비밀번호 확인'
{name} 고객님 안녕하세요.' 
{name} 고객님의 아이디와 비밀번호는 아래와 같습니다.'
아이디 : {userid}'
비밀번호 : {passwd}''')


# 실전예제 2


# riseSun = '오전 6시 30분'
# dawnSun = '오후 7시 20분'
# day = '월'
# monthDay = '3월 30일'
# morningTemp = '-1'
# daytimeTemp = 10
# percentage = 45
# southSea = 0.5
# eastSea = 1.5
# westSea = 0.5
# status = '좋음'


# print('내일 날씨 예보입니다.')
# print(f'{day}요일인 {monthDay}의 아침 최저 기온은 {morningTemp}도, 낮 최고 기온은 {daytimeTemp}도로 예보됐습니다.')
# print(f'비올 확률은 {percentage}%이고, 미세먼지는 {status} 수준일 것으로 예상됩니다.')
# print(f'일출시간은 {riseSun}이고, 일몰시간은 {dawnSun}입니다')
# print(f'바다의 물결은 남해 앞바다 {southSea}m, 동해 앞바다 {eastSea}m, 서해 앞바다 {westSea}m 높이로 일겠습니다.')
# print(f'지금까지{monthDay} {day}요일 날씨 에보였습니다.')


day = input('요일은?')
date = input('날짜(월일)는?')
minTemp = input('최저 기온은?')
maxTemp = input('최대 기온은?')
rainy = input('비올확률은?')
dasty = input('미세먼지는?')
riseSun = input('일출시간은?')
dawnSun = input('일몰시간은?')
southWave = input('남해 물결높이는?')
eastWave = input('동해 물결높이는?')
watsWave = input('서해 물결높이는?')


print(f'''내일 날씨 예보입니다.')
{day}요일인 {date}의 아침 최저 기온은 {minTemp}도, 낮 최고 기온은 {maxTemp}도로 예보됐습니다.
비올 확률은 {rainy}%이고, 미세먼지는 {dasty} 수준일 것으로 예상됩니다.
일출시간은 {riseSun}이고, 일몰시간은 {dawnSun}입니다
바다의 물결은 남해 앞바다 {southWave}m, 동해 앞바다 {eastWave}m, 서해 앞바다 {watsWave}m 높이로 일겠습니다.
지금까지{date} {day}요일 날씨 예보였습니다.''')



# 영수증 예제 직접 풀어본 풀이

# food = '소주'
# food2 = '너나치킨'
# totalTax = '과세합계'
# vat = '부가세'
# total = '총합계'
# amounTreceived = '받은금액'
# changes = '잔돈'
#
# print('[ 음식나라 ]')
#
# print('---------------------')
#
# print(f'{food}     2 '     ,   3000+3000)
# print(f'{food2}    1           12000')
#
# print('---------------------')
#
# print(f'{totalTax}       16200 ')
# print(f'{vat}            1800 ')
#
# print('---------------------')
#
# print(f'{total} ',           6000+12000)
# print(f'받은금액 ' ,           50000 )
# print(f'{changes} ' ,        50000-18000)
#
# print('---------------------')
#
# print('2014. 07. 07 14:35:24')

date = '2014. 07. 07 14:35:24'
soju = 2
chiken = 1

total = (soju * 3000) + (chiken * 12000)
vat = total * (10/110)  # 부가세 = 합계급액 * 10/110
supply = total * (100/110) # 공급가액 = 합계금액 * 100/110
paid = 50000
change = paid - total

print(f'''
[음식나라]

-------------------------
소주\t\t{soju}\t\t{soju * 3000}
너나치킨\t{chiken}\t\t{chiken * 12000} 
-------------------------
과세합계\t\t\t{int(supply)}
부가세\t\t\t{int(vat)}
-------------------------
총합계\t\t\t{total}
받은금액\t\t\t{paid}
잔돈\t\t\t\t{change}
-------------------------
{date}
''')




#3 다음 중 파이썬 변수로 사용 가능한 것은 무엇인지 서술하여라.
rate1 = 123
# 1stPlayer = 456
# myprogram.java = 789
long = 987
# except = 654
TimeLimit = 321
numberOfWindows = 1000

#11. 이름과 몸무게, 나이를 변수로 선언하고 자신의 것을 값으로 초기화 하는 프로그램을 작성하여라
name = '일지매'
weight = 45.5
age = 35

print(name, weight, age)

#12. 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라, (MyAge)
# 연나이 계산 : 현재년도 - 태어난년도 (병역법, 교육법, 민방위)
# 만나이     : 현재년도 - 태어난년도, 생일안지남 (-1) (민법상, 2023-06부터)
# 한국식 나이 : 현재년도 - 태어난년도 +1
currentYear = int(input('현재년도는?'))
birthYear = int(input('생일의 년도는?'))
myAge = currentYear - birthYear

print(f'''현재년도는 {currentYear}이고, 
생일의 년도가 {birthYear}일 때,
나이는  {myAge} 입니다.''')


#13 - 구구단 출력

# print('7 X 1 = 7')
# print('7 X 2 = 14')
# print('7 X 3 = 21')
# print('7 X 4 = 28')
# print('7 X 5 = 35')
# print('7 X 6 = 42')
# print('7 X 7 = 49')
# print('7 X 8 = 56')
# print('7 X 9 = 63')

dan = 7

# print(f'{dan} X 1 = {dan * 1}')
# print(f'{dan} X 2 = {dan * 2}')
# print(f'{dan} X 3 = {dan * 3}')
# print(f'{dan} X 4 = {dan * 4}')
# print(f'{dan} X 5 = {dan * 5}')
# print(f'{dan} X 6 = {dan * 6}')
# print(f'{dan} X 7 = {dan * 7}')
# print(f'{dan} X 8 = {dan * 8}')
# print(f'{dan} X 9 = {dan * 9}')

print(f'''
      {dan} X 1 = {dan * 1}')
{dan} X 2 = {dan * 2}
{dan} X 3 = {dan * 3}
{dan} X 4 = {dan * 4}
{dan} X 5 = {dan * 5}
{dan} X 6 = {dan * 6}
{dan} X 7 = {dan * 7}
{dan} X 8 = {dan * 8}
{dan} X 9 = {dan * 9}''')
