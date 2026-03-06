from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get('https://practicetestautomation.com/practice-test-login/')
driver.maximize_window()
#
wait = WebDriverWait(driver,5)
action=ActionChains(driver)


# username = driver.find_element(By.ID,'username')
# print(username.get_dom_attribute("id"))
username = wait.until(EC.visibility_of_element_located((By.ID,'username')))


username.send_keys('student')
password = driver.find_element(By.ID,'password')
password.send_keys('Password123')
login_button = driver.find_element(By.ID,'submit')
login_button.click()

driver.quit()

# #----------------------------------------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://practicetestautomation.com/practice-test-login/')
# driver.maximize_window()
#
# class LoginPage:
#     def enter_username(self,username):
#         driver.find_element(By.ID,'username').send_keys(username)
#
#     def enter_password(self,passkey):
#         driver.find_element(By.ID,'password').send_keys(passkey)
#
#     def click_login(self):
#         driver.find_element(By.ID,'submit').click()
#
# login_obj = LoginPage()
# login_obj.enter_username('student')
# login_obj.enter_password('Password123')
# login_obj.click_login()

#---------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By
# class LoginPage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def enter_username(self,username):
#         self.driver.find_element(By.ID,'username').send_keys(username)
#
#     def enter_password(self,passkey):
#         self.driver.find_element(By.ID,'password').send_keys(passkey)
#
#     def click_login(self):
#         self.driver.find_element(By.ID,'submit').click()

#create requirements.txt
#python -m venv venv
#venv\Scripts\activate
#pip install -r requirements.txt
#deactivate

#---------------------------------------------------------------------------------------------------------
# from selenium.webdriver.common.by import By
# from Pages.base_page import BasePage
#
#
# class LoginPage(BasePage):
#     usernameloc = (By.ID,'username')
#     passwordloc = (By.ID,'password')
#     logibutton = (By.ID,'submit')
#
#     def __init__(self,driver):
#         super().__init__(driver)
#
#     def enter_username(self,username):
#         self.enter_text(self.usernameloc,username)
#
#     def enter_password(self,passkey):
#         self.enter_text(self.passwordloc,passkey)
#
#     def click_login(self):
#         self.click_button(self.logibutton)



