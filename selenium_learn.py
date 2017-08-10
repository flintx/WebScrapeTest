import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @unittest.skip("don't need.")
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        # print(driver.page_source)
        assert "No results found." not in driver.page_source

    def test_login_in_bilibili_com(self):
        driver = self.driver
        driver.get("https://passport.bilibili.com/login")
        self.assertIn("bilibili", driver.title)
        elem_username = driver.find_element_by_id("login-username")
        elem_username.send_keys("example@mail.com")
        elem_password = driver.find_element_by_id("login-passwd")
        elem_password.send_keys("example_password")
        driver.save_screenshot("E:\\screen.png")
        # print(driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    # browser = webdriver.Chrome()
    # browser.get("http://www.baidu.com")
    # browser.close()
    # browser.quit()
    unittest.main()
