#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import csv

vn_country = [
"An Giang Province" ,
"Ba Ria-Vung Tau Province" ,
"Bac Lieu Province" ,
"Bac Giang Province" ,
"Bac Kan Province" ,
"Bac Ninh Province" ,
"Ben Tre Province" ,
"Binh Duong Province" ,
"Binh Dinh Province" ,
"Binh Phuoc Province" ,
"Binh Thuan Province" ,
"Ca Mau Province" ,
"Cao Bang Province" ,
"Can Tho City" ,
"Da Nang City" ,
"Dak Lak Province" ,
"Dak Nong Province" ,
"Dien Bien Province" ,
"Dong Nai Province" ,
"Dong Thap Province" ,
"Gia Lai Province" ,
"Ha Giang Province" ,
"Ha Nam Province" ,
"Hanoi City" ,
"Ha Tinh Province" ,
"Hai Duong Province" ,
"Haiphong City" ,
"Hau Giang Province" ,
"Hoa Binh Province" ,
"Hung Yen Province" ,
"Khanh Hoa Province" ,
"Kien Giang Province" ,
"Kon Tum Province" ,
"Lai Chau Province" ,
"Lang Song Province" ,
"Lao Cai Province" ,
"Lam Dong Province" ,
"Long An Province" ,
"Nam Dinh Province" ,
"Nghe An Province" ,
"Ninh Binh Province" ,
"Ninh Thuan Province" ,
"Phu Tho Province" ,
"Phu Yen Province" ,
"Quang Binh Province" ,
"Quang Nam Province" ,
"Quang Ngai Province" ,
"Quang Ninh Province" ,
"Quang Tri Province" ,
"Soc Trang Province" ,
"Son La Province" ,
"Tay Ninh Province" ,
"Thai Binh Province" ,
"Thai Nguyen Province" ,
"Thanh Hoa Province" ,
"Ho Chi Minh City" ,
"Thua Thien-Hue Province" ,
"Tien Giang Province" ,
"Tra Vinh Province" ,
"Tuyen Quang Province" ,
"Vinh Long Province" ,
"Vinh Phuc Province" ,
"Yen Bai Province"
]  
def buy():
    # chon tai khoan
    users = open("users.csv", "r")
    reader = csv.reader(users)
    rows = [r for r in reader]
    users.close()
    email, password = rows[random.randrange(0, len(rows))]

    # dang nhap
    driver = webdriver.Firefox()
    driver.get("http://112.137.131.12:9090/en/account/login/")

    email_input = driver.find_element_by_id("id_username")
    email_input.send_keys(email)

    password_input = driver.find_element_by_id("id_password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-list")))
        for i in range(1, random.randrange(2, 5)):
            # mua hang
            categories = [link for link in driver.find_elements_by_class_name("nav-link")]
            categories[random.randrange(0, len(categories))].click()
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-filters")))
            products = [img for img in driver.find_elements_by_class_name("product-list-item-name")]
            products[random.randrange(0, len(products))].click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Add to cart')]"))).click()
        # checkout
        driver.get('http://112.137.131.12:9090/en/checkout/')
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Checkout')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Shipping address')]")))
        address = driver.find_elements_by_tag_name("address")
        if len(address) == 0:
            driver.find_element_by_id("id_street_address_1").send_keys("street address")
            driver.find_element_by_id("id_street_address_2").send_keys("apartment")
            country_area = vn_country[random.randrange(0, len(vn_country))]
            driver.find_element_by_id("id_city").send_keys(country_area)
            driver.find_element_by_id("id_country_area").send_keys(country_area)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Continue')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Continue')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Order & Pay')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Proceed to payment')]"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "id_charge_status_2"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Make payment')]"))).click()
    except Exception as e:
        print(str(e))
    finally:
        driver.quit()