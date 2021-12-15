from selenium.webdriver.common.by import By


class CheckoutPage:

    # variable creation for each object call
    products = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "//div[@class='card new-card h-100']")

    # Driver is initialized
    def __init__(self, driver):
        self.driver = driver

    # method creation as many as needed
    def getProducts(self):
        # * is important to connect variable with the class name
        return self.driver.find_elements(*CheckoutPage.products)

    # noinspection PyMethodMayBeStatic
    def selectProductName(self, product):
        return product.find_element(*CheckoutPage.productName)
