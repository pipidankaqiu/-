"""
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
"""
import pytest
import yaml

with open("E:/Python/pytest_homework/datas/caculator_homework.yaml", encoding='UTF-8') as f:
    # 读取所有数据
    datas = yaml.safe_load(f)
    # 获取加的数据和用例名称
    jia = datas["jia"]
    jia_data = jia["jia_datas"]
    jia_id = jia["jia_ids"]
    # 获取除的数据和用例名称
    chu_data = datas["chu"]["chu_datas"]
    chu_id = datas["chu"]["chu_ids"]
    # 获取减的数据和用例名称
    jian = datas["jian"]
    jian_data = jian["jian_datas"]
    jian_id = jian["jian_ids"]
    # 获取乘法的数据和用例名称
    cheng_data = datas["cheng"]["cheng_datas"]
    cheng_id = datas["cheng"]["cheng_ids"]


# 使用fixture方法，获取加法的参数
@pytest.fixture(params=jia_data, ids=jia_id)
def get_jia_datas(request):
    data = request.param
    yield data


# 使用fixture方法，获取除法的参数
@pytest.fixture(params=chu_data, ids=chu_id)
def get_chu_datas(request):
    data = request.param
    yield data


# 使用fixture方法，获取减法的参数
@pytest.fixture(params=jian_data, ids=jian_id)
def get_jian_datas(request):
    data = request.param
    yield data


# 使用fixture方法，获取乘法的参数
@pytest.fixture(params=cheng_data, ids=cheng_id)
def get_cheng_datas(request):
    data = request.param
    yield data


class Test_Calu_Homework():

    # 使用order将加法用例顺序排在第一位
    @pytest.mark.run(order=1)
    # 测试加法，通过get_calu得到计算器，通过get_jia_datas得到加法的测试数据和用力名称
    def test_jia(self, get_calu, get_jia_datas):
        result = get_calu.jia(get_jia_datas[0], get_jia_datas[1])
        assert result == get_jia_datas[2]

    # 使用order将除法用例顺序排在第四位
    @pytest.mark.run(order=4)
    # 测试除法，通过get_calu得到计算器，通过get_jia_datas得到除法的测试数据和用力名称
    def test_chu(self, get_calu, get_chu_datas):
        result = get_calu.chu(get_chu_datas[0], get_chu_datas[1])
        # 如果结果为小数，则保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            assert result == get_chu_datas[2]

    # 使用order将减法用例顺序排在第二位
    @pytest.mark.run(order=2)
    # 测试减法，通过get_calu得到计算器，通过get_jia_datas得到减法的测试数据和用力名称
    def test_jian(self, get_calu, get_jian_datas):
        result = get_calu.jian(get_jian_datas[0], get_jian_datas[1])
        assert result == get_jian_datas[2]

    # 使用order将乘法用例顺序排在第三位
    @pytest.mark.run(order=3)
    # 测试乘法，通过get_calu得到计算器，通过get_jia_datas得到乘法的测试数据和用力名称
    def test_cheng(self, get_calu, get_cheng_datas):
        result = get_calu.cheng(get_cheng_datas[0], get_cheng_datas[1])
        # 如果结果为小数，则保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
            assert result == get_cheng_datas[2]
