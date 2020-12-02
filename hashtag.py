import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# constant
HASH_TAG = 'dog'
BASE_URL = "https://www.instagram.com/directory/hashtags/"


class ResponsiveTest():
    def __init__(self, tag, dir="screenshots"):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.tag = tag
        self.url = f"{BASE_URL}{tag}"
        self.dir = dir


    def start(self):
        try:
            #self.browser.get(self.url)
            self.browser.get(BASE_URL)

            input = self.browser.find_element_by_class_name("XTCLo")
            input.send_keys(self.tag)
            
            related_box = WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "drKGC")))
            

            if related_box is not None:
                tags = related_box.find_elements_by_xpath("//div/a[@class='yCE8d']")
                print(tags)
                for tag in tags:
                    if tag.tag_name == "a":
                        ActionChains(self.browser).key_down(Keys.COMMAND).click(tag).perform()
        finally:
           self.browser.quit()


tester = ResponsiveTest(HASH_TAG)
tester.start()

