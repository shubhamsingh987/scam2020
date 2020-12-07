import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import names
import random
from db import update
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')

gender=random.choice(['male','female'])
firstname=names.get_first_name(gender)
lastname=names.get_last_name()
email=firstname+lastname+str(random.randint(99,990))
password='Googlegoogle69'
mobile='+918840328651'
loc='US'
stat='unknown'
update(firstname,lastname,email,password,mobile,loc,gender,stat)
user = driver.find_element_by_name("firstName")
user.send_keys(firstname)

user = driver.find_element_by_name("lastName")
user.send_keys(lastname)

user = driver.find_element_by_name("Username")
user.send_keys(email) 

user = driver.find_element_by_name("Passwd")
user.send_keys(password)

user = driver.find_element_by_name("ConfirmPasswd")
user.send_keys(password)

element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#accountDetailsNext > div > button > div.VfPpkd-RLmnJb')))
element.click()

element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#phoneNumberId')))
element.send_keys(mobile)

element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button > div.VfPpkd-RLmnJb')))
element.click()






