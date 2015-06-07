from __future__ import print_function
from insupportable import Context



def test_deprecation(capsys):

    c = Context(version=(1,0,0))
    c.set_warner(lambda *x:print('ok'))

    @c.deprecated(version=(1,0,0), remove=(3,0,0))
    def my_deprecated_function():
        pass

    my_deprecated_function()

    out, err = capsys.readouterr() 
    assert 'ok' in out
