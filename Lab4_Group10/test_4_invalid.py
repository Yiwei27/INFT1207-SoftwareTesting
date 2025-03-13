import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTest3invalid:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Ensure the full page is visible
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test3invalid(self):
        # Open the calculator page
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")

        # Wait for elements to be interactable before clearing them
        wait = WebDriverWait(self.driver, 10)

        fields = ["cage", "cweightkgs", "cheightmeter", "cneckmeter", "cwaistmeter", "chipmeter"]

        for field in fields:
            try:
                element = wait.until(
                    EC.element_to_be_clickable((By.NAME, field) if field in ["cage", "cweightkgs"] else (By.ID, field)))
                self.driver.execute_script("arguments[0].scrollIntoView();", element)  # Scroll to the element
                element.clear()
            except Exception as e:
                print(f"Error clearing field '{field}': {e}")

        # Click the calculate button
        calculate_button = wait.until(EC.element_to_be_clickable((By.NAME, "x")))
        calculate_button.click()

        # Wait for the error message to appear
        try:
            error_messages = wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.rightresult font[color='red']"))
            )

            # Extract and print all error messages
            error_texts = [msg.text.strip() for msg in error_messages]
            print("Female Test Case Result:", error_texts)

            expected_errors = [
                "Please provide a positive age.",
                "Please provide a positive weight.",
                "Height need to be positive.",
                "Neck need to be numeric.",
                "Waist need to be numeric."
            ]

            assert error_texts == expected_errors, f"Expected {expected_errors} but got {error_texts}"

        except Exception as e:
            print(f"Error during test execution: {e}")
            self.driver.save_screenshot("error_screenshot.png")  # Save a screenshot for debugging
            assert False, f"Test failed due to error: {e}"
