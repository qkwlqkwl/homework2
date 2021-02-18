import pytest
from python_code.calc import Calculator

#数据库连接
@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库操作")

#获取计算器实例
@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc=Calculator()
    return calc

#创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
#将 fixture 方法存放在 conftest.py ，设置 scope=module
@pytest.fixture(scope='module')
def print_calc():
    print('开始计算')
    yield
    print('结束计算')