# Generated from Selenium IDE
# Test name: fn switchuser
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_fn_switchuser:
  def setup_method(self, method):
    self.driver = self.selectedBrowser
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

  def test_fn_switchuser(self):
    self.vars["_projtitle"] = self.driver.execute_script("$('#subheaderDiv2 span').remove();return $('#subheaderDiv2').text()")
    self.vars["_myprojects"] = self.driver.execute_script("return $('a[href*=\"index.php?action=myprojects\"]').attr('href')")
    self.vars["_oldusername"] = self.driver.execute_script("return $('#username-reference').text()")
    self.driver.execute_script("//SETDESC:Log out as arguments[0]", self.vars["_oldusername"])
    self.driver.find_element(By.CSS_SELECTOR, "a[href*=\"logout=1\"]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "username")))
    self.driver.execute_script("window.location = arguments[0]", self.vars["_myprojects"])
    assert len(self.driver.find_elements(By.ID, "username")) > 0
    assert len(self.driver.find_elements(By.ID, "password")) > 0
    time.sleep(1)
    self.driver.execute_script("$('#username').val(arguments[0]);$('#password').val('abc123')", self.vars["username"])
    time.sleep(1)
    self.driver.execute_script("//SETDESC:Log in as arguments[0]", self.vars["username"])
    self.driver.find_element(By.ID, "login_btn").click()
    self.driver.find_element(By.LINK_TEXT, self.vars["_projtitle"]).click()
