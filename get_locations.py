import pyautogui, sys

def get_ss(fname='temp.png'):
	im = pyautogui.screenshot(fname)

def get_pos():
	try:
		while True:
			x, y = pyautogui.position()
			positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
			print(positionStr, end='')
			print('\b' * len(positionStr), end='', flush=True)

	except KeyboardInterrupt:
		print('\n')

def main():
	print(pyautogui.size())
	get_pos()
	get_ss()

if __name__ == '__main__':
	main()