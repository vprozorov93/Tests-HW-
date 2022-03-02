from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"/Users/vladislavprozorov/Downloads/chromedriver")

driver.get("https://passport.yandex.ru/auth/")
print(driver.title)
element = driver.find_element(by=By.ID, value='passp-field-login')
element.send_keys('revator.ru@yandex.ru', Keys.ARROW_DOWN)
driver.find_element(by=By.ID, value='passp:sign-in').click()
driver.implicitly_wait(2)
element2 = driver.find_element(by=By.ID, value='passp-field-passwd')
element2.send_keys('N22K2W9L93B', Keys.ARROW_DOWN)
driver.find_element(by=By.ID, value='passp:sign-in').click()
# driver.close()
# driver.quit()