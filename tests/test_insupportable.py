#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_insupportable
----------------------------------

Tests for `insupportable` module.
"""

import unittest

from insupportable import insupportable


class TestInsupportable(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass


def test_dummy():
    import warnings
    warnings.simplefilter('default')
    import insupportable
    from insupportable import S,PY2,PY3
    for config in ({'PY2':True, 'PY3':True},
                {'PY2':False,'PY3':True},
                {'PY2':True,'PY3':False},
                {'PY2':False,'PY3':False},
    ):
        support = S(**config).support

        def test_support():
            if support(PY3):
                print("you are on python 3")
            elif support(PY2):
                print("you are on python 2")
            else:
                print("Python4")
        test_support()




if __name__ == '__main__':
    unittest.main()
