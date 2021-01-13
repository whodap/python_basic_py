"""
#2-1

name = input('당신의 이름은? ')
birth = int(input('당신의 태어난 해는? '))

age = 2022 - birth
print(name + '님의 나이는 ' + str(age) + '세 입니다!')


#2-3

price = int(input('물건 가격 : '))
num = int(input('구매 개수 : '))
pay = int(input('지불 금액 : '))
change = pay - price * num
# print(('물건 가격 : %d, 구매 개수 : %d, 지불금액 : %d => 거스름 돈 : %d') % (price, num, pay, change))
print('물건 가격 : {0}, 구매 개수 : {1}, 지불 금액 : {2} => 거스름 돈 : {3} '.format(price, num, pay, change))


#3-1
num = int(input('정수를 입력하세요 : '))

result = '입력된 정수는 100 ~ 1000 사이에 있지 않습니다!'
if num >= 100 and num <= 1000 :
    result = '입력된 정수는 100 ~ 1000사이에 있습니다!'

print('입력된 정수 : %d' % num)
print(result)


#3-2
char = input('영어 소문자 하나를 입력하세요 : ')
if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') :
    print('%s -> 모음' % char)
else :
    print('%s -> 자음' % char)

#3-3
height = int(input('키를 입력해 주세요 : ')) 
weight = int(input('몸무게를 입력해 주세요 : '))

s = (height - 100) * 0.9;  
print('=' * 50)
print('키 : ', height)
print('몸무게 : ', weight)
if weight > s :
    print('비만입니다, 다이어트가 필요합니다!')  
else :
    print('표준 또는 마른 체형입니다!')

print('=' * 50)

#3-4
month = int(input('please write Month :'))

if month >= 3 and month <= 5 :
    season = 'spring'
    print(month, 'Month', 'is', season, sep='')

elif month >= 6 and month <= 8 :
    season = 'summer'
    print(month, 'Month', 'is', season, sep='')

elif month >= 9 and month <= 11 :
    season = 'fall'
    print(month, 'Month', 'is', season, sep='')

#3-5
price = int(input('물건 구매가를 입력하세요 : '))
dis = 0
if price >= 50000 :
    dis = 0.1
elif price >= 10000 :
    dis = 0.05
elif price >= 1000 :
    dis = 0.01
else : 
    print('미지급')

print('구매가 : price %2f' % (price - (price* dis)))

#3-6
user = input('input ID')
if user == 'admin':
    print('contents availabe!')
else:
    level = int(input('wirte user level:'))
    if level>=1 and level<=7:
        print('contents availabe!')
    else:
        print('sorry, Not availabe contents, please call OP!')


#5-1

for x in [[1,1,1], [2,2,2], [3,3,3]]:
    #line = ['1', '2', '3']
    line = ""
    for y in x:
        line += str(y)
        line += "|"
        pass
    print(line)
    pass



#5-2
data = [[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]]
# data.sort()


for x in data:
    # data에 있는 요소를 하나씩 가져와서 x를 만든다
    L = []
    # append할 대상을 arrary로 지정해주기 위해 선언해준다
    for d in range((len(x)-1), -1, -1):
        # 요소에서 뒷자리부터 가져오기 위해 총 개수에서 하나를 빼면 리스트에 마지막 인덱스다, 
        # 그 인덱스를 사용해서 리스트에 요소를 하나씩 가져온다
        if x[d] % 3  == 0:
            x[d] = 0

        L.append(x[d])
        # 문자열을 더한다
    print(L)

# for x in data:
#     #line = ['1', '2', '3']
#     line = ""
#     x.sort(reverse=True)
#     print(x)
#     # for y in x.sort():
#     #     line += str(y)
#     #     line += "|"
#     # print(line)
# pass

"""

#6