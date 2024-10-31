from CalculatorTest import page
from CalculatorTest.base.base import Base


class PageCalc(Base):
    # 点击数字
    def page_click_num(self, num):
        for i in str(num):
            loc = 'css selector', f'#simple{i}'
            self.base_click(loc)

    # 点击加号
    def page_click_add(self):
        self.base_click(page.calc_add)

    # 点击等号
    def page_click_eq(self):
        self.base_click(page.calc_eq)

    # 获取结果
    def page_get_value(self):
        return self.base_get_value(page.calc_result)

    # 点击清屏
    def page_click_clear(self):
        self.base_click(page.calc_clear)

    # 截图
    def page_get_image(self):
        self.base_get_image()

    # 组装方法
    def page_add_calc(self, a, b):
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()
