import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.driver.set_window_size(1436, 855)
        element = self.driver.find_element(By.XPATH, "//a[@id=\'ui-id-4\']/span[2]")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.XPATH, "//a[@id=\'ui-id-9\']/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.XPATH, "//a[@id=\'ui-id-9\']/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.XPATH, "//a[@id=\'ui-id-12\']/span").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'narrow-by-list\']/div/div").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'narrow-by-list\']/div/div").click()
        self.driver.find_element(By.CSS_SELECTOR, ".allow > .filter-options-title").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'narrow-by-list\']/div/div[2]/ol/li[3]/a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-options-item:nth-child(1) > .filter-options-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(3) > .text").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'narrow-by-list\']/div[2]/div").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swatch-option-link-layered:nth-child(4) > .swatch-option").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'narrow-by-list\']/div[4]/div").click()
        self.driver.find_element(By.CSS_SELECTOR, ".active .item:nth-child(4) > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".product > .product-image-container .product-image-photo").click()
        self.driver.find_element(By.ID, "option-label-size-143-item-168").click()
        self.driver.find_element(By.ID, "option-label-color-93-item-57").click()
        self.driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button > span").click()
        self.driver.find_element(By.XPATH, "//span[2]").click()

        # Wait for 5 seconds before clicking the cart button again
        time.sleep(5)

        # Click the cart button again after 5 seconds
        self.driver.find_element(By.XPATH, "//span[2]").click()

        # Wait and click on the checkout button
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id='top-cart-btn-checkout']"))
        ).click()

        # Wait 5 seconds before clicking the last two elements
        time.sleep(5)

        # Click these elements at the very end
        self.driver.find_element(By.XPATH, "//div[@id=\'opc-sidebar\']/div/div/div").click()

        product_name = self.driver.execute_script(
            "return window.checkoutConfig.quoteItemData[0].name;"
        )

        # Assert the product name
        assert product_name == "Autumn Pullie", f"Expected 'Autumn Pullie', but got '{product_name}'"
        self.driver.close()
