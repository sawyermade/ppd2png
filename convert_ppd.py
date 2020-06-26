import pyautogui, sys, time, os

def cvt_png(coord_list):
	button = (coord_list[0], coord_list[1])
	tl, tr = (coord_list[2], coord_list[3]), (coord_list[4], coord_list[5])
	br, bl = (coord_list[6], coord_list[7]), (coord_list[8], coord_list[9])
	w, h = tr[0] - tl[0], bl[1] - tl[1]

	if not os.path.exists('output'):
		os.makedirs('output')

	pyautogui.click(x=button[0], y=button[1])
	for i in range(1151):
		time.sleep(2)
		pyautogui.click(x=button[0], y=button[1])
		
		fname = str(i + 1).zfill(4) + '.png'
		pyautogui.screenshot(os.path.join('output', fname), region=(tl[0], tl[1], w, h))

def main():
	coord_list = [int(a) for a in sys.argv[1:]]
	cvt_png(coord_list)

if __name__ == '__main__':
	main()