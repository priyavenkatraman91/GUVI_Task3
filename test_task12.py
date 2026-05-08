from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.guvi.in/")
time.sleep(3)
# "taking the 'Live Classes' link as reference point for XPath tasks"
parent_element = driver.find_element(By.XPATH, "//*[@id='header-container']/div[1]/div[3]/div[1]")
print(f"Parent Tag: {parent_element.tag_name}")
# first child and second sibling of the 'Live Classes' link
first_child = driver.find_element(By.XPATH, "//*[@id='header-container']/div[1]/div[3]/div[1]/child::div[1]")
print(f"First Child Text: {first_child.text}")
second_sibling = driver.find_element(By.XPATH, "//*[@id='header-container']/div[1]/div[3]/div[1]/following-sibling::div[2]")
print(f"Second Sibling Text: {second_sibling.text}")

# parent of an element with the attribute "href"
parent_of_href = driver.find_element(By.XPATH, "//*[@href='/manifest.json']/parent::*")
print(f"Parent of 'Manifest' href tag: {parent_of_href.tag_name}")

# ancestors of the 'Signup' button
ancestors = driver.find_elements(By.XPATH, "//*[@id='header-container']/div[1]/div[4]/div/button[2]/ancestor::*")
print(f"Number of ancestors for Signup button: {len(ancestors)}")

# locate all following siblings of the 'LIVE Classes' list item
following_siblings = driver.find_elements(By.XPATH, "//*[@id='header-container']/div[1]/div[3]/div[1]/following-sibling::*")
print("Following Siblings for live classes:")
for sibling in following_siblings:
    print(f" - {sibling.text.strip()}")

# preceding elements of the 'LIVE Classes' link
preceding_elements = driver.find_elements(By.XPATH, "//*[@id='header-container']/div[1]/div[3]/div[1]/preceding::div")
print(f"Found {len(preceding_elements)} preceding div(s) before LIVE Classes.")

driver.quit()
