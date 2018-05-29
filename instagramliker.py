import time
import pyautogui

#### INSTRAGRAM LIKER 1.0 ####

pyautogui.hotkey('alt', 'tab') #switch to instagram where image is opened
for z in range(0,100): #specify number of images to scroll(change 100) 
    time.sleep(0.5) #set processing time according to your pc & internet speed. 
    #if (pyautogui.locateOnScreen('heartButtonOnInsta.png')) != None: #check image is liked or not
    pyautogui.Click()
    pyautogui.Click() # double click to like insta images on website
    pyautogui.press('right') #move to next image
    time.sleep(0.2) #set processing time according to your pc & internet speed.

#basic functionality for now.
#STEPS > 
#open instagram with the first image of a page to like
#alt tab to cmd where u run the script
#voila
