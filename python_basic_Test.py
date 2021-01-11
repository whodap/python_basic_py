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
change 	= pay - price * num
# print('물건 가격 : %d, 구매 개수 : %d, 지불 금액 : %d => 거스름 돈 : %d ') % (price, num, pay, change))
print('물건 가격 : {0}, 구매 개수 : {1}, 지불 금액 : {2} => 거스름 돈 : {3} '.format(price, num, pay, change))