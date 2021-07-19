"""
>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(12)
'twelve'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(440)
'four hundred and forty'
>>> numberutil.aswords(25)
'twenty five'
>>> numberutil.aswords(410)
'four hundred and ten'
>>> numberutil.aswords(333)
'three hundred and thirty three'

"""
import doctest
doctest.testmod(verbose=True)


