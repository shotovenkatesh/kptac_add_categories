import time
from selenium.webdriver import ActionChains
import read_csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.emenu.ae/en/accounts/login/?next=/en/")
time.sleep(2)

# signing in
email_field = driver.find_element(By.NAME, "login").send_keys("alfarah-auh@emenu.ae")
password_field = driver.find_element(By.NAME, "password").send_keys("welcome2023")
driver.find_element(By.NAME, "submit").click()
time.sleep(3)

#clciking on edit pen link
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/a/i').click()
time.sleep(2)


# products drop down
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[6]/div/ul/li[1]/a/span[2]').click()
time.sleep(3)



index = 0
name_from_csv = read_csv.get_names()
category_from_csv = read_csv.get_c()


last_element = len(name_from_csv)

while index < last_element:
    food = name_from_csv[index]

    food_c = category_from_csv[index]

    driver.find_element(By.XPATH,
                        '/html/body/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/span/input').send_keys(
        food)
    time.sleep(3)

    odd_row = driver.find_element(By.CLASS_NAME, 'odd')
    td_element = odd_row.find_element(By.CLASS_NAME, 'td-actions.text-right')
    button = td_element.find_element(By.CLASS_NAME, 'btn.btn-success')
    button.click()
    time.sleep(2)
    driver.execute_script('scrollBy(0,50)')

    # this is  to locate the category field
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/button/div[1]/div/div').click()
    time.sleep(2)
    # this is to search in the category field
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[2]/input').send_keys(
        food_c)
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[4]/div[1]/div/div/div/div[3]/ul/li[1]/a').click()
    driver.execute_script('scrollBy(0,500)')

    submit = driver.find_element(By.NAME, 'submit').click()
    print(f"{food} has been added")
    index += 1
    time.sleep(2)








