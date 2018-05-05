#!/usr/bin/python
import ctypes
from ctypes import *

class bluetooth(Structure):
        _fields_=[('status',c_int),('buf',c_char * 128)]

if __name__ == "__main__":

    func = ctypes.cdll.LoadLibrary("./bluetooth_proxy.so")
    s = bluetooth()
    s.status = 555
    s.buf = bytes('hello,world')
    func.bluetooth_proxy_cb(s)
