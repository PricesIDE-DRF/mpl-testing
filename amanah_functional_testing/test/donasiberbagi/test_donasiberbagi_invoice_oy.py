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

from utils.assert_attribute import assert_id_exists, assert_unique_attribute_exists
from utils.assert_redirect import assert_url_contains
from utils.webdriver_setup import get_webdriver

class TestInvoiceOy():
  def setup_method(self, method):
    self.driver = get_webdriver()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_invoice_oy(self):
    self.driver.get("https://donasiberbagi.amanah-staging.cs.ui.ac.id/")
    time.sleep(2)
    self.driver.set_window_size(1552, 832)
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Donasi").click()
    time.sleep(2)
    element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".aspect-\\[4\\/3\\]"))
    )
    element.click()
    self.driver.find_element(By.CSS_SELECTOR, "a > .btn-outline").click()
    
    time.sleep(2)
    self.driver.find_element(By.NAME, "paymentMethod").click()
    time.sleep(2)
    dropdown = self.driver.find_element(By.NAME, "paymentMethod")
    dropdown.find_element(By.XPATH, "//option[. = 'Invoice']").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".card-actions > .btn").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, ".card-actions > .btn")
    time.sleep(1)

    # FOrm data
    self.driver.find_element(By.NAME, "name").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "name").send_keys("selenium user")
    time.sleep(1)
    self.driver.find_element(By.NAME, "email").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "email").send_keys("try@gmail.com")
    time.sleep(1)
    self.driver.find_element(By.NAME, "phone").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "phone").send_keys("089517313109")
    time.sleep(1)
    self.driver.find_element(By.NAME, "amount").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "amount").send_keys("100000")
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(5) > .input").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".form-control:nth-child(5) > .input").send_keys("donasi selenium")
    time.sleep(1)    
    self.driver.find_element(By.NAME, "quantity").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "quantity").send_keys("2")
    time.sleep(1)
    self.driver.find_element(By.NAME, "price_per_item").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, "price_per_item").send_keys("50000")
    time.sleep(1)
    self.driver.find_element(By.NAME, "vendor_name").click()
    time.sleep(1)
    dropdown = self.driver.find_element(By.NAME, "vendor_name")
    dropdown.find_element(By.XPATH, "//option[. = 'Oy']").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".card-actions > .btn").click()
    time.sleep(1)
    
    # Assert page redirect
    expected_url = "https://donasiberbagi.amanah-staging.cs.ui.ac.id/viapaymentgateway/list"
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
        
        assert_unique_attribute_exists(self.driver, "Invoice")
        assert_id_exists(self.driver)