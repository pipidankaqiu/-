import sys

import allure
import pytest
import yaml

# sys.path.append(base_path)
from pytest_homework.caculator import Caculator

"""
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
"""

# 添加yaml文件，将文件中的数据读取出来
with open("E:/Python/pytest_homework/datas/caculator_homework.yaml") as f:
    datas = yaml.safe_load(f)["datas"]
    jia = datas["jia"]
    chu = datas["chu"]

    jian = datas["jian"]
    cheng = datas["cheng"]


@allure.feature("测试计算器")
class TestCaluHomework:

    # 通过allure装饰器增加测试用例标题
    @allure.story("测试加法")
    # 通过装饰器修改用例执行顺序，加法用例第一顺位执行
    @pytest.mark.first
    # 创建parametrize装饰器进行传参
    @pytest.mark.parametrize("a,b,expect", jia)
    # 传入fixture函数名称
    def test_jia(calu, a, b, expect):
        # 实例化计算器
        cal = Caculator()
        # 计算加法
        result = cal.jia(a, b)
        # 判断加法结果是否于期望结果一致
        assert result == expect

    # 通过allure装饰器增加测试用例标题
    @allure.story("测试除法")
    # 通过装饰器修改用例执行顺序，除法用例第四顺位执行
    @pytest.mark.run(order=4)
    # 创建parametrize装饰器进行传参
    @pytest.mark.parametrize("a,b,expect", chu)
    def test_chu(calu, a, b, expect):
        # 实例化计算器
        cal = Caculator()
        # 计算除法
        result = cal.chu(a, b)
        # 如果计算结果是小数，则保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 判断除法结果是否于期望结果一致
        assert result == expect

    # 通过allure装饰器增加测试用例标题
    @allure.story("测试减法")
    # 通过装饰器修改用例执行顺序，减法用例第二顺位执行
    @pytest.mark.run(order=2)
    # 创建parametrize装饰器进行传参
    @pytest.mark.parametrize("a,b,expect", jian)
    def test_jian(calu, a, b, expect):
        # 实例化计算器
        cal = Caculator()
        # 计算减法
        result = cal.jian(a, b)
        # 判断减肥结果是否于期望结果一致
        assert result == expect

    # 通过allure装饰器增加测试用例标题
    @allure.story("测试乘法")
    # 通过装饰器修改用例执行顺序，乘法用例第三顺位执行
    @pytest.mark.run(order=3)
    # 创建parametrize装饰器进行传参
    @pytest.mark.parametrize("a,b,expect", cheng)
    def test_cheng(calu, a, b, expect):
        # 实例化计算器
        cal = Caculator()
        # 计算乘法
        result = cal.cheng(a, b)
        # 如果计算结果是小数，则保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 判断乘法结果是否于期望结果一致
        assert result == expect
