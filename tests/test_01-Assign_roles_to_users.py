# Generated from Selenium IDE
# Test name: t01 - Assign roles to users
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_01_Assign_roles_to_users:
  def setup_method(self, method):
    self.driver = self.selectedBrowser
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

  def test_01_Assign_roles_to_users(self):
    self.driver.get("http://127.0.0.1/")
    self.driver.find_element(By.LINK_TEXT, "My Projects").click()
    assert len(self.driver.find_elements(By.XPATH, "//*[@id=\"table-proj_table\"][contains(.,'Role Switcher Test')]")) > 0
    self.driver.find_element(By.LINK_TEXT, "Role Switcher Test").click()
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"prefix=role_switcher\"][href*=\"page=configure\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role2\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]").is_selected() is False
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]")).is_selected() else element.click()
    time.sleep(2)
    self.driver.execute_script("$('#south').remove()")
    self.driver.execute_script("//SAVEDESC:Reload page.")
    self.driver.execute_script("window.location.reload()")
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "south")))
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]").is_selected() is True
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role2\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]").is_selected() is True
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]")).is_selected() else element.click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]")).is_selected() else element.click()
    time.sleep(2)
    self.driver.execute_script("$('#south').remove()")
    self.driver.execute_script("//SAVEDESC:Reload page.")
    self.driver.execute_script("window.location.reload()")
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "south")))
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role2\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]").is_selected() is False
