from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    # variable creation for each object call
    shop = (By.XPATH, "//a[text()='Shop']")

    # Driver is initialized
    def __init__(self, driver):
        self.driver = driver

    # method creation as many as needed
    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckoutPage(self.driver)
