from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("https://www.humanity.com/app/") #Open browser to the login page

driver.implicitly_wait(55) #sekunde

driver.find_element_by_name("email").send_keys("ninatest") #Fill in sername
driver.find_element_by_name("password").send_keys("30stepeni") #Fill in password

driver.find_element_by_name("login").click()

# Opening an account => staff
time.sleep(10)
driver.find_element_by_id("sn_staff").click()

# Opening Add Employees
time.sleep(5)
driver.find_element_by_xpath("//*[@id=\"act_primary\"]").click()

# Entering information for the employee
time.sleep(5)
driver.find_element_by_id("_asf1").send_keys("Maja") #Fill in name
driver.find_element_by_id("_asl1").send_keys("Pcelica") #Fill in Last name
driver.find_element_by_id("_ase1").send_keys("p.maja@gmail.com") #Fill in E-mail

# Confirming entry => Save Employees
driver.find_element_by_id("_as_save_multiple").click()

# Opening => Time Clock
driver.find_element_by_id("sn_timeclock").click()

# Clock IN
time.sleep(2)
driver.find_element_by_id("tc_tl_ci").click()

# Clock OUT
time.sleep(5)
driver.find_element_by_id("tc_tl_co").click()