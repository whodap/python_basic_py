"""
a = [1, 2, 3]
print(type(a))

a = [1,2,3]
b = a
a[1] = 4
c = a is b
print(c)

#p.67
a = 'hobby'
print(a.count('b'))

#p.104

a = [1, 2, 3, 4]
while a:
    print(a.pop())


#p.105
# 만약 [1,2,3]이 참이면, "참"이라는 문자열을 출력하고 그렇지 않으면 "거짓"이라는 문자열을 출력하라

if [1, 2, 3]:
    print("참")
else :
    print("거짓")

#p.111
a = 3
b = 5
a, b = b, a
print(a)
print(b)


#p.117
money = True

if not money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#p.117
money = 3000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#p.123
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

"""
#p.138



