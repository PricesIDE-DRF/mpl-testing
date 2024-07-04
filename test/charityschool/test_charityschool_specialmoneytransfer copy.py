# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support import expected_conditions as EC

from utils.assert_attribute import assert_id_disbursement, assert_status_disbursement
from utils.assert_redirect import assert_url_contains
from utils.auth_actions import is_logged_in, perform_login
from utils.webdriver_setup import get_webdriver

class TestSpecialMoneyTransfer():
  def setup_method(self, method):
    self.driver = get_webdriver()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pecialmoneyTransfer(self):
    self.driver.get("https://charityschool.amanah-staging.cs.ui.ac.id/")
    time.sleep(2)
    self.driver.set_window_size(1552, 832)
    time.sleep(2)
    
    if(not is_logged_in(self.driver)):
        perform_login(self.driver)
        
    time.sleep(2)
    # Click the "Program" button to reveal the dropdown
    program_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Program')]"))
    )
    program_button.click()
    
    # Wait for the dropdown to appear and click the "Aktivitas" link
    aktivitas_link = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/activity']/span[contains(text(), 'Aktivitas')]"))
    )
    aktivitas_link.click()
    
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .rounded-box span").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(2) a:nth-child(1) > .btn").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "disbursementMethod").click()
    time.sleep(1)
    dropdown = self.driver.find_element(By.NAME, "disbursementMethod")
    time.sleep(1)
    dropdown.find_element(By.XPATH, "//option[. = 'Special Money Transfer']").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    
        
    # Form data
    self.driver.find_element(By.NAME, "account_number").click()
    self.driver.find_element(By.NAME, "account_number").click()
    self.driver.find_element(By.NAME, "account_number").send_keys("043705231")
    self.driver.find_element(By.NAME, "bank_code").click()
    self.driver.find_element(By.NAME, "bank_code").send_keys("bca")
    self.driver.find_element(By.NAME, "amount").click()
    self.driver.find_element(By.NAME, "amount").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(4) > .input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(4) > .input").send_keys("tarik selenium")
    time.sleep(2)
    self.driver.find_element(By.NAME, "sender_name").click()
    self.driver.find_element(By.NAME, "sender_name").send_keys("selenium sender")
    self.driver.find_element(By.NAME, "sender_country").click()
    self.driver.find_element(By.NAME, "sender_country").send_keys("100252")
    self.driver.find_element(By.NAME, "sender_job").click()
    self.driver.find_element(By.NAME, "sender_job").send_keys("entrepreneur")
    self.driver.find_element(By.NAME, "direction").click()
    dropdown = self.driver.find_element(By.NAME, "direction")
    dropdown.find_element(By.XPATH, "//option[. = 'DOMESTIC_SPECIAL_TRANSFER']").click()
    
    self.driver.find_element(By.NAME, "vendor_name").click()
    time.sleep(2)
    dropdown = self.driver.find_element(By.NAME, "vendor_name")
    dropdown.find_element(By.XPATH, "//option[. = 'Flip']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    
    
    # Assert page redirect
    expected_url = "https://charityschool.amanah-staging.cs.ui.ac.id/disbursement/list"
    assert_url_contains(self.driver, expected_url)
    
    # Navigate to the last page if pagination exists
    while True:
        try:
            next_button = self.driver.find_element(By.XPATH, "//button[span[@class='sr-only' and text()='Last']]")
            if not next_button.is_enabled():
                break
            next_button.click()
            time.sleep(2)
        except:
            break

    # Click the last item in the table
    time.sleep(2)
    table = self.driver.find_element(By.CSS_SELECTOR, ".table tbody")
    rows = table.find_elements(By.TAG_NAME, "tr")
    if rows:
        last_row = rows[-1]
        detail_button = last_row.find_element(By.CSS_SELECTOR, ".btn")
        detail_button.click()
        time.sleep(2)
        
        assert_id_disbursement(self.driver)
        assert_status_disbursement(self.driver)
    
    
  
