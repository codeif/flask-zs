import sys

from flask_zs.exceptions import CustomException

current_module = sys.modules[__name__]


exceptions = [
    ('NoError', 0, 'OK'),
    ('LoginRequired', 1001, 'Login required.'),
]


for name, errcode, errmsg in exceptions:
    cls = type(name,
               (CustomException,),
               {'errcode': errcode, 'errmsg': errmsg})
    setattr(current_module, name, cls)
