from dev import *

try:
    from prod import *
except ImportError, e:
    # todo: logging config
    print 'Using settings.dev'
