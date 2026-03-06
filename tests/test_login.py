# from selenium import webdriver
# from Pages.practice_login import LoginPage
# from Pages.successful_page import LogoutPage
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://practicetestautomation.com/practice-test-login/')
# driver.maximize_window()
#
# def test_successful_login():
#     login_obj = LoginPage(driver)
#     logout_obj = LogoutPage(driver)
#
#     login_obj.enter_username('student')
#     login_obj.enter_password('Password123')
#     login_obj.click_login()
#
#     assert "Successfully" in logout_obj.success_msg(), "Not successful...try again"
#     logout_obj.click_logout()

#----------------------------------------------------------------------------------------

from Pages.practice_login import LoginPage
from Pages.successful_page import LogoutPage

def test_successful_login(setup_and_teardown):
    login_obj = LoginPage(setup_and_teardown)
    logout_obj = LogoutPage(setup_and_teardown)

    login_obj.enter_username('student').
    login_obj.enter_password('Password123')
    login_obj.click_login()

    assert "Successfully" in logout_obj.success_msg(), "Not successful...try again"
    logout_obj.click_logout()


