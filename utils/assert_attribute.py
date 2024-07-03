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