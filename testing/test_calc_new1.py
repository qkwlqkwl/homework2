'''
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
'''

import allure
import pytest
import yaml

#获取yaml里的加法,除法,减法，乘法参数
with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    # 加法参数
    add_datas = datas['add']['datas']
    add_myid = datas['add']['myid']
    # 除法参数
    div_datas = datas['div']['datas']
    div_myid = datas['div']['myid']
    # 减法参数
    sub_datas = datas['sub']['datas']
    sub_myid = datas['sub']['myid']
    # 乘法参数
    mul_datas = datas['mul']['datas']
    mul_myid = datas['mul']['myid']

#fixture参数化方式，传入加法参数
@pytest.fixture(params=add_datas,ids=add_myid)
def get_add_datas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data

#fixture参数化方式，传入除法参数
@pytest.fixture(params=div_datas,ids=div_myid)
def get_div_datas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data

@allure.feature("测试计算器")
class TestCalc:
    '''
    优化点：
    1，加法和除法使用fixture参数化方式
    2，减法和乘法使用parametrize参数化
    '''
    #控制测试用例顺序按照【1加-2减-3乘-4除】这个顺序执行
    @pytest.mark.run(order=1)
    #加法测试用例，通过get_add_datas获取加法参数
    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self,get_calc,get_add_datas,print_calc):
        with allure.step("计算两个数的相加和"):
            # 调用add方法
            result=get_calc.add(get_add_datas[0],get_add_datas[1])
        #得到结果之后，需要写断言
        #判断result是浮点数，做出保留2位小数的处理
        if isinstance(result,float):
            result= round(result,2)
        assert result==get_add_datas[2]

    # 控制测试用例顺序按照【1加-2减-3乘-4除】这个顺序执行
    @pytest.mark.run(order=4)
    # 除法测试用例，通过get_div_datas获取除法参数
    @allure.story("测试除法")
    @pytest.mark.div
    def test_div(self,get_calc,get_div_datas,print_calc):
        #添加异常处理，被除数不能为0
        with allure.step("计算两个数的相除"):
            try:
                result = get_calc.div(get_div_datas[0],get_div_datas[1])
                # 得到结果之后，需要写断言
                assert result == get_div_datas[2]
            except ZeroDivisionError:
                print('被除数不能为0')

    # 控制测试用例顺序按照【1加-2减-3乘-4除】这个顺序执行
    @pytest.mark.run(order=2)
    @allure.story("测试减法")
    # 除法测试用例，使用parametrize参数化
    @pytest.mark.parametrize('a,b,expect',sub_datas,ids=sub_myid)
    def test_sub(self,get_calc,a,b,expect):
        with allure.step("计算两个数的相减"):
            result = get_calc.sub(a,b)
        assert result == expect

    # 控制测试用例顺序按照【1加-2减-3乘-4除】这个顺序执行
    @pytest.mark.run(order=3)
    @allure.story("测试乘法")
    # 加法测试用例，使用parametrize参数化
    @pytest.mark.parametrize('a,b,expect', mul_datas, ids=mul_myid)
    def test_mul(self, get_calc, a, b, expect):
        with allure.step("计算两个数的相乘"):
            result = get_calc.mul(a, b)
            # 判断result是浮点数，做出保留2位小数的处理
            if isinstance(result, float):
                result = round(result, 2)
        assert result == expect

