import time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# constant
SITE = 'https://www.naver.com'

sizes = [
    320, 480, 960, 1024, 1366, 1920
]


class ResponsiveTest():
    def __init__(self, site, max_page=10, dir="screenshots"):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.site = site
        self.dir = dir
        self.max_page = max_page


    def start(self):
        try:
            self.browser.get(self.site)
            self.browser.maximize_window()
            max_height = self.browser.get_window_size()['height']
            
            for size in sizes:
                self.browser.set_window_size(size, max_height)
                real_width = self.browser.get_window_size()['width']
                scroll_height = self.browser.execute_script("return document.body.scrollHeight")
                total_section = math.ceil(scroll_height/max_height)

                for section in range(total_section):
                    self.browser.execute_script(f"window.scrollTo(0, {(section)*max_height})")
                    self.browser.save_screenshot(f"screenshots/{real_width}x{section+1}.png")
                    time.sleep(0.5)

        finally:
            self.browser.quit()


reponsive = ResponsiveTest(SITE)
reponsive.start()