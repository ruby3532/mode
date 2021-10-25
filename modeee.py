# while 的應用
while True:
	mode = input('請輸入遊戲模式: ')
	if mode == 'q':
		break
	elif mode == '1':
		print('啟動遊戲模式 1')
	elif mode == '2':
		print('啟動遊戲模式 2')
	else:
		print('麻煩輸入 1/2/q')
