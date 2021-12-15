import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Initialising driver to use it globally
driver = None


# below method helps in adding additional command line arguments for different purpose
def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )


# below fixture lets use the setup method call only once at class level
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browserName = request.config.getoption("--browserName")

    if browserName == "chrome":
        chrome_option = Options()
        # chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)

    elif browserName == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.maximize_window()
    driver.get("Any link you want to test")
    request.cls.driver = driver
    yield
    time.sleep(3)
    driver.close()
    driver.quit()


# The below additional code helps in capturing screenshots when a test fails... do not change anything
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ['call', "setup"]:
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# below method is part of the snapshot capturing event
def _capture_screenshot(name):
    global driver
    driver.get_screenshot_as_file(name)
