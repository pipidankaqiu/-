import pytest
import yaml

from pytest_homework.caculator import Caculator

"""
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""

# 添加yaml文件，将文件中的加法和除法读取出来
with open("E:/Python/pytest_homework/datas/caculator_homework.yaml") as f:
    datas = yaml.safe_load(f)["datas"]
    add_jia = datas["jia"]
    add_chu = datas["chu"]


class TestCaculatorHomework():
    pass

    # 在调用测试方法之前打印【开始计算】
    def setup(self):
        print("计算开始")
        # 实例化计算器
        self.calu = Caculator()

    # 在调用测试方法之后打印【计算结束】
    def teardown(self):
        print("计算结束")

    # 通过装饰器parametrize传入加法的参数
    @pytest.mark.parametrize("a,b,expect", add_jia)
    def test_jia(self, a, b, expect):
        # self.calu = Caculator()
        # 进行加法运算
        result = self.calu.jia(a, b)
        # 判断运算结果是否和预期结果一致
        assert result == expect

    # 通过装饰器parametrize传入除法的参数
    @pytest.mark.parametrize("a,b,expect", add_chu)
    def test_chu(self, a, b, expect):
        # 进行除法运算
        result = self.calu.chu(a, b)
        # 如果运算结果为小数，则保留2位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 判断运算结果是否和预期结果一致
        assert result == expect
