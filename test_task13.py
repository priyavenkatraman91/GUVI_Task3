import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    # Initialize Driver
    driver = webdriver.Chrome() 
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    time.sleep(3)
    yield driver
    driver.quit()

@pytest.mark.positive
def test_drag_and_drop(driver):
    # Switch to the iframe containing the draggable and droppable elements
    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='content']/iframe"))
    # finding droppable and draggable elements
    draggable = driver.find_element(By.XPATH, "//*[@id='draggable']")
    droppable = driver.find_element(By.XPATH, "//*[@id='droppable']")
    # performing drag and drop action
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()
    # actions.click_and_hold(draggable).pause(1).move_to_element(droppable).pause(1).release().perform()
    time.sleep(3)
    assert droppable.text == "Dropped!"
    print("Drag and drop action performed successfully, test passed.")

@pytest.mark.negative
def test_drag_and_drop_invalid(driver):
    # finding draggable and droppable elements
    driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='content']/iframe"))
    # finding droppable and draggable elements
    draggable = driver.find_element(By.XPATH, "//*[@id='draggable']")
    droppable = driver.find_element(By.XPATH, "//*[@id='droppable']")
    # performing drag and drop action to an invalid target 
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, driver.find_element(By.TAG_NAME, "body")).perform()
    time.sleep(3)
    assert droppable.text != "Dropped!"
    print("Drag and drop action to an invalid target did not succeed, test passed.")
   
