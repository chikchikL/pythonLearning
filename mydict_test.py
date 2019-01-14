import unittest

from myDict import Dict


# 编写一个测试类，从 unittest.TestCase 继承
# 测试用例要覆盖常用的输入组合、边界条件和异常
# 以 test 开头的方法就是测试方法，不以 test 开头的方法不被认为是测试方法，测试的时候不会被执行
class TestDict(unittest.TestCase):
    def test_key(self):
        print('test_key')
        d = Dict()
        d['key'] = 'value'
        # 调用这些方法就可以断言输出是否是我们所期望的,常用的就是assertEqual
        self.assertEqual(d.key, 'value')

    def test_attrerror(self):
        print('test_attrerror')
        d = Dict()
        # 通过 d.empty 访问不存在的 key 时，期待抛出 AttributeError
        with self.assertRaises(AttributeError):
            value = d.empty

# setUp()和 tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
# 设想你的测试需要启动一个数据库，这时，就可以在 setUp()方法中连接数据库，在 tearDown()方法中关
# 闭数据库，这样，不必在每个测试方法中重复相同的代码
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


# 最简单的运行方式
if __name__ == '__main__':
    unittest.main()


