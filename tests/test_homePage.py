import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.selectCheckbox().click()
        self.selectOptionsByText(homePage.chooseGender(), getData["gender"])
        log.info(getData["name"] + getData["gender"] + getData["email"] + getData["password"] )
        homePage.clickSubmit().click()
        confirm = homePage.getMessage().text
        log.info("Full Message from Homepage is: " + confirm)

        assert "successfully" in confirm
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_data("testcase2"))
    def getData(self, request):
        return request.param
