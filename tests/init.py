# Generated from Selenium IDE
# Test name: init
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_init:
  def setup_method(self, method):
    self.driver = self.selectedBrowser
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

  def test_init(self):
    self.driver.get("http://127.0.0.1/")
    self.driver.find_element(By.LINK_TEXT, "My Projects").click()
    assert len(self.driver.find_elements(By.XPATH, "//*[@id=\"table-proj_table\"][contains(.,'Role Switcher Test')]")) == 0
    self.driver.find_element(By.LINK_TEXT, "New Project").click()
    self.driver.find_element(By.ID, "app_title").send_keys("Role Switcher Test")
    self.driver.find_element(By.ID, "purpose").find_element(By.CSS_SELECTOR, "*[value='0']").click()
    self.driver.find_element(By.ID, "project_template_radio1").click()
    self.driver.find_element(By.XPATH, "//table[@id='table-template_projects_list']//tr[contains(.,'Classic Database')]//input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primaryrc").click()
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"UserRights/index.php\"]").click()
    self.driver.find_element(By.ID, "new_rolename").send_keys("Role1")
    self.driver.find_element(By.ID, "createRoleBtn").click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"design\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"user_rights\"][value=\"1\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"data_access_groups\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"alerts\"]")).is_selected() else element.click()
    self.driver.find_element(By.CSS_SELECTOR, "[aria-describedby=\"editUserPopup\"] button[style*=\"bold\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='table-user_rights_roles_table']//tr[contains(.,'Role1')]")))
    self.driver.find_element(By.XPATH, "//table[@id='table-user_rights_roles_table']//a[contains(.,'admin')]").click()
    self.driver.find_element(By.ID, "assignUserBtn2").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "user_role").find_element(By.XPATH, "//option[. = 'Role1']").click()
    self.driver.find_element(By.ID, "assignDagRoleBtn").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='table-user_rights_roles_table']//tr[contains(.,'Role1')][contains(.,'admin')]")))
    self.driver.find_element(By.ID, "new_rolename").send_keys("Role2")
    self.driver.find_element(By.ID, "createRoleBtn").click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"design\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"user_rights\"][value=\"1\"]")).is_selected() else element.click()
    None if (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"data_access_groups\"]")).is_selected() else element.click()
    None if not (element := self.driver.find_element(By.CSS_SELECTOR, "input[name=\"alerts\"]")).is_selected() else element.click()
    self.driver.find_element(By.CSS_SELECTOR, "[aria-describedby=\"editUserPopup\"] button[style*=\"bold\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='table-user_rights_roles_table']//tr[contains(.,'Role2')]")))
    self.driver.find_element(By.ID, "new_username_assign").send_keys("user1")
    self.driver.find_element(By.ID, "assignUserBtn").click()
    time.sleep(2)
    None if not (element := self.driver.find_element(By.ID, "notify_email_role")).is_selected() else element.click()
    self.driver.find_element(By.ID, "user_role").find_element(By.XPATH, "//option[. = 'Role1']").click()
    self.driver.find_element(By.ID, "assignDagRoleBtn").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='table-user_rights_roles_table']//tr[contains(.,'Role1')][contains(.,'user1')]")))
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"route=DataAccessGroupsController:index\"]").click()
    self.driver.find_element(By.ID, "new_group").send_keys("DAG1")
    self.driver.find_element(By.ID, "new_group_button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='table-dags_table']//tr[contains(.,'DAG1')]")))
    self.driver.find_element(By.ID, "new_group").send_keys("DAG2")
    self.driver.find_element(By.ID, "new_group_button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='table-dags_table']//tr[contains(.,'DAG2')]")))
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"ExternalModules/manager/project.php\"]").click()
    self.driver.find_element(By.ID, "external-modules-enable-modules-button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "tr[data-module=\"role_switcher\"] button.enable-button")))
    self.driver.find_element(By.CSS_SELECTOR, "tr[data-module=\"role_switcher\"] button.enable-button").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "tr[data-module=\"role_switcher\"] button.external-modules-disable-button")))
