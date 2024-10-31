from selenium import webdriver
from CalculatorTest import page


class GetDriver:
    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Edge()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
