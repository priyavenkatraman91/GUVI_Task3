from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

# Test Data
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_TITLE = "Swag Labs"
HOMEPAGE_URL = "https://www.saucedemo.com/"
DASHBOARD_URL = "https://www.saucedemo.com/inventory.html"

@pytest.fixture
def driver():
    # Choose your browser driver (e.g., Chrome, Firefox)
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

@pytest.mark.details
def test_fetch_webpage_details(driver):
  
     # 1.) Title of the webpage
    title = driver.title
    print("Webpage Title: ", title)
    
    # 2.) Current URL of the webpage
    current_url = driver.current_url
    print(f"Current URL: {current_url}")

    # 3.) Extract the entire contents of the webpage and save it in a Text file
    page_content = driver.page_source
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_content)
    print("Webpage content saved to Webpage_task_11.txt")

# --- Positive Test Cases ---
@pytest.mark.positive
def test_valid_login(driver):
    # Verifies successful login with valid credentials.
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # 1) Title of web application
    assert driver.title == EXPECTED_TITLE

    # 3) URL of the Dashboard after Login with credentials given above
    assert driver.current_url == DASHBOARD_URL

def test_homepage_url(driver):

    driver.get(URL)
    # 2) URL of the Homepage
    assert driver.current_url == HOMEPAGE_URL

# --- Negative Test Cases ---
@pytest.mark.negative
def test_invalid_username_login(driver):
    """Verifies error message with invalid username."""
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match any user in this service" in error_message

@pytest.mark.negative
def test_invalid_password_login(driver):
    # Verifies error message with invalid password.
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
    assert "Username and password do not match any user in this service" in error_message

@pytest.mark.negative
def test_locked_out_user_login(driver):
    # Verifies error message for a locked out user.
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Sorry, this user has been locked out" in error_message

@pytest.mark.negative
def test_empty_fields(driver):
    # Verifies error message for empty fields.
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
    assert "Username is required" in error_message