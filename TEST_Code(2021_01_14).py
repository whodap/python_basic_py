
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


#6-1 함수 매개변수 활용
def test(start, end):
    hap = 0
    for i in range(start, end+1):
        hap = hap + i
        print('%d ~ %d의 정수의 합계 : %d' % (start, end, hap))

test(1, 10)
test(200, 200)
print("end")

"""
#6-2 함수리턴값 활용
def function_hap(start, end):
    hap = 0
    for i in range(start, end+1):
        hap = hap + i
        print('%d ~ %d의 정수의 합계 : %d' % (start, end, hap))
    return hap


result = function_hap(200, 200) + function_hap(1, 10) - 5
print(result)
print("end")

# 파일 쓰기
file = open('sample.txt', 'w') 
for i in range(0, 3, 1): 
    print(i) 
    file.write(str(i))
file.close()
print("end")

# 파일 읽기
file = open('sample.txt', 'r') 
for i in file.readline(): 
    print(i) 
file.close()
print("end")


# 클래스 생성
class Room():
    status = 'clean'

    def __init__(self):
        print('new room')

    def clean(self):
        self.status = 'clean'

    def openPartry(self):
        self.status = 'not clean'

# 클래스로 객제 생성
room1 = Room() # Room 을 객체로 받은 room1 생성

print(room1)
print(room1.status)

# 파티를 해서 청소 필요
room1.openPartry() 
print(room1.status)

# 청소함
room1.clean()

# 이제 깨끗함
print(room1.status)
print('end')

#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926
# 사용자 정의 모듈 임포트
from module.item import Car

# 클래스로 인스턴스(객채 생성)
item = Car()

print(item)
print(item.category)
print(item.number)
item.update()
print(item.number)
print("end")