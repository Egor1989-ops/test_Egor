from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Test1:
    def test_1(self, browser):
        page = browser
        page.goto('https://github.com/microsoft/vscode/issues')
        page.get_by_role('//button[@id="query-builder-twet-clear-button"]') / click()
        page.get_by_role('span[class="flex-1"]').send_keys('in:title bug')
        pass


class Test2:
    def test_2(self, browser):
        page = browser
        page.goto('https://github.com/microsoft/vscode/issues')
        page.get_by_role('//div[@data-sestid="action-bar-autors"]/descendant::button"]') / click()
        page.get_by_role('//span/input[@type="text"]').send_keys("bpasero")
        page.get_by_role('//div[@aria-lable="User results"]').click()
        pass


class Test3:
    def test_3(self, browser):
        page = browser
        page.goto('https://github.com/microsoft/vscode/issues')
        page.get_by_role('//select[@id="search_language"]').send_keys("Python")
        page.get_by_role('//*[@id="search_stars"]').send_keys("2000")
        page.get_by_role('//*[@id="search_filename"]').send_keys("environment.yml")
        pass


class Test4:
    def test_4(self, browser):
        page = browser
        page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')
        driver.set_window_size(1400, 770)
        action_chains = webdriver.ActionChains(driver)
        time.sleep(3)
        action_chains.move_to_element("//*[@id='commit-activity-master']")).perform()
        page.get_by_role('//*[@id="js-repo-pjax-container"]')
        pass

class Test5
    def test_5(self, browser):
        page = browser
        page.goto('https://skillbox.ru/code/')
        page.get_by_role('input[value = 'profession']).click()
        page.get_by_role('// span[text()[contains(., "1С")]] / preceding::input[1]).click()
        el = ('//*[contains(@class, 'slider-ltr')])
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(el)
            .click_and_hold(el)\
            .move_by_offset(xoffset=6, yoffset=12)\
            .perform()
        pass