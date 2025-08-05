# 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
# 在conftest.py配置里写方法可以实现数据共享，不需要import导入，可以跨文件共享
import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser


# 重写hook函数，修改默认编码unicode格式的测试用例，改为支持中文格式的unicode-escape
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


# # 定义全局变量，用于存储浏览器的类型名称
# web_env = {}
#
#
# # 实现命令行注册，解决自定义参数（设置多浏览器运行命令行参数）报错问题
# def pytest_addoption(parser: Parser):
#     """
#     hook函数
#     1、通过 parser.getgroup创建/获取组名: hogwarts
#     2、addoption添加一个命令行选项：pytest xxx.py --browser=chrome
#     :param parser:
#     :return:
#     """
#     hogwarts = parser.getgroup("hogwarts")
#     # pytest .\test_demo.py --browser=chrome
#     # pytest .\test_demo.py --driver=chrome
#     # 注册一个命令行参数
#     hogwarts.addoption("--browser")
#     # 第一个参数"--browser"为指定的命令行参数的形式：--browser=chrome、--driver=chrome
#     # 第二个参数 default="firefox" 指定参数的默认值
#     # 第三个参数 dest = "browser" 用于改写 第一个参数 "--browser" 的名称
#     # 第四个参数 help="指定执行的浏览器" 用于给 hogwarts 组名 做解释
#
#
# def pytest_configure(config: Config):
#     """
#     hook函数： 用于获取到指定传参参数的值（这个值为浏览器的名称，例如chrome）
#     :param config:
#     :return:
#     """
#     config.addinivalue_line("markers",
#                             "test_normal: mark test functions that test data type errors")
#     config.addinivalue_line("markers",
#                             "test_data_type_error: mark test functions that test data type errors")
#     config.addinivalue_line("markers",
#                             "test_data_range: mark test functions that test data type errors")
#     config.addinivalue_line("markers",
#                             "test_zero_division_error: mark test functions that test data type errors")
#     browser = config.getoption("--browser")
#     web_env['browser'] = browser
#     web_env.update(web_env)
#     print(web_env)
#     return web_env
