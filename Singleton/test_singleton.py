import unittest
from singleton import SingletonObject 

obj1 = SingletonObject()

obj1.value = 'Object 1 value'
print(f'Object 1 value: {obj1}')
print('--------------------------------')
obj2 = SingletonObject()
obj2.value = 'Object 2 value'
print(f'Object 2 value: {obj2}')