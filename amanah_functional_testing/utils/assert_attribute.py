from selenium.webdriver.common.by import By

def assert_unique_attribute_exists(driver, method):
    elements_unique = driver.find_elements(By.CSS_SELECTOR, ".mb-2:nth-child(13) > div")
    assert len(elements_unique) > 0, f"Assertion failed: Unique attribute does not exist in {method}"
    
    elements_unique_content = elements_unique[0].text.strip()
    assert elements_unique_content, f"Assertion failed: Unique attribute does not exist in {method}"

    print(f"Assertion passed: {method} Unique attribute exists")

def assert_id_exists(driver):
    elements_id = driver.find_elements(By.CSS_SELECTOR, ".mb-2:nth-child(12) > div")
    assert len(elements_id) > 0, f"Assertion failed: ID does not exist"
    print(f"Assertion passed: ID exists, oject created successfully")
    
    
def assert_id_disbursement(driver):
    elements_id = driver.find_elements(By.CSS_SELECTOR, ".mb-2:nth-child(1) > div")
    assert len(elements_id) > 0, f"Assertion failed: ID does not exist"
    
    id_content = elements_id[0].text.strip()
    assert id_content, f"Assertion failed: ID does not exist"
    print(f"Assertion passed: ID exists, oject created successfully")

def assert_status_disbursement(driver):
    status_element = driver.find_elements(By.CSS_SELECTOR, ".mb-2:nth-child(8) > div")
    assert len(status_element) > 0, f"Tidak terdapat Status"
    
    status_content = status_element[0].text.strip()
    assert status_content == "PENDING", f"Expected status to be 'PENDING' but got '{status_value}'"


    print("Status is correctly set to 'PENDING'")