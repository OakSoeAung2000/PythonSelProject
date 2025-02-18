import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestOne:



    def test_e2e(self, setup):


        setup.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            pname = product.find_element(By.XPATH, "div/h4/a").text
            if pname == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        driver.find_element(By.CLASS_NAME, "btn-success").click()

        driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element(By.LINK_TEXT, "India").click()
        driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success" in successText
        driver.close()