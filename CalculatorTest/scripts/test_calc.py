# 导包
import unittest
from parameterized import parameterized

from CalculatorTest.base.get_driver import GetDriver
from CalculatorTest.page.page_calc import PageCalc
from CalculatorTest.tool.read_json import read_json


def get_data():
    datas = read_json("calc.json")
    # 新建空列表
    arr = []
    for data in datas.values():
        arr.append((data['a'], data['b'], data['expect']))
    return arr


# 新建测试类 并 继承
class TestCalc(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # 初始化 计算页面对象
        cls.driver = GetDriver().get_driver()
        cls.calc = PageCalc(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # 关闭driver
        GetDriver().quit_driver()

    @parameterized.expand(get_data())
    def test_add_calc(self, a, b, expect):
        # 计算业务
        self.calc.page_add_calc(a, b)
        print(f"预期结果为：{expect}实际计算结果为：{self.calc.page_get_value()}")
        try:
            # 断言
            self.assertEqual(self.calc.page_get_value(), str(expect))
        except:
            # 截图
            self.calc.page_get_image()
            raise
