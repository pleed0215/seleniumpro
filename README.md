# Selenium

## 1. driver

### webdriver

- Webdriver manager for python 설치.
- pipenv install webdriver_manager

## 2. WebElement

## 3. Error handling

    - try except를 for loop에 사용시 error가 발생해도 loop를 돌리고 싶다면??
        - except에 continue를 써주면 된다.

## 4. enumerate

    - iterating에서 아이템과 index를 같이 얻어 올 수 있다.

## 5. Waiting for elements

    - javascript 실행 되는 시간 때문에 더러 원하는 결과를 얻지 못할 때가 있다.
    ```python
        shitty_element = WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "g-blk")))
    ```
    - By - locator, selenium.webdriver.common.by 에서 import
    - expected_conditions -> selenium.webdriver.support에서 import
    - WebDriverWait -> selenium.webddriver.support.ui 에서 import
    - 코드는 최대 5초까지 기다리면서... classname이 g-blk가 포함되는 element가 js에 의하여 located될 때까지 기다리라는 의미..

## 6. javascript를 이용하여 shitty_element를 없애기

    - 참고로 python에서는 multiline script는 """ """
    - browser.execute_script(script, *args)
        - args는 arguments[0] ... 으로 들어간다.
    - selenium에서 찾은 element를 script함수를 통해 보내면, html element가 된다.
