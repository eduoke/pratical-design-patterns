import pytest

class TestSingletonObject:

    # SingletonObject creates only one instance
    def test_singleton_creates_only_one_instance(self):
        obj1 = SingletonObject()
        obj2 = SingletonObject()
        assert obj1 is obj2, "SingletonObject should create only one instance"

    # SingletonObject handles multiple instantiations correctly
    def test_singleton_handles_multiple_instantiations(self):
        obj1 = SingletonObject()
        obj1.value = 10
        obj2 = SingletonObject()
        assert obj2.value == 10, "SingletonObject should handle multiple instantiations correctly"