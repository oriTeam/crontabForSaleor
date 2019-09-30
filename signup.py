from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://112.137.131.12:9090/en/account/signup/")

# dang ky
generated_email = "test_{}@gmail.com".format(time.time())
email = driver.find_element_by_id("id_email")
email.send_keys(generated_email)

generated_password = "password"
password = driver.find_element_by_id("id_password") 
password.send_keys(generated_password)
password.send_keys(Keys.RETURN)

try:
    wait = WebDriverWait(driver, 10)

    success_alert = wait.until(EC.url_changes("http://112.137.131.12:9090/en/"))

    import csv
    users = open('users.csv', 'a')
    writer = csv.writer(users)
    writer.writerow([generated_email, generated_password])
    users.close()
finally:
    driver.quit()