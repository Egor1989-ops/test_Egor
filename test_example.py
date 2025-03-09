from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://skillbox.ru")


class TestExample:
    def test_example(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert "Skillbox" == driver.title
