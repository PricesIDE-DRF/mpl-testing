from selenium import webdriver
import os

def get_webdriver():
    driver_path = os.path.join(os.path.dirname(__file__), '../drivers/chromedriver')
    if os.name == 'nt':  # For Windows
        driver_path += '.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    return driver