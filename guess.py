import random

r = random.randiant(1,100)
count = 0
while True: 
	count = count + 1# count += 1
	num = input('请输入数字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('这是你猜的第'，count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这是你猜的第'，count, '次')
