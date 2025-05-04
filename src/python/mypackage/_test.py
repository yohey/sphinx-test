# -*- coding: utf-8 -*-

from ctypes import POINTER, byref, c_double

from ._findlib import _libmypackage


def add(a, b):
    _libmypackage.ffi_mypackage_add.argtypes = [POINTER(c_double), POINTER(c_double)]
    _libmypackage.ffi_mypackage_add.restype = c_double
    return _libmypackage.ffi_mypackage_add(byref(c_double(a)), byref(c_double(b)))
