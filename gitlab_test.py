import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.webdriver.support.select import Select
import math
import csv


class GitLab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver=self.driver
        driver.get("https://gitlab.com/users/sign_in")
        time.sleep(5)
        assert "Sign in · GitLab" in driver.title


    def test_login(self):
        csvfile=open('testcase1.csv','w', newline='')
        testresult=[('MODULE','DESCRIPTION','MESSAGE','STATUS')]
        str_module = 'GITLAB LOGIN'
        str_description = ''
        str_message = ''
        str_status = ''
        driver=self.driver
        time.sleep(3)
        driver.get("https://gitlab.com/users/sign_in")
        driver.maximize_window()
        def validation(str_desc):
            time.sleep(6)
            save_button = driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/input')
            ActionChains(driver).move_to_element(save_button).click().perform()
            driver.implicitly_wait(10)
            time.sleep(2)
            err_msg = driver.find_element_by_xpath('//*[@id="new_user"]/div[1]/p').text
            str_description = str_desc
            str_message = err_msg
            str_status = 'Success'
            time.sleep(2)
            testresult.append((str_module,str_description,str_message,str_status,))

        validation("Username Validation")
        elem = driver.find_elements_by_id('user_login')[0]
        elem.clear()
        elem.send_keys('sandra')
        # validation("password validation")
        driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/input').click()
        time.sleep(3)
        bln_display = driver.find_element_by_xpath('//*[@id="new_user"]/div[2]/p').is_displayed()
        if bln_display:
            str_description='Validation message for password is displayed'
            str_message=driver.find_element_by_xpath('//*[@id="new_user"]/div[2]/p').text
            str_status='Success'
        else:
            str_status='Failed'
            str_message=''
            str_description='There is no validation message'
        testresult.append((str_module,str_description,str_message,str_status,))
        elem = driver.find_elements_by_id('user_password')[0]
        elem.clear()
        elem.send_keys("testpass",Keys.ENTER)
        bln_display=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div').is_displayed()
        driver.current_url
        if bln_display:
            str_description='There are validation for invalid inputs'
            str_message=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div').text
            str_status='Success'
        else:
            str_description='There are no validation'
            str_message=''
            str_status='Failed'
        testresult.append((str_module,str_description,str_message,str_status,))
        # giving valid inputs
        time.sleep(2)
        elem = driver.find_elements_by_id('user_login')[0]
        elem.clear()
        elem.send_keys('sandrasunny281@gmail.com')
        elem = driver.find_elements_by_id('user_password')[0]
        elem.clear()
        elem.send_keys("Sandra@1997",Keys.ENTER)
        # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div').is_displayed
        time.sleep(3)
        if driver.current_url == 'https://gitlab.com/':
            str_description="Successfully entered"
            str_message='Successfully entered'
            str_status='Success'
            testresult.append((str_module,str_description,str_message,str_status,))
        driver.maximize_window()
        obj=csv.writer(csvfile)
        for rst_data in testresult:
            obj.writerow(rst_data)
        csvfile.close()
        driver.close()
    def test_register(self):
        csvfile=open('testcase2.csv','w', newline='')
        testresult=[('MODULE','DESCRIPTION','MESSAGE','Status')]
        str_module = 'GITLAB REGISTRATION'
        str_description = ''
        str_message = ''
        str_status = ''
        driver=self.driver
        time.sleep(3)
        driver.get("https://gitlab.com/users/sign_up")
        driver.maximize_window()
        # print("title of the page is (driver.find_element_by_partiallink_text("Register for GitLab").text)")
        def validation(str_desc):
            time.sleep(6)
            save_button = driver.find_element_by_xpath('//*[@id="new_new_user"]/div[10]/input')
            ActionChains(driver).move_to_element(save_button).click().perform()
            driver.implicitly_wait(10)
            time.sleep(2)
            # import pdb; pdb.set_trace()
            err_msg = driver.find_element_by_xpath('//*[@id="new_new_user"]/div[3]/div[1]/p').text
            str_description = str_desc
            str_message = err_msg
            str_status = 'Succes'
            time.sleep(2)
            testresult.append((str_module,str_description,str_message,str_status,))

        validation("Fields validation")
        time.sleep(3)
        elem=driver.find_elements_by_xpath('//*[@id="new_user_first_name"]')[0]
        elem.click()
        elem.send_keys("sandra")
        driver.find_element_by_id("new_user_last_name").send_keys("sunny")
        driver.find_element_by_id("new_user_username").send_keys("sandrasunny281")
        driver.find_element_by_id("new_user_email").send_keys("sandrasunny281@gmail.com")
        driver.find_element_by_id("new_user_password").send_keys("Sandra@1997")
        driver.find_elements_by_xpath('//*[@id="new_user_email_opted_in"]')[0].click()
        # driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]').click()
        # click on recaptchaa
        obj=csv.writer(csvfile)
        for rst_data in testresult:
            obj.writerow(rst_data)
        csvfile.close()
        driver.close()
    def test_newproject(self):
        csvfile=open('testcase3.csv','w', newline='')
        testresult=[('MODULE','DESCRIPTION','MESSAGE','STATUS')]
        str_module = 'GITLAB NEWPROJECT'
        str_description = ''
        str_message = ''
        str_status = ''
        driver=self.driver
        time.sleep(3)
        driver.get("https://gitlab.com/users/sign_in")
        driver.maximize_window()
        elem = driver.find_elements_by_id('user_login')[0]
        elem.clear()
        elem.send_keys('sandrasunny281@gmail.com')
        elem = driver.find_elements_by_id('user_password')[0]
        elem.clear()
        elem.send_keys('Sandra@1997',Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content-body"]/div[3]/div/a').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//*[@id="content-body"]/div[2]/div[2]/div[2]/a[1]').click()
        time.sleep(3)
        driver.maximize_window()
        if driver.current_url == 'https://gitlab.com/projects/new':
            str_description='Successfully entered newpage'
            str_message="New page url is 'https://gitlab.com/projects/new'"
            str_status='Success'
        else:
            str_description=''
            str_message=''
            str_status="Failed"
        testresult.append((str_module,str_description,str_message,str_status,))
        time.sleep(2)



        # import pdb; pdb.set_trace()
        obj=csv.writer(csvfile)
        for rst_data in testresult:
            obj.writerow(rst_data)
        csvfile.close()


if __name__ == "__main__":
    unittest.main()
