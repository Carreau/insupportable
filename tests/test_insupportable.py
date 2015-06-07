"""
test_insupportable
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


##########

from insupportable import Context

def test_deprecation_predicate(capsys):
    """
    Context should be able to get a predicate
    """

    import sys

    c = Context(pyversion=lambda:sys.version_info, pysupport=lambda:(3,0,0))


def test_deprecation_predicate_py(capsys):
    """
    should raise on deprecated python versions
    """

    import sys
    import pytest

    c = Context(pyversion=lambda:sys.version_info, pysupport=lambda:(4,0,0))

    with pytest.raises(DeprecationWarning):
        @c.deprecated(version=(1,0,0), pyremove=(1,0,0))
        def my_deprecated_function():
            pass

    with pytest.raises(DeprecationWarning):
        if c.deprecated(version=(1,0,0), pyremove=(1,0,0)):
            pass

def test_deprecation_predicate_py_2(capsys):
    """
    should raise on deprecated python versions
    """

    import sys
    import pytest

    c = Context(pyversion=lambda:sys.version_info, pysupport=lambda:(2,0,0))

    with pytest.raises(DeprecationWarning):
        @c.deprecated(version=(1,0,0), pyremove=(1,0,0))
        def my_deprecated_function():
            pass

    with pytest.raises(DeprecationWarning):
        if c.deprecated(version=(1,0,0), pyremove=(1,0,0)):
            pass








if __name__ == '__main__':
    unittest.main()
