# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class RegistrationNewWM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Progs\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://web.cpa-dev.safesocks.ru"
        self.verificationErrors = []
        self.accept_next_alert = True

        #Test data
        self.name = "some name"
        self.email = "test12@ukr.net"
        self.password = "qwerty"
        self.skype = "everad_test"
        self.wmr = "R034873236762"
        self.adminLogin = "admin@example.com"
                
    def test_1_registration_new_wm_with_valid_data(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Я веб-мастер").click()
        driver.find_element_by_css_selector("a.sign_button.registration-link").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(self.name)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(self.email)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(self.password)
        driver.find_element_by_id("repeat_password").clear()
        driver.find_element_by_id("repeat_password").send_keys(self.password)
        driver.find_element_by_id("skype").clear()
        driver.find_element_by_id("skype").send_keys(self.skype)
        driver.find_element_by_id("wmr").clear()
        driver.find_element_by_id("wmr").send_keys(self.wmr)
        driver.find_element_by_css_selector("input.send_button.send_if_checked").click()
        driver.find_element_by_css_selector("input.send_button.send_if_checked").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.registration-finished"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print("registration_new_wm_with_valid_data FAILED")
        else: print("registration_new_wm_with_valid_data PASSED")
        
    def test_2_activate_new_wm_in_adminPage(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(self.adminLogin)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("test")
        driver.find_element_by_css_selector("input.submit.enter_btn").click()
        driver.find_element_by_css_selector("div.dropdown-toggle.nav-item").click()
        driver.find_element_by_link_text(u"Партнеры").click()
        try: driver.find_element_by_xpath("//div[@id='advertisers-list']/div/div[2]/div/div/table/tbody/tr/td[10]/div/button[3]").click()
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print("activate_new_wm_in_adminPage FAILED")
        else: print("activate_new_wm_in_adminPage PASSED")
        
    def test_3_enter_wm_after_activate(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(self.email)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_css_selector("input.submit.enter_btn").click()
        for i in range(60):
            try:
                if u"Партнёрская сеть" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Партнёрская сеть", driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))  
            print("enter_wm_after_activate FAILED")
        else: print("enter_wm_after_activate PASSED")
  
    def test_payment_WM_balance(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_link_text(u"Финансы").click()
        driver.find_element_by_xpath("//div[@id='content']/div/div/div/div/div/button").click()
        driver.find_element_by_name("amount").clear()
        driver.find_element_by_name("amount").send_keys("1000000")
        driver.find_element_by_name("comment").clear()
        driver.find_element_by_name("comment").send_keys(u"на хлеб")
        driver.find_element_by_xpath("//div[@id='1']/form/footer/button").click()
        driver.find_element_by_id("logout").click()
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(self.email)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_css_selector("input.submit.enter_btn").click()
        try: self.assertEqual(u"2000000.00P–", driver.find_element_by_xpath("//div[@id='page-home']/div/div/header/div/div[2]/div[3]/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    '''def post_conditions(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("admin@example.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("test")
        driver.find_element_by_css_selector("input.submit.enter_btn").click()
        driver.find_element_by_css_selector("div.dropdown-toggle.nav-item").click()
        driver.find_element_by_link_text(u"Партнеры").click()
        driver.find_element_by_xpath("//div[@id='advertisers-list']/div/div[2]/div/div/table/tbody/tr/td[10]/div/button[4]").click()
        driver.find_element_by_xpath("//div[@id='1']/form/footer/button").click()'''
                
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
