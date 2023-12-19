import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

def fill_registration_form(driver, fake):
    fake_first_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_username = fake.user_name()
    fake_email = fake.email()
    fake_password = fake.password()

    firstname_field = driver.find_element(By.NAME, 'first_name')
    lastname_field = driver.find_element(By.NAME, 'last_name')
    username_field = driver.find_element(By.NAME, 'username')
    email_field = driver.find_element(By.NAME, 'email')
    password1_field = driver.find_element(By.NAME, 'password1')
    password2_field = driver.find_element(By.NAME, 'password2')
    role_dropdown = Select(driver.find_element(By.NAME, 'role'))

    firstname_field.send_keys(fake_first_name)
    lastname_field.send_keys(fake_last_name)
    username_field.send_keys(fake_username)
    email_field.send_keys(fake_email)
    password1_field.send_keys(fake_password) # secure (sake of testing)
    password2_field.send_keys(fake_password)

    role_dropdown.select_by_visible_text('Teacher')

def register_user(driver):
    register_button = driver.find_element(By.CLASS_NAME, 'submit')
    register_button.click()


def main():
    url = 'https://vizdataacademy.com/signup/'
    
    service = Service(ChromeDriverManager().install())
    service.start()

    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)

    fake = Faker()

    fill_registration_form(driver, fake)
    register_user(driver)

    input("Press Enter to close the browser...")

    driver.quit()
    service.stop()

if __name__ == "__main__":
    main()