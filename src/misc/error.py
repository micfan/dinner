# coding=utf-8
__author__ = 'Michael Fan'

# todo: error_code分等级，类似http_code
error_info = {
    u'正确': 0,  # no error
    u'错误': 1,
    u'密码错误': 2,
    u'参数错误': 3,
    u'错误：需要登录': 4,
    u'未知错误': 9999
}

# reverse from `enum_error_info`
error_code = {str(v): k for k,v in error_info.items()}

