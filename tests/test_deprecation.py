from __future__ import print_function
from insupportable import Context
import pytest



def test_deprecation_current(capsys):

    c = Context(version=(1,0,0))
    c.set_warner(lambda *x:print('ok'))

    @c.deprecated(version=(1,0,0), remove=(2,0,0))
    def my_deprecated_function():
        pass

    # should definitively not show anything at compile time
    out, err = capsys.readouterr()
    assert 'ok' not in out

    # call the function this should trigger the deprecation
    my_deprecated_function()

    out, err = capsys.readouterr()
    assert 'ok' in out


def test_deprecation_compile(capsys):
    """ test wether or not the warning is triggerd at compile time"""

    c = Context(version=(2,0,0))
    c.set_warner(lambda *x:print('ok'))

    with pytest.raises(DeprecationWarning   ):
        @c.deprecated(version=(1,0,0), remove=(2,0,0))
        def my_deprecated_function():
            pass


def test_deprecation_if_statement(capsys):


    c = Context(version=(1, 0, 0))
    c.set_warner(lambda *x:print('ok'))

    if( c.deprecated(version=(1, 0, 0), remove=(3,0,0))):
        pass

    out, err = capsys.readouterr()
    assert 'ok' in out


def test_deprecation_if_statement2(capsys):
    """ deprecation context in n+1 version should not do a thing"""


    c = Context(version=(1, 0, 0))
    c.set_warner(lambda *x:print('ok'))

    if( c.deprecated(version=(2, 0, 0), remove=(3,0,0))):
        pass

    out, err = capsys.readouterr()
    assert out == ''


def test_deprecation_remove_optional(capsys):
    """ remove omitted should raise on verion.major+1"""

    c = Context(version=(2,0,0))

    with pytest.raises(DeprecationWarning):
        @c.deprecated(version=(1,0,0))
        def my_deprecated_function():
            pass

    with pytest.raises(DeprecationWarning):
        if c.deprecated(version=(1,0,0)):
            pass

def test_deprecation_remove_optional_noraise(capsys):
    """ remove omitted should raise on verion.major+1"""

    c = Context(version=(1,5,0))

    @c.deprecated(version=(1,0,0))
    def my_deprecated_function():
        pass

    if c.deprecated(version=(1,0,0)):
        pass


def test_deprecation_predicate(capsys):
    """
    Context should be able to get a predicate
    """

    c = Context(version=lambda :(2,0,0))
    with pytest.raises(DeprecationWarning):
        @c.deprecated(version=(1,0,0))
        def my_deprecated_function():
            pass

    with pytest.raises(DeprecationWarning):
        if c.deprecated(version=(1,0,0)):
            pass




