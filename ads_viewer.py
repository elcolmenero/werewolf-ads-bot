from pynput.mouse import Button, Controller
import time
import PIL.ImageGrab

mouse 		= Controller()

# Click Function
def click_sys(coor, button, times):
	mouse.position = coor
	mouse.press(button)
	mouse.release(button)
	time.sleep(times)

# Ammount of Video To View
loop = 100


for x in range( loop ):
	print(x)
	
	print('Clicking See Video')
	for y in range(580, 782, 3):
		color = PIL.ImageGrab.grab().load()[1212,y]
		r,g,b = color[0], color[1], color[2]
		if r >= 240:

			click_sys((1209, y+5),Button.left,0.5)

			break

	print('Waiting Video to Stop')
	time.sleep(35)

	print('Clicking Close VideoAD')
	click_sys((1322, 250),Button.left,0.5)

	print('Clicking Get Recompensa')
	for y in range(580, 782, 3):
		color = PIL.ImageGrab.grab().load()[1212,y]
		r,g,b = color[0], color[1], color[2]

		if r >= 240:
			click_sys((1209, y+5),Button.left,0.5)
			break

	print('Waiting For it Stop')
	time.sleep(15)
