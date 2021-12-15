import inspect
import pytest
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# below fixture is called from conftest.py from tests package
@pytest.mark.usefixtures("setup")
class BaseClass:

    # noinspection PyMethodMayBeStatic
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("../utilities/logFile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    # below method is a explicit wait code which can be used at multiple places inside tests
    def explicit_wait_link(self, value):
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, value)))


