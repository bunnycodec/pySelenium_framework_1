from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# Main test method which will be needed to execute
class TestOne(BaseClass):

    def test_e2e(self):

        # the below logger is called from the baseclass
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItem()

        products = checkOutPage.getProducts()
        for product in products:
            productName = checkOutPage.selectProductName(product).text
            log.info(productName)
            if productName == "Blackberry":
                checkOutPage.selectProduct(product).click()

        checkOutPage.clickCheckOut1().click()
        confirmPage = checkOutPage.clickCheckOut2()

        confirmPage.getCountryName().send_keys("india")
        # below code is an extension from baseline code
        self.explicit_wait_link("//a[text()='India']")
        confirmPage.selectCountryName().click()
        confirmPage.selectCheckbox().click()
        confirmPage.clickSubmit().click()
        msg = confirmPage.getMessage().text
        log.info("Message from the page end is " + msg)

        assert msg == "Success!"
