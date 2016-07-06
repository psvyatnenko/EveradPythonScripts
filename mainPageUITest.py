# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class MainPageUITests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Install\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://web.cpa-dev.safesocks.ru"
        self.verificationErrors = []
        self.accept_next_alert = True
        #self.driver.maximize_window()
    
    def test_01_assert_title(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        # Assert Title
        try: self.assertEqual(u"Рекламная сеть EverAD - лучшая партнерская (CPA) сеть по продаже товаров", driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_title FAILED')
        else: print('test_assert_title PASSED')

    def test_02_assert_logo_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        # Assert Logo is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "html/body/div[3]/header/div[1]/a/img"))   
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_logo_is_present FAILED')
        else: print('test_assert_logo_is_present PASSED')
        
    def test_03_assert_wmLink_is_present(self):    
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        # Assert wmLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "ВЕБМАСТЕРУ"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_wmLink_is_present FAILED')
        else: print('test_assert_wmLink_is_present PASSED')
        
    def test_04_assert_wmLinkText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        # Assert wmLinkText is equal "ВЕБМАСТЕРУ"
        try: self.assertEqual(u"ВЕБМАСТЕРУ", driver.find_element_by_link_text(u"ВЕБМАСТЕРУ").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_wmLinkText FAILED')
        else: print('test_assert_wmLinkText PASSED')

    def test_05_assert_advLink_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        # Assert advLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"РЕКЛАМОДАТЕЛЮ"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_advLink_is_present FAILED')
        else: print('test_assert_advLink_is_present PASSED')

    def test_06_assert_advLinkText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        # Assert advLinkText is equal "РЕКЛАМОДАТЕЛЮ"
        try: self.assertEqual(u"РЕКЛАМОДАТЕЛЮ", driver.find_element_by_link_text(u"РЕКЛАМОДАТЕЛЮ").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_advLinkText FAILED')
        else: print('test_assert_advLinkText PASSED')

    def test_07_assert_aboutSystemLink_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()    
        # Assert aboutSystemLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"О СИСТЕМЕ"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_aboutSystemLink_is_present FAILED')
        else: print('test_assert_aboutSystemLink_is_present PASSED')

    def test_08_assert_aboutSystemLinkText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()          
        # Assert aboutSystemLinkText is equal "О СИСТЕМЕ"
        try: self.assertEqual(u"О СИСТЕМЕ", driver.find_element_by_link_text(u"О СИСТЕМЕ").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_aboutSystemLinkText FAILED')
        else: print('test_assert_aboutSystemLinkText PASSED')

    def test_09_assert_contactsLink_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()     
        # Assert contactsLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"КОНТАКТЫ"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_contactsLink_is_present FAILED')
        else: print('test_assert_contactsLink_is_present PASSED')

    def test_10_assert_contactsLinkText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()  
        # Assert contactsLinkText is equal "КОНТАКТЫ"
        try: self.assertEqual(u"КОНТАКТЫ", driver.find_element_by_link_text(u"КОНТАКТЫ").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_contactsLinkText FAILED')
        else: print('test_assert_contactsLinkText PASSED')
        
    def test_11_assert_enterAndRegButton_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()         
        # Assert enterAndRegButton is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Вход и регистрация"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_enterAndRegButton_is_present FAILED')
        else: print('test_assert_enterAndRegButton_is_present PASSED')
        
    def test_12_assert_enterAndRegButtonText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()     
        # Assert enterAndRegButtonText is equal "Вход и регистрация"
        try: self.assertEqual(u"Вход и регистрация", driver.find_element_by_link_text(u"Вход и регистрация").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_enterAndRegButtonText FAILED')
        else: print('test_assert_enterAndRegButtonText PASSED')

    def test_13_assert_iAmWMButton_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert iAmWMButton is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Я веб-мастер"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_iAmWMButton_is_present FAILED')
        else: print('test_assert_iAmWMButton_is_present PASSED')

    def test_14_assert_iAmWMButtonText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()         
        # Assert iAmWMButtonText is equal "Я веб-мастер"
        try: self.assertEqual(u"Я веб-мастер", driver.find_element_by_link_text(u"Я веб-мастер").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_iAmWMButtonText FAILED')
        else: print('test_assert_iAmWMButtonText PASSED')

    def test_15_assert_iAmAdvButton_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()         
        # Assert iAmAdvButton is present
        try: self.assertTrue(self.is_element_present(By.XPATH, u"(//a[contains(text(),'Я рекламодатель')])[2]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_iAmAdvButton_is_present FAILED')
        else: print('test_assert_iAmAdvButton_is_present PASSED')

    def test_16_assert_iAmAdvButtonText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert iAmAdvButtonText is equal "Я рекламодатель"
        try: self.assertEqual(u"Я рекламодатель", driver.find_element_by_xpath(u"(//a[contains(text(),'Я рекламодатель')])[2]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_iAmAdvButtonText FAILED')
        else: print('test_assert_iAmAdvButtonText PASSED')

    def test_17_assert_iAmWMBannerText1Locator_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert iAmWMBannerText1Locator is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "html/body/div[3]/main/div[1]/div[1]/div[2]/p"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_iAmWMBannerText1Locator_is_present FAILED')
        else: print('test_assert_iAmWMBannerText1Locator_is_present PASSED')

    def test_18_assert_regButton_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()     
        # Assert regButton is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "html/body/div[3]/main/div[1]/a"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_regButton_is_present FAILED')
        else: print('test_assert_regButton_is_present PASSED')

    def test_19_assert_regButtonText(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()              
        # Assert regButtonText is equal "Зарегистрироваться"
        try: self.assertEqual(u"Зарегистрироваться", driver.find_element_by_xpath("html/body/div[3]/main/div[1]/a").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_regButtonText FAILED')
        else: print('test_assert_regButtonText PASSED')

    def test_20_assert_imageLeftLabel1_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()         
        # Assert imageLeftLabel1 is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".item_desc"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_imageLeftLabel1_is_present FAILED')
        else: print('test_assert_imageLeftLabel1_is_present PASSED')

    def test_21_assert_imageLeftLabel1Text(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert imageLeftLabel1Text is equal "Разместите ваше предложение"
        try: self.assertEqual(u"Выберите предложение", driver.find_element_by_css_selector(".item_desc").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_imageLeftLabel1Text FAILED')
        else: print('test_assert_imageLeftLabel1Text PASSED')

    def test_22_assert_imageMiddleLabel1_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert imageMiddleLabel1 is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='section1-a']/div/div[2]/div/span[2]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_imageMiddleLabel1_is_present FAILED')
        else: print('test_assert_imageMiddleLabel1_is_present PASSED')

    def test_23_assert_imageMiddleLabel1Text(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()         
        # Assert imageMiddleLabel1Text is equal "Привлеките покупателей"
        try: self.assertEqual(u"Привлеките покупателей", driver.find_element_by_xpath("//div[@id='section1-a']/div/div[2]/div/span[2]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_imageMiddleLabel1Text FAILED')
        else: print('test_assert_imageMiddleLabel1Text PASSED')

    def test_24_assert_imageRightLabel1_is_present(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert imageRightLabel1 is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='section1-a']/div/div[3]/div/span[2]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_imageRightLabel1_is_present FAILED')
        else: print('test_assert_imageRightLabel1_is_present PASSED')

    def test_25_assert_imageRightLabel1Text(self):        
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()           
        # Assert imageRightLabel1Text is equal "Получайте прибыль"
        try: self.assertEqual(u"Получайте прибыль", driver.find_element_by_xpath("//div[@id='section1-a']/div/div[3]/div/span[2]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_imageRightLabel1Text FAILED')
        else: print('test_assert_imageRightLabel1Text PASSED')

    def test_26_assert_footerLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()  
        # Assert footerLabel is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#section5 > h2"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_footerLabel_is_present FAILED')
        else: print('test_assert_footerLabel_is_present PASSED')

    def test_27_assert_footerLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()       
        # Assert footerLabelText is equal "Начинайте зарабатывать вместе с нашей рекламной сетью"
        try: self.assertEqual(u"Начинайте зарабатывать вместе с нашей рекламной сетью", driver.find_element_by_css_selector("#section5 > h2").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_footerLabelText FAILED')
        else: print('test_assert_footerLabelText PASSED')

    def test_28_assert_regButtonFooter_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()  
        # Assert regButtonFooter is present
        try: self.assertTrue(self.is_element_present(By.XPATH, u"(//a[contains(text(),'Зарегистрироваться')])[4]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_regButtonFooter_is_present FAILED')
        else: print('test_assert_regButtonFooter_is_present PASSED')

    def test_29_assert_regButtonFooterText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert regButtonFooterText is equal "Зарегистрироваться"
        try: self.assertEqual(u"Зарегистрироваться", driver.find_element_by_xpath(u"(//a[contains(text(),'Зарегистрироваться')])[4]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_regButtonFooterText FAILED')
        else: print('test_assert_regButtonFooterText PASSED')

    def test_30_assert_forWMLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert forWMLabel is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.footer__item > p"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_regButtonFooterText FAILED')
        else: print('test_assert_regButtonFooterText PASSED')

    def test_31_assert_forWMLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()         
        # Assert forWMLabelText is equal "Для веб-мастеров"
        try: self.assertEqual(u"Для веб-мастеров", driver.find_element_by_css_selector("div.footer__item > p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_forWMLabelText FAILED')
        else: print('test_assert_forWMLabelText PASSED')

    def test_32_assert_rulesLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert rulesLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Правила"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_rulesLink_is_present FAILED')
        else: print('test_assert_rulesLink_is_present PASSED')

    def test_33_assert_forWMLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert forWMLabelText is equal "Правила"
        try: self.assertEqual(u"Правила", driver.find_element_by_link_text(u"Правила").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_forWMLabelText FAILED')
        else: print('test_assert_forWMLabelText PASSED')

    def test_34_assert_faqLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()     
        # Assert faqLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "FAQ"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_faqLink_is_present FAILED')
        else: print('test_assert_faqLink_is_present PASSED')

    def test_35_assert_forWMLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()      
        # Assert forWMLabelText is equal "FAQ"
        try: self.assertEqual("FAQ", driver.find_element_by_link_text("FAQ").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_forWMLabelText FAILED')
        else: print('test_assert_forWMLabelText PASSED')

    def test_36_assert_forAdvLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()              
        # Assert forAdvLabel is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "//footer/div/div[2]/p"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_forAdvLabel_is_present FAILED')
        else: print('test_assert_forAdvLabel_is_present PASSED')

    def test_37_assert_forAdvLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()            
        # Assert forAdvLabelText is equal "Рекламодателям"
        try: self.assertEqual(u"Рекламодателям", driver.find_element_by_xpath("//footer/div/div[2]/p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_forAdvLabelText FAILED')
        else: print('test_assert_forAdvLabelText PASSED')

    def test_38_assert_addProjectLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert addProjectLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Разместить проект"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_addProjectLink_is_present FAILED')
        else: print('test_assert_addProjectLink_is_present PASSED')

    def test_39_assert_addProjectLinkText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert addProjectLinkText is equal "Разместить проект"
        try: self.assertEqual(u"Разместить проект", driver.find_element_by_link_text(u"Разместить проект").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_addProjectLinkText FAILED')
        else: print('test_assert_addProjectLinkText PASSED')

    def test_40_assert_aboutCompanyLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert aboutCompanyLabel is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "//footer/div/div[3]/p"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_aboutCompanyLabel_is_present FAILED')
        else: print('test_assert_aboutCompanyLabel_is_present PASSED')
        
    def test_41_assert_aboutCompanyLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()         
        # Assert aboutCompanyLabelText is equal "Компания"
        try: self.assertEqual(u"Компания", driver.find_element_by_xpath("//footer/div/div[3]/p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_aboutCompanyLabelText FAILED')
        else: print('test_assert_aboutCompanyLabelText PASSED')

    def test_42_assert_aboutUsLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()  
        # Assert aboutUsLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"О нас"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_aboutUsLink_is_present FAILED')
        else: print('test_assert_aboutUsLink_is_present PASSED')

    def test_43_assert_aboutUsLinkText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()   
        # Assert aboutUsLinkText is equal "О нас"
        try: self.assertEqual(u"О нас", driver.find_element_by_link_text(u"О нас").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_aboutUsLinkText FAILED')
        else: print('test_assert_aboutUsLinkText PASSED')

    def test_44_assert_contactsFooterLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert contactsFooterLink is present
        try: self.assertTrue(self.is_element_present(By.XPATH, u"(//a[contains(text(),'Контакты')])[2]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_contactsFooterLink_is_present FAILED')
        else: print('test_assert_contactsFooterLink_is_present PASSED')

    def test_45_assert_contactsFooterLinkText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert contactsFooterLinkText is equal "Контакты"
        try: self.assertEqual(u"Контакты", driver.find_element_by_xpath(u"(//a[contains(text(),'Контакты')])[2]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_contactsFooterLinkText FAILED')
        else: print('test_assert_contactsFooterLinkText PASSED')

    def test_46_assert_privacyLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()      
        # Assert privacyLink is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Политика конфиденциальности"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_privacyLink_is_present FAILED')
        else: print('test_assert_privacyLink_is_present PASSED')

    def test_47_assert_privacyLinkText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert privacyLinkText is equal "Политика конфиденциальности"
        try: self.assertEqual(u"Политика конфиденциальности", driver.find_element_by_link_text(u"Политика конфиденциальности").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_privacyLinkText FAILED')
        else: print('test_assert_privacyLinkText PASSED')

    def test_48_assert_postAddressLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert postAddressLabel is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.footer__item.footer__item_addr > p"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabel_is_present FAILED')
        else: print('test_assert_postAddressLabel_is_present PASSED')

    def test_49_assert_postAddressLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert postAddressLabelText is equal "Почтовый адрес"
        try: self.assertEqual(u"Почтовый адрес", driver.find_element_by_css_selector("div.footer__item.footer__item_addr > p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabelText FAILED')
        else: print('test_assert_postAddressLabelText PASSED')

    def test_50_assert_postAddressLabel1_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert postAddressLabel1 is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.footer__item__address > p"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabel1_is_present FAILED')
        else: print('test_assert_postAddressLabel1_is_present PASSED')

    def test_51_assert_postAddressLabel1Text(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert postAddressLabel1Text is equal "Cariovision Trade Ltd. Geneva Place"
        try: self.assertEqual("Cariovision Trade Ltd. Geneva Place", driver.find_element_by_css_selector("div.footer__item__address > p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabel1Text FAILED')
        else: print('test_assert_postAddressLabel1Text PASSED')

    def test_52_assert_postAddressLabel2_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window() 
        # Assert postAddressLabel2 is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "//p[2]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabel2_is_present FAILED')
        else: print('test_assert_postAddressLabel2_is_present PASSED')

    def test_53_assert_postAddressLabel2Text(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()        
        # Assert postAddressLabel2Text is equal "Waterfront Drive, P.O. Box 3469, Road"
        try: self.assertEqual("Waterfront Drive, P.O. Box 3469, Road", driver.find_element_by_xpath("//p[2]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabel2Text FAILED')
        else: print('test_assert_postAddressLabel2Text PASSED')

    def test_54_assert_postAddressLabel3_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()     
        # Assert postAddressLabel3 is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "//p[3]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabel3_is_present FAILED')
        else: print('test_assert_postAddressLabel3_is_present PASSED')

    def test_55_assert_postAddressLabel3Text(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()            
        # Assert postAddressLabel3Text is equal "Town, Tortola. BVI"
        try: self.assertEqual("Town, Tortola. BVI", driver.find_element_by_xpath("//p[3]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_postAddressLabel3Text FAILED')
        else: print('test_assert_postAddressLabel3Text PASSED')

    def test_56_assert_megastockLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()      
        # Assert megastockLink is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"www.megastock.ru\"]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_megastockLink_is_present FAILED')
        else: print('test_assert_megastockLink_is_present PASSED')

    def test_56_assert_webmanyAtestatLink_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()     
        # Assert webmanyAtestatLink is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, u"img[alt=\"Здесь находится аттестат нашего WM идентификатора 216729121143\"]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_webmanyAtestatLink_is_present FAILED')
        else: print('test_assert_webmanyAtestatLink_is_present PASSED')

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
  
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class MainPagePopUpUITests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Install\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "http://web.cpa-dev.safesocks.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()
        
    def test_1_assert_popUp_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUp is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.form_popup_top"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUp_is_present FAILED')
        else: print('test_assert_popUp_is_present PASSED')

    def test_2_assert_popUpEnterAccountLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpEnterAccountLabelText
        try: self.assertEqual(u"Войти в аккаунт\n×", driver.find_element_by_css_selector("div.form_popup_top").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpEnterAccountLabelText FAILED')
        else: print('test_assert_popUpEnterAccountLabelText PASSED')
        
    def test_3_assert_popUpXElement_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpXElement is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"×"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpXElement_is_present FAILED')
        else: print('test_assert_popUpXElement_is_present PASSED')

    def test_4_assert_popUpEmailField_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpEmailField is present
        try: self.assertTrue(self.is_element_present(By.NAME, "email"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpEmailField_is_present FAILED')
        else: print('test_assert_popUpEmailField_is_present PASSED')

    def test_5_assert_popUpEmailFieldPlaceholderText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_name("email").clear()
        # Assert popUpEmailFieldPlaceholderText
        try: self.assertEqual("Email", driver.find_element_by_name("email").get_attribute("placeholder"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpEmailFieldPlaceholderText FAILED')
        else: print('test_assert_popUpEmailFieldPlaceholderText PASSED')       

    def test_6_assert_popUpPasswordField_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_name("email").clear()
        # Assert popUpPasswordField is present
        try: self.assertTrue(self.is_element_present(By.NAME, "password"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpPasswordField_is_present FAILED')
        else: print('test_assert_popUpPasswordField_is_present PASSED')        

    def test_7_assert_popUpPasswordFieldPlaceholderText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_name("password").clear()
        # Assert popUpPasswordFieldPlaceholderText
        try: self.assertEqual("Пароль", driver.find_element_by_name("password").get_attribute("placeholder"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpPasswordFieldPlaceholderText FAILED')
        else: print('test_assert_popUpPasswordFieldPlaceholderText PASSED')

    def test_8_assert_popUpRememberMeCheckBox_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpRememberMeCheckBox is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "label.pool-label"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRememberMeCheckBox_is_present FAILED')
        else: print('test_assert_popUpRememberMeCheckBox_is_present PASSED')

    def test_9_assert_popUpRememberMeCheckBoxText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpRememberMeCheckBoxText
        try: self.assertEqual(u"Запомнить меня", driver.find_element_by_css_selector("label.pool-label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRememberMeCheckBoxText FAILED')
        else: print('test_assert_popUpRememberMeCheckBoxText PASSED')

    def test_10_assert_popUpForgotPasswordLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpForgotPasswordLabel is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Забыли пароль?"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpForgotPasswordLabel_is_present FAILED')
        else: print('test_assert_popUpForgotPasswordLabel_is_present PASSED')

    def test_11_assert_popUpForgotPasswordLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpForgotPasswordLabelText
        try: self.assertEqual(u"Забыли пароль?", driver.find_element_by_link_text(u"Забыли пароль?").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpForgotPasswordLabelText FAILED')
        else: print('test_assert_popUpForgotPasswordLabelText PASSED')
        
    def test_12_assert_popUpEnterButton_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpEnterButton is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.submit.enter_btn"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpEnterButton_is_present FAILED')
        else: print('test_assert_popUpEnterButton_is_present PASSED')

    def test_13_assert_popUpEnterButtonText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpEnterButtonText
        try: self.assertEqual("", driver.find_element_by_css_selector("input.submit.enter_btn").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpEnterButton_is_present FAILED')
        else: print('test_assert_popUpEnterButton_is_present PASSED')        

    def test_14_assert_popUpVKIcon_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpVKIcon is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "i.socicon-vkontakte"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpVKIcon_is_present FAILED')
        else: print('test_assert_popUpVKIcon_is_present PASSED')

    def test_15_assert_popUpFBIcon_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpFBIcon is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "i.socicon-facebook"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpFBIcon_is_present FAILED')
        else: print('test_assert_popUpFBIcon_is_present PASSED')

    def test_16_assert_popUpCancelButton_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpCancelButton is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input.cancel_button"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpCancelButton_is_present FAILED')
        else: print('test_assert_popUpCancelButton_is_present PASSED')

    def test_17_assert_popUpCancelButtonText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpCancelButtonText
        try: self.assertEqual("Отмена", driver.find_element_by_css_selector("input.cancel_button").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpCancelButtonText FAILED')
        else: print('test_assert_popUpCancelButtonText PASSED')

    def test_18_assert_popUpNoAccountLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpNoAccountLabel is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.not_account > p"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpNoAccountLabel_is_present FAILED')
        else: print('test_assert_popUpNoAccountLabel_is_present PASSED')

    def test_19_assert_popUpNoAccountLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpNoAccountLabelText
        try: self.assertEqual("Нет аккаунта?", driver.find_element_by_css_selector("div.not_account > p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpNoAccountLabelText FAILED')
        else: print('test_assert_popUpNoAccountLabelText PASSED')

    def test_20_assert_popUpRegButton_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpRegButton is present
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Зарегистрироваться"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRegButton_is_present FAILED')
        else: print('test_assert_popUpRegButton_is_present PASSED')

    def test_21_assert_popUpRegButtonText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        # Assert popUpRegButtonText
        try: self.assertEqual(u"Зарегистрироваться", driver.find_element_by_link_text(u"Зарегистрироваться").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRegButtonText FAILED')
        else: print('test_assert_popUpRegButtonText PASSED')

    def test_22_assert_errorRegLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_css_selector("input.submit.enter_btn").click()
        # Assert errorRegLabel is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p.login-error-text"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_errorRegLabel FAILED')
        else: print('test_assert_errorRegLabel PASSED')

    # def test_23_assert_errorRegLabelText(self):
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     driver.find_element_by_link_text(u"Вход и регистрация").click()
    #     driver.find_element_by_css_selector("input.submit.enter_btn").click()
    #     # Assert errorRegLabelText
    #     self.assertEqual("Неверный email или пароль", driver.find_element_by_css_selector(".login-error-text").text)
    #     print('test_assert_errorRegLabelText FAILED')
    #     else: print('test_assert_errorRegLabelText PASSED')
    #     self.assertEqual(u"Неверный email или пароль", driver.find_element_by_css_selector("p.login-error-text.firepath-matching-node").text)
        
    def test_24_assert_popUpRestorePasswordLabel_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_link_text(u"Забыли пароль?").click()
        # Assert popUpRestorePasswordLabel is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p.recovery-text"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRestorePasswordLabel_is_present FAILED')
        else: print('test_assert_popUpRestorePasswordLabel_is_present PASSED')

    def test_25_assert_popUpRestorePasswordLabelText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_link_text(u"Забыли пароль?").click()
        # Assert popUpRestorePasswordLabelText
        try: self.assertEqual(u"На заданный E-mail адрес, будет выслана ссылка. По которой вы сможете создать новый пароль по вашей учетной записи", driver.find_element_by_css_selector("p.recovery-text").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRestorePasswordLabelText FAILED')
        else: print('test_assert_popUpRestorePasswordLabelText PASSED')

    def test_26_assert_popUpRestorePasswordEmailField_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_link_text(u"Забыли пароль?").click()
        # Assert popUpRestorePasswordEmailField is present
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.form-item > input[name=\"email\"]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRestorePasswordEmailField_is_present FAILED')
        else: print('test_assert_popUpRestorePasswordEmailField_is_present PASSED')

    def test_27_assert_popUpRestorePasswordEmailPlaceholderText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_link_text(u"Забыли пароль?").click()
        # Assert popUpRestorePasswordEmailPlaceholderText
        try: self.assertEqual("Email", driver.find_element_by_css_selector("div.form-item > input[name=\"email\"]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRestorePasswordEmailPlaceholderText FAILED')
        else: print('test_assert_popUpRestorePasswordEmailPlaceholderText PASSED')

    def test_28_assert_popUpRestorePasswordButton_is_present(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_link_text(u"Забыли пароль?").click()
        # Assert popUpRestorePasswordButton is present
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='recover-password-container']/div/form/button"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRestorePasswordButton_is_present FAILED')
        else: print('test_assert_popUpRestorePasswordButton_is_present PASSED')

    def test_29_assert_popUpRestorePasswordButtonText(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Вход и регистрация").click()
        driver.find_element_by_link_text(u"Забыли пароль?").click()
        # Assert popUpRestorePasswordButtonText
        try: self.assertEqual(u"Восстановить", driver.find_element_by_xpath("//div[@id='recover-password-container']/div/form/button").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print('test_assert_popUpRestorePasswordButtonText FAILED')
        else: print('test_assert_popUpRestorePasswordButtonText PASSED')

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
   
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)        

if __name__ == "__main__":
    unittest.main()
