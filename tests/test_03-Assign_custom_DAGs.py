# Generated from Selenium IDE
# Test name: t03 - Assign custom DAGs
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_03_Assign_custom_DAGs:
  def setup_method(self, method):
    self.driver = self.selectedBrowser
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

  def test_03_Assign_custom_DAGs(self):
    self.driver.get("http://127.0.0.1/")
    self.driver.find_element(By.LINK_TEXT, "My Projects").click()
    assert len(self.driver.find_elements(By.XPATH, "//*[@id=\"table-proj_table\"][contains(.,'Role Switcher Test')]")) > 0
    self.driver.find_element(By.LINK_TEXT, "Role Switcher Test").click()
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"prefix=role_switcher\"][href*=\"page=configure\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role2\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role1\"]").is_selected() is False
    assert self.driver.find_element(By.CSS_SELECTOR, "input[title=\"user1 - Role2\"]").is_selected() is False
    self.driver.find_element(By.CSS_SELECTOR, "a.roleswitcherdags[data-user=\"admin\"]").click()
    assert len(self.driver.find_elements(By.XPATH, "//div[@aria-describedby][contains(.,'You must assign roles to the user')]")) > 0
    self.driver.find_element(By.XPATH, "//div[@aria-describedby][contains(.,'You must assign roles to the user')]//*[contains(@class,'ui-dialog-buttonset')]//button").click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role2\"]")).is_selected() else element.click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "a.roleswitcherdags[data-user=\"admin\"]").click()
    assert len(self.driver.find_elements(By.XPATH, "//div[@aria-describedby][contains(.,'You must assign roles to the user')]")) == 0
    assert len(self.driver.find_elements(By.CSS_SELECTOR, "div[aria-describedby=\"dags-dialog\"]")) > 0
    None if (element := self.driver.find_element(By.XPATH, "//label[contains(.,'Role1 - [No assignment]')]//input")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.XPATH, "//label[contains(.,'Role2 - DAG1')]//input")).is_selected() else element.click()
    self.driver.find_element(By.CSS_SELECTOR, "div[aria-describedby=\"dags-dialog\"] div.ui-dialog-buttonset button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')][contains(.,'Custom')]")))
    assert len(self.driver.find_elements(By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')]//td[contains(.,'Custom')]")) > 0
    self.driver.execute_script("//SETDESC:DAG assignments set")
    self.driver.find_element(By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')]//td[contains(.,'Custom')]").send_keys("SAVESCREENSHOT")
    self.driver.execute_script("//SAVEDESC:Reload page.")
    self.driver.execute_script("window.location.reload()")
    self.driver.execute_script("//SETDESC:Confirm custom DAG assignments saved")
    self.driver.find_element(By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')]//td[contains(.,'Custom')]").send_keys("SAVESCREENSHOT")
    self.driver.find_element(By.CSS_SELECTOR, "a.roleswitcherdags[data-user=\"admin\"]").click()
    assert len(self.driver.find_elements(By.XPATH, "//div[@aria-describedby][contains(.,'You must assign roles to the user')]")) == 0
    assert len(self.driver.find_elements(By.CSS_SELECTOR, "div[aria-describedby=\"dags-dialog\"]")) > 0
    assert self.driver.find_element(By.XPATH, "//label[contains(.,'Role1 - [No assignment]')]//input").is_selected() is True
    assert self.driver.find_element(By.XPATH, "//label[contains(.,'Role2 - DAG1')]//input").is_selected() is True
    None if not (element := self.driver.find_element(By.XPATH, "//label[contains(.,'Role1 - [No assignment]')]//input")).is_selected() else element.click()
    None if not (element := self.driver.find_element(By.XPATH, "//label[contains(.,'Role2 - DAG1')]//input")).is_selected() else element.click()
    self.driver.find_element(By.CSS_SELECTOR, "div[aria-describedby=\"dags-dialog\"] div.ui-dialog-buttonset button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')][contains(.,'Standard')]")))
    assert len(self.driver.find_elements(By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')]//td[contains(.,'Standard')]")) > 0
    self.driver.execute_script("//SETDESC:DAG assignments unset")
    self.driver.find_element(By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')]//td[contains(.,'Standard')]").send_keys("SAVESCREENSHOT")
    self.driver.execute_script("//SAVEDESC:Reload page.")
    self.driver.execute_script("window.location.reload()")
    self.driver.execute_script("//SETDESC:Confirm custom DAG assignments removed")
    self.driver.find_element(By.XPATH, "//table[@class='roleswitchertbl']//tr[contains(.,'admin')]//td[contains(.,'Standard')]").send_keys("SAVESCREENSHOT")
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role1\"]")).is_selected() else element.click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[title=\"admin - Role2\"]")).is_selected() else element.click()
    time.sleep(2)
