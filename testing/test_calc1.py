import pytest
import yaml

from python_code.calc import Calculator

# with open("./datas/calc.yaml") as f:
#     # 获取加法参数
#     add1 = yaml.safe_load(f)['add']
#     add_datas = add1['datas']
#     add_myid = add1['myid']
#     # 获取除法参数
#     div1 = yaml.safe_load(f)['div']
#     div_datas = div1['datas1']
#     div_myid = div1['myid1']

#获取yaml里的加法和除法参数
with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_myid = datas['add']['myid']
    div_datas = datas['div']['datas']
    div_myid = datas['div']['myid']


class TestCalc1:
    def setup_class(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    def setup(self):
        print("每个测试用例开始")

    def teardown(self):
        print("每个测试用例结束")

    # 加法测试用例
    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas, ids=add_myid
    )
    def test_add1(self, a, b, expect):
        result = self.calc.add(a, b)
        # 判断result是浮点数，做出保留2位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect

    #除法测试用例
    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas, ids=div_myid
    )
    def test_div1(self, a, b, expect):
        #添加异常处理，被除数不能为0
        try:
            result = self.calc.div(a, b)
            # 得到结果之后，需要写断言
            assert result == expect
        except ZeroDivisionError:
            print('被除数不能为0')

