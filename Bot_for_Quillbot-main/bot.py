from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import os
import time
path = "C:\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = path
driver = webdriver.Chrome(path)
fname = r"C:\\Users\\Omen\\Downloads\\Bot_for_Quillbot-main\\Bot_for_Quillbot-main\\cp.txt"
wname = r"C:\\Users\\Omen\\Downloads\\Bot_for_Quillbot-main\\parapharased.txt"
w = open(wname, "w+")
fh = open(fname)
i=0
for line in fh:
	if(i!=0):
		driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[i])
	driver.get("http://www.quillbot.com")
	print("Copying Paragraph: %d" %(i+1))
	driver.find_element(By.ID,"inputText").send_keys(line)
	driver.find_element(By.XPATH, '//button/parent::div[@class="MuiGrid-root css-rfnosa"]').click()
	i = i+1
i=0
f = open(fname)
for line in f:
	driver.switch_to.window(driver.window_handles[i])
	wait = WebDriverWait(driver, 80, poll_frequency=1,
							ignored_exceptions=[NoSuchElementException,
												ElementNotVisibleException,
												ElementNotSelectableException])
	Element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="articleTextArea"]')))
	print("Pasting Paragraph: %d" %(i+1))
	quilled = driver.find_element(By.XPATH, '//div[@id="articleTextArea"]')
	w.write(quilled.text)
	w.write("\n")
	i=i+1

#driver.quit()
	

#chromeTest.test()	






