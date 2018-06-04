import time
import pyautogui

#### INSTRAGRAM LIKER 1.0 ####

pyautogui.hotkey('alt', 'tab') #switch to instagram where image is opened
for z in range(0,1000): #specify number of images to scroll(change 100) 
	#time.sleep(0.5) #set processing time according to your pc & internet speed. 
	if (pyautogui.locateOnScreen('instaCheck.png')) != None: #check image is liked or not
		#pyautogui.doubleClick()
		#pyautogui.moveTo(pyautogui.locateCenterOnScreen('instaCheck.png'))
		#pyautogui.rightClick()
		#print('centre')
		x,y = pyautogui.locateCenterOnScreen('instaCheck.png')
		pyautogui.moveTo(x,y)
		pyautogui.click()
		#time.sleep(0.2) 
		pyautogui.scroll(-700)

		#set processing time according to your pc & internet speed.
	else:
		pyautogui.scroll(-500)
	#pyautogui.press('right') #move to next image    	

#basic functionality for now.
#STEPS > 
#open instagram with the first image of a page to like
#alt tab to cmd where u run the script
#voila
#MAKE SURE TO PLACE MOUSE ON IMAGE then ALT TAB to CMD and then without changing mouse position run script
