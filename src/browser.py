from selenium.webdriver import Remote
import pytest

from selenium.webdriver.chrome.options import options



@pytest.fixture()
def go_to_url(page):
    options = Options()
    options.page.load_strategy = 'normal'
    driver = Remote(
        disared_capabilities={
            "browserName": pytestconfig.getini("browser_name"),
            "broserVersion": pytestconfig.getini("browser_version")
        },
        command_executor=pytestconfig.getini("selenium_url")
        options=options
    )
    yield driver
    driver.quit()


