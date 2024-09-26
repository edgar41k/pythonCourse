from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time


# Создаем экземпляр Firefox WebDriver
driver = webdriver.Chrome() 


# Переходим на веб-страницу
# driver.get('https://www.github.com')


# print(driver.get.window_size().get('width'))
# driver.set_window_size(1600, 800)
# print(driver.get.window_position())
# driver.set_window_position(0, 0)
# print(driver.get_window_rect())
# print(driver.set_window_rect(150, 150, 800, 600))
# driver.fullscreen_window()
# time.sleep(5)
# driver.maximize_window()
# time.sleep(5)
# driver.minimize_window()
# time.sleep(5)


driver.get('https://www.google.com')

# driver.save_screenshot('main.png')
# div = driver.find_element(By.CSS_SELECTOR, '#CXQnmb > div > div > div.GZ7xNe')
# div.screenshot('main.png')
# driver.refresh()
# print(driver.current_url)

google = driver.current_window_handle
driver.switch_to.new_window('window')
driver.get('https://www.github.com')
github = driver.current_window_handle
time.sleep(3)
driver.switch_to.window(google)
print(driver.window_handles)

# partial - по частичному совпадению
# email = driver.find_element('partial link text', 'Start a free')
# email.click()
# email.sleep(5)

# email = driver.find_element('id', 'hero_user_email')
# email.send_keys('edgar@example.com')


# email.send_keys(Keys.ENTER)
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div[4]/main/div[1]/text-suggester/div[1]/form/div[2]/div[2]/button'))
#     )
#     element.click()
# finally:
#     driver.sleep(5)
#     driver.quit()


# def waiter(timeout, selector_value):
#     try:
#         element = WebDriverWait(driver, timeout).until(
#             EC.element_to_be_clickable((selector, selector_value))
#         )
#         return element
#     except:
#         return None
    
    # element = waiter(10, by.Path, '/html/body/div[1]/div[4]/div[4]/main/div[1]/text-suggester/div[1]/form/div[2]/div[2]/button')


    #     element.click()
    # finally:
    #     driver.sleep(5)
    #     driver.quit()


# continue_btn = driver.find_element('xpath', '/html/body/div[1]/div[4]/div[4]/main/div[1]/text-suggester/div[1]/form/div[2]/div[2]/button')
# continue_btn.click()


# xpath путь по html коду
# /html/body/div[1]/div[4]/div[4]/main/div[1]/text-suggester/div[1]/form/div[2]/div[2]/button
# //*[@id="email-container"]div[2]/button


# print(driver.name)
# print(driver.title)
# print(driver.page_source.encode())


# Ждем 10 секунд, чтобы увидеть страницу
# time.sleep(10)


# Закрываем браузер после ожидания
# driver.quit()
# Закрываем вкладку в браузере
# driver.close()
