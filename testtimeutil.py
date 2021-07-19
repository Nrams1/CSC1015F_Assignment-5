"""
>>> import timeutil
>>> timeutil.validate ("1 32 p.m.")
False
>>> timeutil.validate ("432:10 p.m.")
False
>>> timeutil.validate ("02:56 a.m.")
False
>>> timeutil.validate ("13:43 ")
False
>>> timeutil.validate ("1:453 a.m.")
False
>>> timeutil.validate ("11:00 a.m.")
True

"""
import doctest
doctest.testmod(verbose=True)


