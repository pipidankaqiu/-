import pytest


# 创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
@pytest.fixture(scope="module")
def calu():
    print("计算开始")
    # yield返回【计算结束】
    yield
    print("计算结束")
