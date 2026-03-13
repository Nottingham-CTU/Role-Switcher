# Generated from Selenium IDE
# Test name: t04 - Custom DAGs enacted
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from fn_switchuser import Test_fn_switchuser as Sub1

class Test_04_Custom_DAGs_enacted:
  def setup_method(self, method):
    self.driver = self.selectedBrowser
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

  def test_04_Custom_DAGs_enacted(self):
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
    self.driver.find_element(By.CSS_SELECTOR, "a.roleswitcherdags[data-user=\"user1\"]").click()
    assert len(self.driver.find_elements(By.XPATH, "//div[@aria-describedby][contains(.,'You must assign roles to the user')]")) == 0
    assert len(self.driver.find_elements(By.CSS_SELECTOR, "div[aria-describedby=\"dags-dialog\"]")) > 0
    None if (element := self.driver.find_element(By.XPATH, "//label[contains(.,'Role1 - [No assignment]')]//input")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.XPATH, "//label[contains(.,'Role2 - DAG1')]//input")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.XPATH, "//label[contains(.,'Role2 - DAG2')]//input")).is_selected() else element.click()
    self.driver.find_element(By.CSS_SELECTOR, "div[aria-describedby=\"dags-dialog\"] div.ui-dialog-buttonset button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'user1')][contains(.,'Custom')]")))
    self.vars["username"] = "user1"
    sub=Sub1();sub.driver=self.driver;sub.vars=self.vars;sub.test_fn_switchuser() # Run fn switchuser
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"prefix=role_switcher\"][href*=\"page=switchrole\"]").click()
    assert len(self.driver.find_elements(By.ID, "dag-switcher-change-button")) == 0
    self.driver.execute_script("$('#south').remove()")
    self.driver.find_element(By.CSS_SELECTOR, "input[value=\"Role2\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "south")))
    assert len(self.driver.find_elements(By.ID, "dag-switcher-change-button")) > 0
    self.driver.execute_script("$('#south').remove()")
    self.driver.find_element(By.CSS_SELECTOR, "input[value=\"Role1\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "south")))
    assert len(self.driver.find_elements(By.ID, "dag-switcher-change-button")) == 0
    self.vars["username"] = "admin"
    sub=Sub1();sub.driver=self.driver;sub.vars=self.vars;sub.test_fn_switchuser() # Run fn switchuser
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"prefix=role_switcher\"][href*=\"page=configure\"]").click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]")).is_selected() else element.click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]")).is_selected() else element.click()
    time.sleep(2)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'user1')][contains(.,'Standard')]")))
