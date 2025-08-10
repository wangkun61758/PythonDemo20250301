import json
import unittest

import pytest
import yaml


class Test(unittest.TestCase):
    def test_1(self):
        print("test1")
        assert 1 == 1

    def test_2(self):
        print("test2")
        assert 1 == 1
if __name__ == '__main__':
    Test().test_2()
    Test().test_1()


