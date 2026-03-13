# Generated from Selenium IDE
# Test name: t02 - Users can switch roles
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from fn_switchuser import Test_fn_switchuser as Sub1

class Test_02_Users_can_switch_roles:
  def setup_method(self, method):
    self.driver = self.selectedBrowser
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

  def test_02_Users_can_switch_roles(self):
    self.driver.get("http://127.0.0.1/")
    self.driver.find_element(By.LINK_TEXT, "My Projects").click()
    assert len(self.driver.find_elements(By.XPATH, "//*[@id=\"table-proj_table\"][contains(.,'Role Switcher Test')]")) > 0
    self.driver.find_element(By.LINK_TEXT, "Role Switcher Test").click()
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"prefix=role_switcher\"][href*=\"page=configure\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role2\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]").is_selected() is False
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]")).is_selected() else element.click()
    time.sleep(2)
    self.vars["username"] = "user1"
    sub=Sub1();sub.driver=self.driver;sub.vars=self.vars;sub.test_fn_switchuser() # Run fn switchuser
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"prefix=role_switcher\"][href*=\"page=switchrole\"]").click()
    assert len(self.driver.find_elements(By.CSS_SELECTOR, "a[href*=\"route=AlertsController:setup\"]")) > 0
    self.driver.execute_script("$('#south').remove()")
    self.driver.find_element(By.CSS_SELECTOR, "input[value=\"Role2\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "south")))
    assert len(self.driver.find_elements(By.CSS_SELECTOR, "a[href*=\"route=AlertsController:setup\"]")) == 0
    self.driver.execute_script("$('#south').remove()")
    self.driver.find_element(By.CSS_SELECTOR, "input[value=\"Role1\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "south")))
    assert len(self.driver.find_elements(By.CSS_SELECTOR, "a[href*=\"route=AlertsController:setup\"]")) > 0
    self.vars["username"] = "admin"
    sub=Sub1();sub.driver=self.driver;sub.vars=self.vars;sub.test_fn_switchuser() # Run fn switchuser
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"prefix=role_switcher\"][href*=\"page=configure\"]").click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]")).is_selected() else element.click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]")).is_selected() else element.click()
    time.sleep(2)
