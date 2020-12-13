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
        self.id = ""
        self.password = ""

    def wait_for(self, locator, second=10):
        return WebDriverWait(self.browser, second).until(
            EC.presence_of_element_located(locator)
        )

    def start(self):
        try:
            #self.browser.get(self.url)
            self.browser.maximize_window()
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

            ul_tag = WebDriverWait(self.browser, 500).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/div/div[1]/div[2]/nav/ul')))
            time.sleep(5)
            print("Wait for 5 seconds... ")
            items = ul_tag.find_elements_by_tag_name("li")            
            

            for item in items:
                if item.text != "Deals":
                    #ActionChains(self.browser).key_down(Keys.COMMAND).click(item).perform()
                    ActionChains(self.browser).key_down(Keys.LEFT_SHIFT).click(item).key_up(Keys.LEFT_SHIFT).perform()  
                                        
                    data = {"category": item.text, "restaurants": []}
                    ###self.browser.switch_to.window(window)
                    main_box = self.wait_for((By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div[2]'))
                    boxes = main_box.find_elements_by_xpath('//*[@id="main-content"]/div/div/div[2]/div/div[2]/div')
                    for box in boxes:
                        name = box.find_element_by_tag_name('p')
                        image = box.find_element_by_xpath('//div/figure/div[1]/picture/source')

                        ActionChains(self.browser).click(box).perform()

                        address = self.wait_for((By.XPATH, '//*[@id="main-content"]/div[3]/div[1]/p'), 100) 
                        addressText= self.browser.execute_script("return arguments[0].firstChild.textContent", address)
                        self.wait_for((By.XPATH, '//*[@id="main-content"]/div/div[3]/ul/li[1]/ul/li[1]/div'), 100)

                        print(addressText)
                        dishes = self.browser.find_elements_by_xpath('//*[@id="main-content"]/div[3]/ul/li/ul/li')                        
                        data.get("restaurants").append({"name":name.text, "image":image.get_attribute("srcset"), "address":addressText, "dishes":[]})
                        i = len(data.get('restaurants'))
                        print(i)
                        for dish in dishes:
                            try:
                                dish_name = dish.find_element_by_class_name('jq jr js aj')
                                dish_price = dish.find_element_by_class_name('cv cp cq bc')
                                dish_description = dish.find_element_by_class_name('ca f1 cq cs')
                                dish_image = dish.find_element_by_xpath('//div/div/div/div[2]/picture/source')
                                data.get('restaurants')[i-1]['dishes'].append({'name': dish_name.text, 'price': dish_price.text[1:], 'description':dish_description.text, 'image': dish_image.get_attribute('srcset')})

                            except exceptions.NoSuchElementException:
                                continue                        
                        self.browser.back()
                        
                    print(data)
                    ActionChains(self.browser).key_down(Keys.LEFT_CONTROL).send_keys('w').key_up(Keys.LEFT_CONTROL).perform()
                


        finally:
            print('end')
           #self.browser.quit()
            

        """    nav_box = self.browser.find_element_by_tag_name('nav')

            items = nav_box.find_elements_by_tag_name('li')

            for item in items:
                print(item.text)
            

            
            
            #related_box = WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "fuqBx")))
        """
        


tester = GetUberEats()
tester.start()

