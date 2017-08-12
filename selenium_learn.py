import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
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


class TestSeleniumFind(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_selenium_find(self):
        browser = self.driver
        browser.get("http://www.baidu.com")

        # by id, 等价于 elem_qrcode_img = browser.find_element(By.CLASS_NAME, "qrcode-img")
        elem_img_qrcode = browser.find_element_by_class_name("qrcode-img")
        print(elem_img_qrcode.size)

        # by name, 等价于 elem_news_a = browser.find_element(By.NAME, "tj_trnews")
        elem_a_news = browser.find_element_by_name("tj_trnews")
        print(elem_a_news.text)

        # by class name, 等价于 elem_qrcode_img = browser.find_element(By.ID, "su")
        elem_baidu_button = browser.find_element_by_id("su")

        # by tag name, 等价于 elem_p = browser.find_elements(By.TAG_NAME, "p")
        elem_p_list = browser.find_elements_by_tag_name("p")
        elem_p_text_list = list(map(lambda x: x.text, elem_p_list))
        print(elem_p_text_list)

        # 通过链接文本内容, 等价于 elem_tieba_a = browser.find_element(By.LINK_TEXT, "贴吧")
        elem_a_tieba = browser.find_element_by_link_text("贴吧")
        print(elem_a_tieba.get_property("href"))

        # 通过部分链接文本内容, 等价于 elem_hao123_a = browser.find_element(By.PARTIAL_LINK_TEXT, "hao")
        elem_a_hao123 = browser.find_element_by_partial_link_text("hao")
        print(elem_a_hao123.text + ": " + elem_a_hao123.get_property("href"))

        # by XPath or CSS Selector
        # elem_input_kw_by_xpath = browser.find_element_by_xpath("//*[@id='kw']")
        elem_input_kw_by_xpath = browser.find_element(By.XPATH, "//*[@id='kw']")
        elem_input_kw = browser.find_element_by_css_selector("#kw")
        elem_input_kw_by_xpath.send_keys("AcFun")
        elem_input_kw.send_keys("bilibili")
        elem_baidu_button.click()


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestSeleniumFind("test_selenium_find"))
    # About verbosity:
    # You only have 3 different levels:
    #   0 (quiet): you just get the total numbers of tests executed and the global result
    #   1 (default): you get the same plus a dot for every successful test or a F for every failure
    #   2 (verbose): you get the help string of every test and the result
    # You can use command line args rather than the verbosity argument: --quiet and --verbose which
    # would do something similar to passing 0 or 2 to the runner.
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

    # unittest.main()
