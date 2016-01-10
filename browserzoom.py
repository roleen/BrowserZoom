#!/usr/bin/env python

from pyvirtualdisplay import Display
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

SCREEN_WIDTH = 2880
SCREEN_HEIGHT = 1880
URL = "http://www.google.com"
SHORT_WAIT = 5
ZOOM_TIMES = 7

def start_browser():
	'''() -> list
	Starts virtual display and browser and returns display object
	and selenium webdriver for the browser.
	'''
	print("Starting virtual display...")
	display = Display(visible=0, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
	display.start()
	print("Starting browser...")
	browser = webdriver.Firefox()
	browser.set_window_size(SCREEN_WIDTH, SCREEN_HEIGHT)
	print("Browser ready.")
	
	return [display, browser]


def quit_browser(display, browser):
	'''(Display, webdriver) -> None
	Quits webdriver browser and stops virtual display display.
	'''
	print("Quitting browser.")
	browser.quit()
	print("Stopping virtual display.")
	display.stop()


def load_page(browser):
	'''(webdriver) -> None
	Loads the URL into the webdriver browser.
	'''
	print("Loading " + URL + ' ...')
	browser.get(URL)
	time.sleep(SHORT_WAIT)
	

def browser_zoom(browser, times):
	'''(webdriver, int) -> None
	Does the keypress CONTROL+ADD times number of times on the 
	webdriver browser.
	'''
	print("Zooming " + str(times)  + " times...")
	for i in range(times):
		ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.ADD).key_up(Keys.CONTROL).perform()


def save_image(browser):
	'''(webdriver) -> None
	Saves the screenshot of the browser page in the images folder.
	'''
	print("Saving screenshot...")
	browser.save_screenshot("./images/fullpage.png")



if(__name__ == '__main__'):
	
	display, browser = start_browser()
	
	load_page(browser)

	browser_zoom(browser, ZOOM_TIMES)
	
	save_image(browser)
	
	quit_browser(display, browser)
