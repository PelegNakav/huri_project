from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

from undetected_chromedriver import WebElement


class CustomWebElement:
    def __init__(self, web_element):
        self._web_element = web_element

    def click(self, driver):
        try:
            self._web_element.click()
        except ElementClickInterceptedException:
            element = driver.find_element_by_css_selector('#px-captcha')
            action = ActionChains(driver)
            action.click_and_hold(element)
            action.perform()
            time.sleep(10)
            action.release(element)
            action.perform()
            time.sleep(0.2)
            action.release(element)
            self._web_element.click()