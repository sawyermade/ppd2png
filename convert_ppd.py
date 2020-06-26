import pyautogui, sys, time, os

def cvt_png(coord_list):
	button = (coord_list[0], coord_list[1])
	tl, tr = (coord_list[2], coord_list[3]), (coord_list[4], coord_list[5])
	br, bl = (coord_list[6], coord_list[7]), (coord_list[8], coord_list[9])
	fx, fy = coord_list[10], coord_list[11]
	w, h = tr[0] - tl[0] + 5, bl[1] - tl[1] + 5

	if not os.path.exists('output'):
		os.makedirs('output')

	pyautogui.click(x=fx, y=fy)
	fname = str(1).zfill(4) + '.png'
	pyautogui.screenshot(os.path.join('output', fname), region=(tl[0], tl[1], w, h))
	for i in range(1, 1151):
		time.sleep(2)
		pyautogui.click(x=button[0], y=button[1])
		fname = str(i + 1).zfill(4) + '.png'
		pyautogui.screenshot(os.path.join('output', fname), region=(tl[0], tl[1], w, h))

def main():
	coord_list = [int(a) for a in sys.argv[1:]]
	cvt_png(coord_list)

if __name__ == '__main__':
	main()