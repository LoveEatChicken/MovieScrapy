#!/usr/bin/env python
# coding: utf-8

def md5(str):
    import hashlib
    if isinstance(str, basestring):
        m = hashlib.md5()
        m.update(str.encode("utf8"))
        return m.hexdigest()
    else:
        return ''