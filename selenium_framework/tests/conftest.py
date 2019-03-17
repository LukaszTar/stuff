from base.webdriver_factory import DriverFactory
from utitilies.util import remove_png_from_screenshots_dir
import pytest


@pytest.fixture(scope='class')
def class_level_fixture(request, browser):
    df = DriverFactory(browser)
    driver = df.initialize_driver()
    remove_png_from_screenshots_dir()
    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', help='Type browser name on which test cases will be run')


@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption('--browser')
