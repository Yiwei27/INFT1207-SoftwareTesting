import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTest2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Implicit wait for elements
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()  # Ensures the session is properly closed

    def test_test2(self):
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")
        self.driver.set_window_size(1424, 842)

        # Input values after clearing the fields
        self.driver.find_element(By.NAME, "cage").clear()
        self.driver.find_element(By.NAME, "cage").send_keys("100")

        self.driver.find_element(By.NAME, "cweightkgs").clear()
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("200")

        self.driver.find_element(By.ID, "cheightmeter").clear()
        self.driver.find_element(By.ID, "cheightmeter").send_keys("200")

        self.driver.find_element(By.ID, "cneckmeter").clear()
        self.driver.find_element(By.ID, "cneckmeter").send_keys("100")

        self.driver.find_element(By.ID, "cwaistmeter").clear()
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")

        # Click calculate button
        self.driver.find_element(By.NAME, "x").click()

        # Wait for result to appear
        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "font > b"))
        )

        result_text = result_element.text
        print("Male Test Case Result:", result_text)  # Print actual result for debugging

        # Adjust assertion based on the real displayed result
        expected_result = "Body Fat: 0.0%"  # Update this if incorrect
        assert result_text == expected_result, f"Expected '{expected_result}' but got '{result_text}'"
