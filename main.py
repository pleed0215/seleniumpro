from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# constant
KEYWORD = "buy domain"




class GoogleKeywordScreenShooter():
    def __init__(self, keyword, dir="screenshots"):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.dir = dir

    def start(self):
        self.browser.get('https://google.com')
        try:
            search_bar = self.browser.find_element_by_class_name('gLFyf')
            search_bar.send_keys(self.keyword, Keys.RETURN)

            shitty_element = WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "g-blk")))
            self.browser.execute_script("""
                const shitty = arguments[0];
                shitty.parentElement.removeChild(shitty);
            """, shitty_element)
            search_results = self.browser.find_elements_by_class_name('g')

            print(f"Count of Results: {len(search_results)}")
            for i,result in enumerate(search_results):
                if 'kno-kp' not in result.get_attribute('class'):
                    result.screenshot(f"{self.dir}/{self.keyword}-{i}.png")
        finally:
            self.browser.quit() 


"""
def get_titles(keyword):
    try:
        search_bar = browser.find_element_by_class_name('gLFyf')
        search_bar.send_keys(keyword, Keys.RETURN)

        search_results = browser.find_elements_by_class_name('g')
        

        print(f"Count of Results: {len(search_results)}")
        for result, i in enumerate(search_results):
            try:
                title = result.find_element_by_tag_name('h3');
                if title is not None:
                    title.screentshot()
            except exceptions.NoSuchElementException:
                print("An error is occured.")
                continue
    finally:
        browser.quit() 


def get_screentshots(keyword):
    try:
        search_bar = browser.find_element_by_class_name('gLFyf')
        search_bar.send_keys(keyword, Keys.RETURN)

        shitty_element = WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "g-blk")))
        browser.execute_script('''
            const shitty = arguments[0];
            shitty.parentElement.removeChild(shitty);
        , shitty_element)
        search_results = browser.find_elements_by_class_name('g')

        print(f"Count of Results: {len(search_results)}")
        for i,result in enumerate(search_results):
            if 'kno-kp' not in result.get_attribute('class'):
                result.screenshot(f"{keyword}-{i}.png")
    finally:
        browser.quit() 
"""

#get_titles(KEYWORD)
#get_screentshots(KEYWORD)
shotter = GoogleKeywordScreenShooter(KEYWORD)
shotter.start()