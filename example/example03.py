# 26 결혼여부 입력 세금율
isMarried = int(input('결혼여부는? 0:미혼, 1:기혼'))
salary = int(input('연봉은?'))

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

# 27
# 1992, 2000, 2020 (윤)
# 1900, 2100 (윤x)
year = int(input('년도는?'))

isLeap = '윤년아님!'

cond1 = (year % 4 == 0 and year % 100 != 0)
cond2 = (year % 400 == 0)
if cond1 or cond2 : isLeap = '윤년 맞음!@@'

print(f'{year} 년은 {isLeap} ')


# 28
# dan = int(input('1부터 9까지의 숫자를 입력하세요 :'))
dan = input('1부터 9까지의 숫자를 입력하세요 :')

result = '잘못 입력하셨습니다'
# if dan > 0 and dan <= 9:
if (dan.isdigit()) and (0 < int(dan) <= 9):
    result = f'{dan} x 1 = {dan * 1}\n'
    result += f'{dan} x 2 = {dan * 2}\n'
    result += f'{dan} x 3 = {dan * 3}\n'
    result += f'{dan} x 4 = {dan * 4}\n'
    result += f'{dan} x 5 = {dan * 5}\n'
    result += f'{dan} x 6 = {dan * 6}\n'
    result += f'{dan} x 7 = {dan * 7}\n'
    result += f'{dan} x 8 = {dan * 8}\n'
    result += f'{dan} x 9 = {dan * 9}'

print(result)


# 33
cardno = int(input('카드번호는?'))

result = '잘못된 카드 번호입니다'
if cardno ==  356317:  result = 'JCB카드 NH농협카드'
elif cardno == 356901: result = 'JCB카드 신한카드'
elif cardno == 356912: result = 'JCB카드 KB국민카드'
elif cardno == 404825: result = '비자카드 비씨카드'
elif cardno == 438677: result = '비자카드 신한카드'
elif cardno == 515594: result = '마스터카드 신한카드'
elif cardno == 524353: result = '마스터카드 외환카드'
elif cardno == 540926: result = '마스터카드 KB국민카드'

print(result)


# 35
daytime = input('시간때는?')

result = '잘못 입력하셨습니다'
if daytime == 'morning hour' : result = '아침시간 (7-12)'
elif (daytime == 'midday') or (daytime == 'noon') : result = '점심시간 (12-1)'
elif (daytime == 'midday') or (daytime == 'daybreak') : result = '시간 (12-1)'
elif (daytime == 'midday') or (daytime == 'daybreak') : result = '시간 (12-1)'
elif (daytime == 'midday') or (daytime == 'daybreak') : result = '시간 (12-1)'
elif (daytime == 'midday') or (daytime == 'daybreak') : result = '시간 (12-1)'
elif (daytime == 'midday') or (daytime == 'daybreak') : result = '시간 (12-1)'
elif (daytime == 'midday') or (daytime == 'daybreak') : result = '시간 (12-1)'


print(f'{daytime} / {result}')