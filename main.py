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
    def __init__(self, keyword, max_page=10, dir="screenshots"):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.dir = dir
        self.max_page = max_page

    def start(self):
        self.browser.get('https://google.com')
        try:
            search_bar = self.browser.find_element_by_class_name('gLFyf')
            search_bar.send_keys(self.keyword, Keys.RETURN)

            

            for page in range(1, self.max_page+1):
                try:
                    shitty_element = WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "g-blk")))
                    if shitty_element is not None:
                        self.browser.execute_script("""
                            const shitty = arguments[0];
                            shitty.parentElement.removeChild(shitty);
                        """, shitty_element)
                except exceptions.TimeoutException:
                    pass
                
                search_results = self.browser.find_elements_by_class_name('g')

                print(f"Count of Results: {len(search_results)}")
                for i,result in enumerate(search_results):
                    if 'kno-kp' not in result.get_attribute('class'):
                        result.screenshot(f"{self.dir}/{self.keyword}-{page}-{i}.png")

                next_page_elems = self.browser.find_elements_by_class_name('fl')
                next_page = None
                for p in next_page_elems:
                    if p.text != '' and int(p.text) == page+1:
                        next_page = p
                        break
                
                if next_page is not None:
                    next_page.click()
                else:
                    break


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