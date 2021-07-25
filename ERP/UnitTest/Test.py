# coding:utf-8
# from mathFunc import MathFunc
import unittest


# coding:utf-8
class MathFunc():

    # 加法
    def add_func(self, a, b):
        return a + b

    # 减法
    def minus_func(self, a, b):
        return a - b

    # 乘法
    def multi_func(self, a, b):
        return a * b

    # 除法
    def divide_func(self, a, b):
        return a / b

class TestAddFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("加法测试开始...")

    @classmethod
    def tearDownClass(cls):
        print("加法测试结束...")

    def test_add_func001(self):
        res = MathFunc().add_func(10, 20)
        self.assertEqual(res, 30)

    def test_add_func002(self):
        res = MathFunc().add_func(-10, -20)
        self.assertEqual(res, -30)

    def test_add_func003(self):
        res = MathFunc().add_func(0, 10)
        self.assertEqual(res, 10)

    def test_add_func004(self):
        res = MathFunc().add_func(2.5, 3.7)
        self.assertEqual(res, 6.2)


if __name__ == '__main__':
    unittest.main()