from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://google.com')


search_bar = browser.find_element_by_class_name('gLFyf')
search_bar.send_keys('hello', Keys.RETURN)

search_results = browser.find_elements_by_class_name('g')

for result in search_results:
    print(dir(result))

browser.quit()