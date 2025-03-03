from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://skillbox.ru")
corrent_title = driver.title


def run_script():

    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.get("https:skillbox.ru")
    driver.quit()
