import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import csv
"""
name //*[@id="main-content"]/div/div/div[2]/div/div[2]/div[1]/div/a/div/div[1]/p

image srcset //*[@id="main-content"]/div/div/div[2]/div/div[2]/div[1]/div/figure/div[1]/picture/source
    address //*[@id="main-content"]/div[3]/div[1]/p"""


# constant
YOUR_ID="pleed@naver.com"
YOUR_PASSWORD=""

BASE_URL="https://www.ubereats.com/"


class GetUberEats():
    def __init__(self, id=None, password=None):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.id = "pleed0215@gmail.com"
        self.password = "Plmandoo1!"

    def wait_for(self, locator, second=10):
        return WebDriverWait(self.browser, second).until(
            EC.presence_of_element_located(locator)
        )

    def start(self):
        try:
            #self.browser.get(self.url)
            self.browser.get(BASE_URL)

            print("Clicking Sign in button")
            sign_in = self.browser.find_element_by_link_text("Sign in")
            print (sign_in.text)
            sign_in.click()
            
            print("Wating for input box")
            id_input = self.wait_for((By.ID, "useridInput"))
            id_input.send_keys(self.id)
            print("Id inserted")

            next_button = self.browser.find_element_by_xpath('//button')
            next_button.click()
            print("Click next button and wait 3 seconds for password input")
            time.sleep(3)

            print("Wait for password input..")
            password_input = self.wait_for((By.ID, "password"))
            password_input.send_keys(self.password)
            print("Password inserted ...")

            next_button = self.browser.find_element_by_xpath('//button')
            next_button.click()
            print("Now loggin...")

            print("You may input verify code.. please look up your sms code.")

            ul_tag = self.wait_for((By.XPATH, '//*[@id="main-content"]/div/div[1]/div[2]/nav/ul'), 500)
            items = ul_tag.find_elements_by_tag_name("li")

            

            for item in items:
                if item.text != "Deals":
                    ActionChains(self.browser).key_down(Keys.COMMAND).click(item).perform()
                    
            time.sleep(5)
            print("Wait for 5 seconds... ")

            for window in self.browser.window_handles:
                self.browser.switch_to.window(window)
                main_box = self.wait_for((By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div[2]'))
                names = main_box.find_elements_by_xpath('//*[@id="main-content"]/div/div/div[2]/div/div[2]/div/div/a/div/div[1]/p')
                print(len(names))
                for name in names:
                    print(name.text)

        finally:
            print("end")    

        """    nav_box = self.browser.find_element_by_tag_name('nav')

            items = nav_box.find_elements_by_tag_name('li')

            for item in items:
                print(item.text)
            

            
            
            #related_box = WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fuqBx")))
        """
        
           #self.browser.quit()


tester = GetUberEats()
tester.start()

