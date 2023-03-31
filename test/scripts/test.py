"""
    isort:skip_file
"""

import package
from package import Class1, Class2, func_1, func_2
from package3 import *


class TestClass(BaseClass1, BaseClass2):
    """ Hola! """
    def __init__(self, x: int, y: List[Union[None, str]], z='default',
                 *args, **kwargs):
        super().__init__()
        self.x = x  # type: int

    def method1(self):
        pass


@decorator
async def test2(x, y, z):
    async for i in x:
        yield y
    with open('text', 'r', encoding='utf-8') as f:
        while True:
            x += 1

@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print('Gre\'ater')
    return (param2 - param1 + 1 + 0b10l) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
