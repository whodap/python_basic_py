"""
# 연습문제 2_1 키보드로  출생년을 입력 받아 나이 계산하기
name = input('당신의 이름은? ')
birth = int(input('당신의 태어난 해는? '))

age = 2021 - birth
print(name + '님의 나이는 ' + str(age) + '세 입니다!')


# 연습문제 2_2 키보드로 년,월,일을 입력 받아 화면에 출력하기(기본)
a = input('년 : ')
b = input('월 : ')
c = input('일 : ')

print('your ' + 'b-day ' + str(a), str(b), str(c), sep='-')


# 연습문제 2_3 물건가격, 구매개수, 지불금액 등을 입력 받아 거스름돈을 계산

price = int(input('물건 가격 : '))
num = int(input('구매 개수 : '))
pay = int(input('지불 금액 : '))
change = pay - price * num
print(('물건 가격 : %d, 구매 개수 : %d, 지불금액 : %d => 거스름 돈 : %d') % (price, num, pay, change))
# print('물건 가격 : {0}, 구매 개수 : {1}, 지불 금액 : {2} => 거스름 돈 : {3} '.format(price, num, pay, change))


# 논리연산자 : or 활용
x = 20
if x %2 == 0 or x %3 == 0 :
    print('True')

else :
    print('False')

y = 11
if y %2 == 0 or x%3 == 0 :
    print('True')

else : 
    print('False')



# If~ 구문을 이용한 영어 단어 퀴즈(기본대로)

ans1 = input('"사자"의 영어 단어는 무엇일까요? ')

if ans1 == str('lion') :
    print('딩동댕! 참 잘했어요 ~~ ')
else :
    print('땡! 틀렸습니다. ')

print('===' * 50)

ans2 = input('"기차"의 영어 단어는 무엇일까요? ')

if ans2 == str('train') :
    print('딩동댕! 참 잘했어요 ~~ ')
else :
    print('땡! 틀렸습니다. ')



# If~ 구문을 이용한 영어 단어 퀴즈(응용)

ans1 = input('"사자"의 영어 단어는 무엇일까요? ')
result = '땡 틀렸습니다.'

if ans1 == 'lion' :
    result = '딩동댕! 참 잘했어요 ~~ '
print(result)

ans2 = input('"기차"의 영어 단어는 무엇일까요? ')
result = '땡 틀렸습니다.'
if ans2 == 'train' :
    result = '딩동댕! 참 잘했어요 ~~ '
print(result)


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
user = input('input ID : ')
if user == 'admin':
    print('contents availabe!')
else:
    level = int(input('wirte user level: '))
    if level>=1 and level<=7:
        print('contents availabe!')
    else:
        print('sorry, Not availabe contents, please call OP!')


###### 4. FOR, WHILE ######

# for문 돌리기

for x in range(5):
    print('Hello!')


# 각 반복 루프의 변수 값
sum = 0
for x in range(1, 11) : 
    sum = sum + x
    print(x, sum)


# For문에서 range 합

for w in range(1,10,2):
    print(w)

print('=' * 20)

for x in range(20,0,-2):
    print(x)

print('=' * 20)

for y in range(10):
    print(y)

print('=' * 20)

for z in range(1, 10):
    print(z)

"""
# 연습 문제 4-1. 100~300 까지의 수 중에서 5의 배수의 합
sum = 0
for i in range(100, 301, 5):
    sum = sum + i
    print(i)
print('100 ~ 300의 정수 중에서 5의 배수의 합계 : %d' % sum)


# 연습 문제 4-2. 1~1000 까지의 수 중에서 5의 배수의 합, 단 10의 배수 제외
# 추가조건 : 단, 10의 배수는 제외

for x in range(0, 1001, 5):
    if x %10 == 0:
# x를 10으로 나누었을 때 나머지가 0과 같다
# 10의 배수이므로 print까지 가지말고 위에서 다시 시작해라 => continue
        continue
    print(x)
    pass


# 추가 예제

# 입력받은 데이터 (hello world) 포문을 사용해서 하나의 문자씩 출력
# hello world 중에 h만 출력
# 단, 지금 작성한 코드에서 한 줄말 추가하여야 함
# h 대신, hello까지만 나오고 공백에 빠져나올 수 있게 변환

word = input('English sentense write : ')

for t in word :
    print(t)
    if t == ' ':
        break
    pass
pass

"""

# 2차원 배열을 생성하고 출력해보세요

w = ["1", "2", "3", "4"]
print(w.index(4))
print('end')

x = [[1,1,1], [2,2,2], [3,3,3]]
#y = []
for x1 in x:
    print('x1' % x)

"""
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
