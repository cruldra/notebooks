# 导入子模块
from .module1 import function1
from .module2 import function2

print("__init__.py is running")

# 定义包级别的变量
__version__ = '1.0.0'


# 定义包级别的函数
def package_function():
    print("This is a function defined at the package level.")


# 使用 __all__ 控制 * 导入行为
__all__ = ['function1', 'function2', 'package_function']
