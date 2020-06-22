import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = int(input('請猜數字:'))
	if r == num:
		print('終於猜對了')
		print('總共猜了',count,'次')
		break
	elif num < r :
		print('比答案小')
	else:
		print('比答案大')
	print('這是您猜的第', count, '次')
