from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法 (提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 获取value属性方法
    def base_get_value(self, loc):
        # 注意：一定要返回元素的文本信息
        return self.base_find_element(loc).get_attribute('value')

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./fail.png")
