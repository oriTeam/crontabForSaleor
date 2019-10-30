#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

def fulfill():
    # dang nhap
    driver = webdriver.Firefox()
    driver.get("http://34.67.41.100:8000/en/account/login/")

    email_input = driver.find_element_by_id("id_username")
    email_input.send_keys('admin@example.com')

    password_input = driver.find_element_by_id("id_password")
    password_input.send_keys('admin')
    password_input.send_keys(Keys.RETURN)

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-list")))
        driver.get('http://34.67.41.100:8000/dashboard/orders/?id=&name_or_email=&created_after=&created_before=&status=unfulfilled&payment_status=fully-charged&total_net_min=&total_net_max=&sort_by=')
        orders = driver.find_elements_by_xpath("//*[contains(text(), 'Unfulfilled')]")
        while len(orders) > 0:
            driver.find_element_by_xpath("//*[contains(text(), 'Unfulfilled')]").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Fulfill')]"))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Fulfill')]"))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Invoice')]")))
            driver.get('http://34.67.41.100:8000/dashboard/orders/?id=&name_or_email=&created_after=&created_before=&status=unfulfilled&payment_status=fully-charged&total_net_min=&total_net_max=&sort_by=')
            orders = driver.find_elements_by_xpath("//*[contains(text(), 'Unfulfilled')]")
    except Exception as e:
        print(e)
    finally:
        driver.quit()