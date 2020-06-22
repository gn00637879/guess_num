import random
start = int(input('請輸入範圍起始值:'))
end = int(input('請輸入範圍結束值:'))
r = random.randint(start, end)
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
