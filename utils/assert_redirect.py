from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assert_url_contains(driver, expected_url):
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url))
    assert expected_url in driver.current_url, f"URL mismatch: expected to contain {expected_url}, got {driver.current_url}"
    print(f"Succesfuly redirect to {expected_url}")
    