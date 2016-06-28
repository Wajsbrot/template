#!/usr/bin/env/ python


# run tests with py.test -q test_class.py from root directory
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
