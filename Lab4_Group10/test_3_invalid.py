import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTest3invalid():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test3invalid(self):
        # Open the calculator page
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")
        self.driver.set_window_size(1424, 842)

        # Input invalid age value
        self.driver.find_element(By.NAME, "cage").click()
        self.driver.find_element(By.NAME, "cage").clear()  # Clear any existing value
        self.driver.find_element(By.NAME, "cage").send_keys("@@")  # Invalid input

        # Click the calculate button
        self.driver.find_element(By.NAME, "x").click()

        # Wait for the error message to appear
        try:
            # Wait for the error messages to appear (updated CSS selector)
            error_message = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.rightresult font[color='red']"))
            )

            # Extract the error message text
            error_text = error_message.text.strip()

            # Define the expected error message
            expected_error = "Please provide a positive age."

            # Verify if the error message matches the expected one
            assert error_text == expected_error, f"Expected '{expected_error}' but got '{error_text}'"

            print("Female Test Case Result:", error_text)

        except Exception as e:
            print(f"Error during the test: {e}")
            # Optionally capture a screenshot if the error occurs
            self.driver.save_screenshot("error_screenshot.png")
            assert False, f"Test failed due to error: {e}"
