
.. image:: https://badge.fury.io/py/insupportable.png
    :target: http://badge.fury.io/py/insupportable

.. image:: https://travis-ci.org/Carreau/insupportable.png?branch=master
        :target: https://travis-ci.org/Carreau/insupportable

.. image:: https://pypip.in/d/insupportable/badge.png
        :target: https://pypi.python.org/pypi/insupportable


I am really annoyed, more and more, especially in old project to figure out what code is a war a workaround
for old version of python, or another library. 

This library should provide a simple way to warn you as early as possible when you can remove some legacy code,
that deals with unsupported library version.

By default come pre-configured with Python 2/3 convenience function, but works
with other libraries and more fine grained version numbering.

.. code-block::

    # warn you you have dead code if you
    # drop Python2 support
    from insupportable import support
    if support('PY2'):
        print("You are on python 2")
    else:
        print("You are on python 3")


.. code-block::

    # warn you you have dead code if you
    # drop Python2 support
    from insupportable import support
    if support('PY3'):
        print("You are on python 3")
    else:
        print("You are on python 2")


Set it up to drop Python2 support.
----------------------------------

Quick and dirty way, modify global config, which is not recommended as it may
affect other libraries that use this too, but super usefull. 

.. code-block:: 

    support.config(PY2=False)

    if support(PY2):
        print("You are on python 2")
    else:
        print("You are on python 3")


warn the following:

.. code-block::

    mymodule/myfile.py:3: UserWarning: You are not supporting PY2 anymore 
      if support(PY2):
    mymodule/myfile.py:3: UserWarning: PY2 is the last supported feature of this group, you can simplifiy this logic. 
      if support(PY2):

More involve way, create a config context that have effect only locally: 

.. code-block::

    from insupportable import S

    support = S(PY2=False).support

    ....

Advance configuration/custom features:
--------------------------------------

Example:

.. code-block::
    support.config(config=({
        'WindowsPhone':True,
        'Android'     :False,
        'iOS'         :False
       },))
    if support('WindowsPhone'):
        print('Click on start menu')
    else:
        print("Probably Android - but you don't support it anymore")

.. code-block::
        mymodule/myfile.py:1: UserWarning: WindowsPhone is the last supported feature of this group, you can simplifiy this logic. 
          if support('WindowsPhone'):




TODO:
-----

Write predicates and document like:

.. code-block::

    if workaround('tornado==2.2'):
        # do something special


The predicate would decide wether or not to yield depending on the version of `tornado`, 
and warn if min tornado is  higher than 2.2


Deprecation decorator:

.. code-block::

    @deprecated_since('2.3.1',will_remove='3.0.0')
    def my_api('something'):
        """deprecated fucntion that should 
        warn user when function is **called**

        when module version is >= 3.0, the decorator should warn **developper** at **compile** time
        that code has to be removed. 
        """

This case is more interesting than `support()` as there is 2 pass, the decoration of the function itsef,
and the execution of the function. `will_remove` should infer next major I guess. 
Should we add option to deprecate after/at a date for some case like API.

.. code-block::
    
    @deprecate_after(date='2015/10/15'):
    def marty_from_the_future(self):
        """
        Docs has some invalid ssl certificates ?
        """





* Free software: MIT license
* Documentation: https://insupportable.readthedocs.org.

Features
--------

TODO
----



