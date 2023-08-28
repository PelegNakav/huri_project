import selenium.webdriver.chrome.options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains
from websockets import headers

from driver_version import *
import undetected_chromedriver as uc
from selenium.webdriver.remote.webdriver import By
#from click import *
import time

def get_departments(driver):
    try:
        departments_button = driver.find_element(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/main/div/div[3]/div/div/div[1]/div[1]/section/div/section[1]/div[1]/h3/button/div")
    except NoSuchElementException:
        element = driver.find_element(By.CSS_SELECTOR, "#px-captcha")
        action = ActionChains(driver)
        action.click_and_hold(element)
        action.perform()
        time.sleep(10)
        action.release(element)
        action.perform()
        time.sleep(0.2)
        action.release(element)
        time.sleep(10)
        departments_button = driver.find_element(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/main/div/div[3]/div/div/div[1]/div[1]/section/div/section[1]/div[1]/h3/button/div")
    departments_button.click()
    try:
        show_more = driver.find_element(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/main/div/div[3]/div/div/div[1]/div[1]/section/div/section[1]/div[2]/div/button")
    except NoSuchElementException:
        show_more = 0
    if show_more:
        try:
            show_more.click()
        except ElementClickInterceptedException:
            element = driver.find_element_by_css_selector('#px-captcha')
            action = ActionChains(driver)
            time.sleep(5)
            action.click_and_hold(element)
            action.perform()
            time.sleep(10)
            action.release(element)
            action.perform()
            time.sleep(0.2)
            action.release(element)
            show_more.click()
    departments = driver.find_elements(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/main/div/div/div/div/div[3]/div[1]/section/div/section[1]/div[2]/div/div[2]/div[*]/label/input")
    if len(departments) == 0:
        driver.back()
        return 0
    for department_index in range(len(departments)):
        print(departments[department_index])
        departments[department_index].click()
        get_departments(driver)
        departments_button = driver.find_element(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/main/div/div/div/div/div[3]/div[1]/section/div/section[1]/div/h3/button/div")
        departments_button.click()
        try:
            show_more = driver.find_element(By.XPATH,
                                            r"/html/body/div/div[1]/div/div/div[2]/div/main/div/div/div/div/div[3]/div[1]/section/div/section[1]/div[2]/div/button")
        except NoSuchElementException:
            show_more = 0
        if show_more:
            show_more.click()
        departments = driver.find_elements(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/main/div/div/div/div/div[3]/div[1]/section/div/section[1]/div[2]/div/div[2]/div[*]/label/input")
        print(len(departments))
    driver.back()


def get_categories(driver):
    categories_link = driver.find_elements(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[*]/ul/li[*]/ul/li[*]/a")
    for category_link_index in range(len(categories_link)):
        buttons = driver.find_elements(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[*]/ul/li[*]/button")
        for button in buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                print("error error ad matay")
                pass
        actions = ActionChains(driver)
        # Move the cursor to the element
        actions.move_to_element(categories_link[category_link_index]).perform()
        categories_link[category_link_index].click()
        get_departments(driver)
        categories_link = driver.find_elements(By.XPATH, r"/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[*]/ul/li[*]/ul/li[*]/a")
    driver.back()
def browse_departments():
    driver = uc.Chrome(driver_executable_path=get_chromedriver_fp())
    driver.implicitly_wait(2)
    driver.get(
        'https://www.walmart.com/all-departments')
    element = driver.find_element(By.CSS_SELECTOR, "#px-captcha")
    action = ActionChains(driver)
    action.click_and_hold(element)
    action.perform()
    time.sleep(10)
    action.release(element)
    action.perform()
    time.sleep(0.2)
    action.release(element)
    time.sleep(10)
    shop_all_links = driver.find_elements(By.LINK_TEXT, "Shop All")
    for link_index in range(len(shop_all_links)):
        shop_all_links[link_index].click()
        get_categories(driver)
        shop_all_links = driver.find_elements(By.LINK_TEXT, "Shop All")
        driver.back()
    driver.quit()



'''
departments = get_all_departments()

for department in departments:
    brands = get_all_brands()

    for brand in brands:
        pages = get_pages()

        for page in pages:
            products = get_products()
            products_data_chunk = []

            for i, product in enumerate(products):
                data = get_product_data()
                products_data_chunk.append(data)

                if i % 20 == 0:
                    print(products_data_chunk)
                    products_data_chunk = []

            if len(products_data_chunk) > 0:
                print(products_data_chunk)  # Press Ctrl+F8 to toggle the breakpoint.

'''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    browse_departments()


