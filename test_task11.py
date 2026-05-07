import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


# Test data
SIGN_IN_URL = "https://www.guvi.in/sign-in/"
EMAIL = "priya.venkatraman91@gmail.com"
PASSWORD = "ABCD1234"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()

@pytest.mark.positive
def test_loginPage_and_verifyURL(driver):
    # Click on the login button
    login_button = driver.find_element(By.XPATH, '//*[@id="login-btn"]')
    login_button.click()
    time.sleep(2)
    # Verify that the URL is correct
    assert "https://www.guvi.in/sign-in/" in driver.current_url
    print("The URL is correct: ", driver.current_url)

@pytest.mark.positive
def test_login_page_elements(driver):
    # Verify that the email and password fields are present
    driver.get(SIGN_IN_URL)
    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")

    assert username_field.is_displayed() and password_field.is_displayed()
    assert username_field.is_enabled() and password_field.is_enabled()
    print("Email and Password fields are present on the login page.")


@pytest.mark.positive
def test_login_with_valid_credentials(driver):
    # Enter username and password
    driver.get(SIGN_IN_URL)
    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)
    # Click the login button    
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(3)

@pytest.mark.negative
def test_login_with_invalid_credentials(driver):
    # Enter invalid username and password
    driver.get(SIGN_IN_URL)
    username_field = driver.find_element(By.ID, "email").send_keys("email.com")
    password_field = driver.find_element(By.ID, "password").send_keys("invalid_password")
    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)
    # Verify that an error message is displayed
    assert driver.find_element(By.XPATH, '//*[@id="emailgroup"]/div').is_displayed()
    print("Error message is displayed for invalid credentials.")

@pytest.mark.negative
def test_login_with_empty_fields(driver):
    # Click the login button without entering username and password
    driver.get(SIGN_IN_URL)
    # driver.find_element(By.ID, "email").send_keys("")
    # driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)
    # Verify that an error message is displayed
    assert driver.find_element(By.XPATH, "//*[@id='passwordGroup']/div").is_displayed()
    print("Error message is displayed for empty fields.")

# Run the tests
# pytest test_task11.py --html=report.html --self-contained-html
# Positive test cases: test_loginPage_and_verifyURL, test_login_page_elements, test_login_with_valid_credentials
# Negative test cases: test_login_with_invalid_credentials, test_login_with_empty_fields