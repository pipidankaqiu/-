import pytest
import yaml

from pytest_homework.caculator import Caculator

"""
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""

with open("E:/Python/pytest_homework/datas/caculator_homework.yaml") as f:
    datas = yaml.safe_load(f)["datas"]
    add_jia = datas["jia"]
    add_chu = datas["chu"]


class TestCaculatorHomework():
    pass

    def setup(self):
        print("计算开始")
        self.calu = Caculator()

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", add_jia)
    def test_jia(self, a, b, expect):
        # self.calu = Caculator()
        result = self.calu.jia(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",add_chu)
    def test_chu(self, a, b, expect):
        result = self.calu.chu(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
