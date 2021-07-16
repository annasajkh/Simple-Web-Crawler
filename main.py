import sys

import math as python_lib_Math
import math as Math
import inspect as python_lib_Inspect
import sys as python_lib_Sys
import random as python_lib_Random
import re as python_lib_Re
import socket as python_lib_Socket
import ssl as python_lib_Ssl
import time as python_lib_Time
import traceback as python_lib_Traceback
from io import StringIO as python_lib_io_StringIO
from socket import socket as python_lib_socket_Socket
from ssl import SSLContext as python_lib_ssl_SSLContext
import urllib.parse as python_lib_urllib_Parse
from threading import Semaphore as Lock
from threading import RLock as sys_thread__Mutex_NativeRLock
import threading
from threading import Thread


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False



class Enum:
    _hx_class_name = "Enum"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        self.tag = tag
        self.index = index
        self.params = params

    def __str__(self):
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'



class Class: pass


class Crawler:
    _hx_class_name = "Crawler"
    __slots__ = ()
    _hx_statics = ["crawl"]

    @staticmethod
    def crawl(link):
        print(str(("crawling " + ("null" if link is None else link))))
        result = sys_Http.requestUrl(link)
        links = haxe_ds_List()
        _g = 0
        _g1 = result.split(">")
        while (_g < len(_g1)):
            line = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            startIndex = None
            if (((line.find("href=\"") if ((startIndex is None)) else HxString.indexOfImpl(line,"href=\"",startIndex))) != -1):
                _this = HxOverrides.arrayGet(line.split("href=\""), 1)
                link = python_internal_ArrayImpl._get(_this.split("\""), 0)
                startIndex1 = None
                if (((link.find("http") if ((startIndex1 is None)) else HxString.indexOfImpl(link,"http",startIndex1))) != -1):
                    links.add(link)
        return links


class EReg:
    _hx_class_name = "EReg"
    __slots__ = ("pattern", "matchObj", "_hx_global")
    _hx_fields = ["pattern", "matchObj", "global"]

    def __init__(self,r,opt):
        self.matchObj = None
        self._hx_global = False
        options = 0
        _g = 0
        _g1 = len(opt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(opt))) else ord(opt[i]))
            if (c == 109):
                options = (options | python_lib_Re.M)
            if (c == 105):
                options = (options | python_lib_Re.I)
            if (c == 115):
                options = (options | python_lib_Re.S)
            if (c == 117):
                options = (options | python_lib_Re.U)
            if (c == 103):
                self._hx_global = True
        self.pattern = python_lib_Re.compile(r,options)



class Lambda:
    _hx_class_name = "Lambda"
    __slots__ = ()
    _hx_statics = ["exists"]

    @staticmethod
    def exists(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                return True
        return False


class Main:
    _hx_class_name = "Main"
    __slots__ = ()
    _hx_statics = ["main"]

    @staticmethod
    def main():
        links = haxe_ds_List()
        result = Crawler.crawl("http://www.google.com/")
        _g_head = result.h
        while (_g_head is not None):
            val = _g_head.item
            _g_head = _g_head.next
            link = val
            links.add(link)
        while (not links.isEmpty()):
            def _hx_local_0():
                nonlocal result
                link = links.pop()
                try:
                    result = Crawler.crawl(link)
                except BaseException as _g:
                    e = haxe_Exception.caught(_g)
                    print(str(("Failed crawling url " + ("null" if link is None else link))))
                    print(str(e))
                _g1_head = result.h
                while (_g1_head is not None):
                    val = _g1_head.item
                    _g1_head = _g1_head.next
                    link = val
                    links.add(link)
            sys_thread__Thread_HxThread.create(_hx_local_0,False)


class Reflect:
    _hx_class_name = "Reflect"
    __slots__ = ()
    _hx_statics = ["isFunction", "compareMethods"]

    @staticmethod
    def isFunction(f):
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compareMethods(f1,f2):
        if HxOverrides.eq(f1,f2):
            return True
        if (isinstance(f1,python_internal_MethodClosure) and isinstance(f2,python_internal_MethodClosure)):
            m1 = f1
            m2 = f2
            if HxOverrides.eq(m1.obj,m2.obj):
                return (m1.func == m2.func)
            else:
                return False
        if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
            return False
        return False


class Std:
    _hx_class_name = "Std"
    __slots__ = ()
    _hx_statics = ["isOfType", "string", "parseInt"]

    @staticmethod
    def isOfType(v,t):
        if ((v is None) and ((t is None))):
            return False
        if (t is None):
            return False
        if (t == Dynamic):
            return (v is not None)
        isBool = isinstance(v,bool)
        if ((t == Bool) and isBool):
            return True
        if ((((not isBool) and (not (t == Bool))) and (t == Int)) and isinstance(v,int)):
            return True
        vIsFloat = isinstance(v,float)
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and (t == Int)):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                None
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        if (((not isBool) and (t == Float)) and isinstance(v,(float, int))):
            return True
        if (t == str):
            return isinstance(v,str)
        isEnumType = (t == Enum)
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        if isEnumType:
            return False
        isClassType = (t == Class)
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        if isClassType:
            return False
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        if python_lib_Inspect.isclass(t):
            cls = t
            loop = None
            def _hx_local_1(intf):
                f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                if (f is not None):
                    _g = 0
                    while (_g < len(f)):
                        i = (f[_g] if _g >= 0 and _g < len(f) else None)
                        _g = (_g + 1)
                        if (i == cls):
                            return True
                        else:
                            l = loop(i)
                            if l:
                                return True
                    return False
                else:
                    return False
            loop = _hx_local_1
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        return python_Boot.toString1(s,"")

    @staticmethod
    def parseInt(x):
        if (x is None):
            return None
        try:
            return int(x)
        except BaseException as _g:
            None
            base = 10
            _hx_len = len(x)
            foundCount = 0
            sign = 0
            firstDigitIndex = 0
            lastDigitIndex = -1
            previous = 0
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    if (foundCount > 0):
                        return None
                    continue
                else:
                    c1 = c
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                foundCount = (foundCount + 1)
                lastDigitIndex = i
                previous = c
            if (firstDigitIndex <= lastDigitIndex):
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            return None


class Float: pass


class Int: pass


class Bool: pass


class Dynamic: pass


class StringTools:
    _hx_class_name = "StringTools"
    __slots__ = ()
    _hx_statics = ["isSpace", "ltrim", "rtrim"]

    @staticmethod
    def isSpace(s,pos):
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        c = HxString.charCodeAt(s,pos)
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    __slots__ = ()


class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "get_message", "get_native"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        self._hx___skipStack = 0
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    def toString(self):
        return self.get_message()

    def get_message(self):
        return str(self)

    def get_native(self):
        return self._hx___nativeException

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            e = haxe_ValueException(value)
            e._hx___skipStack = (e._hx___skipStack + 1)
            return e



class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "exceptionStack"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value

    def unwrap(self):
        return self.value



class haxe_ds_List:
    _hx_class_name = "haxe.ds.List"
    __slots__ = ("h", "q", "length")
    _hx_fields = ["h", "q", "length"]
    _hx_methods = ["add", "pop", "isEmpty"]

    def __init__(self):
        self.q = None
        self.h = None
        self.length = 0

    def add(self,item):
        x = haxe_ds__List_ListNode(item,None)
        if (self.h is None):
            self.h = x
        else:
            self.q.next = x
        self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def pop(self):
        if (self.h is None):
            return None
        x = self.h.item
        self.h = self.h.next
        if (self.h is None):
            self.q = None
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 - 1)
        _hx_local_1
        return x

    def isEmpty(self):
        return (self.h is None)



class haxe_ds__List_ListNode:
    _hx_class_name = "haxe.ds._List.ListNode"
    __slots__ = ("item", "next")
    _hx_fields = ["item", "next"]

    def __init__(self,item,next):
        self.item = item
        self.next = next



class haxe_ds_ObjectMap:
    _hx_class_name = "haxe.ds.ObjectMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "remove"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def remove(self,key):
        r = (key in self.h)
        if r:
            del self.h[key]
        return r



class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()



class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        self.posInfos = None
        super().__init__(message,previous)
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos

    def toString(self):
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))



class haxe_exceptions_NotImplementedException(haxe_exceptions_PosException):
    _hx_class_name = "haxe.exceptions.NotImplementedException"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_exceptions_PosException


    def __init__(self,message = None,previous = None,pos = None):
        if (message is None):
            message = "Not implemented"
        super().__init__(message,previous,pos)


class haxe_http_HttpBase:
    _hx_class_name = "haxe.http.HttpBase"
    _hx_fields = ["url", "responseBytes", "responseAsString", "postData", "postBytes", "headers", "params", "emptyOnData"]
    _hx_methods = ["onData", "onBytes", "onError", "onStatus", "hasOnData", "success", "get_responseData"]

    def __init__(self,url):
        self.emptyOnData = None
        self.postBytes = None
        self.postData = None
        self.responseAsString = None
        self.responseBytes = None
        self.url = url
        self.headers = []
        self.params = []
        self.emptyOnData = self.onData

    def onData(self,data):
        pass

    def onBytes(self,data):
        pass

    def onError(self,msg):
        pass

    def onStatus(self,status):
        pass

    def hasOnData(self):
        return (not Reflect.compareMethods(self.onData,self.emptyOnData))

    def success(self,data):
        self.responseBytes = data
        self.responseAsString = None
        if self.hasOnData():
            self.onData(self.get_responseData())
        self.onBytes(self.responseBytes)

    def get_responseData(self):
        if ((self.responseAsString is None) and ((self.responseBytes is not None))):
            self.responseAsString = self.responseBytes.getString(0,self.responseBytes.length,haxe_io_Encoding.UTF8)
        return self.responseAsString



class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_methods = ["sub", "getString", "toString"]
    _hx_statics = ["alloc", "ofString"]

    def __init__(self,length,b):
        self.length = length
        self.b = b

    def sub(self,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_Bytes(_hx_len,self.b[pos:(pos + _hx_len)])

    def getString(self,pos,_hx_len,encoding = None):
        tmp = (encoding is None)
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

    def toString(self):
        return self.getString(0,self.length)

    @staticmethod
    def alloc(length):
        return haxe_io_Bytes(length,bytearray(length))

    @staticmethod
    def ofString(s,encoding = None):
        b = bytearray(s,"UTF-8")
        return haxe_io_Bytes(len(b),b)



class haxe_io_BytesBuffer:
    _hx_class_name = "haxe.io.BytesBuffer"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["getBytes"]

    def __init__(self):
        self.b = bytearray()

    def getBytes(self):
        _hx_bytes = haxe_io_Bytes(len(self.b),self.b)
        self.b = None
        return _hx_bytes



class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "close", "set_bigEndian", "writeFullBytes", "prepare", "writeString"]

    def writeByte(self,c):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        b = s.b
        k = _hx_len
        while (k > 0):
            self.writeByte(b[pos])
            pos = (pos + 1)
            k = (k - 1)
        return _hx_len

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def writeFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.writeBytes(s,pos,_hx_len)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def prepare(self,nbytes):
        pass

    def writeString(self,s,encoding = None):
        b = haxe_io_Bytes.ofString(s,encoding)
        self.writeFullBytes(b,0,b.length)



class haxe_io_BytesOutput(haxe_io_Output):
    _hx_class_name = "haxe.io.BytesOutput"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["writeByte", "writeBytes", "getBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self):
        self.b = haxe_io_BytesBuffer()
        self.set_bigEndian(False)

    def writeByte(self,c):
        self.b.b.append(c)

    def writeBytes(self,buf,pos,_hx_len):
        _this = self.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > buf.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        _this.b.extend(buf.b[pos:(pos + _hx_len)])
        return _hx_len

    def getBytes(self):
        return self.b.getBytes()


class haxe_io_Encoding(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Encoding"
    _hx_constructs = ["UTF8", "RawNative"]
haxe_io_Encoding.UTF8 = haxe_io_Encoding("UTF8", 0, ())
haxe_io_Encoding.RawNative = haxe_io_Encoding("RawNative", 1, ())


class haxe_io_Eof:
    _hx_class_name = "haxe.io.Eof"
    __slots__ = ()
    _hx_methods = ["toString"]

    def __init__(self):
        pass

    def toString(self):
        return "Eof"


class haxe_io_Error(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Error"
    _hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

    @staticmethod
    def Custom(e):
        return haxe_io_Error("Custom", 3, (e,))
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, ())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, ())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, ())


class haxe_io_Input:
    _hx_class_name = "haxe.io.Input"
    __slots__ = ()
    _hx_methods = ["readByte", "readBytes"]

    def readByte(self):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Input.hx", 'lineNumber': 53, 'className': "haxe.io.Input", 'methodName': "readByte"}))

    def readBytes(self,s,pos,_hx_len):
        k = _hx_len
        b = s.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        try:
            while (k > 0):
                b[pos] = self.readByte()
                pos = (pos + 1)
                k = (k - 1)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return (_hx_len - k)



class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()



class python_Boot:
    _hx_class_name = "python.Boot"
    __slots__ = ()
    _hx_statics = ["keywords", "toString1", "fields", "simpleField", "hasField", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

    @staticmethod
    def toString1(o,s):
        if (o is None):
            return "null"
        if isinstance(o,str):
            return o
        if (s is None):
            s = ""
        if (len(s) >= 5):
            return "<...>"
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                None
                return str(o)
        if isinstance(o,list):
            o1 = o
            l = len(o1)
            st = "["
            s = (("null" if s is None else s) + "\t")
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                prefix = ""
                if (i > 0):
                    prefix = ","
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            st = (("null" if st is None else st) + "]")
            return st
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        if hasattr(o,"__class__"):
            if isinstance(o,_hx_AnonObject):
                toStr = None
                try:
                    fields = python_Boot.fields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    None
                    return "{ ... }"
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            if isinstance(o,Enum):
                o1 = o
                l = len(o1.params)
                hasParams = (l > 0)
                if hasParams:
                    paramsStr = ""
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        prefix = ""
                        if (i > 0):
                            prefix = ","
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    fields = python_Boot.getInstanceFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
                else:
                    fields = python_Boot.getClassFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
            if (o == str):
                return "#String"
            if (o == list):
                return "#Array"
            if callable(o):
                return "function"
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            if hasattr(o,"__str__"):
                return o.__str__([])
            if hasattr(o,"__name__"):
                return o.__name__
            return "???"
        else:
            return str(o)

    @staticmethod
    def fields(o):
        a = []
        if (o is not None):
            if hasattr(o,"_hx_fields"):
                fields = o._hx_fields
                if (fields is not None):
                    return list(fields)
            if isinstance(o,_hx_AnonObject):
                d = o.__dict__
                keys = d.keys()
                handler = python_Boot.unhandleKeywords
                for k in keys:
                    if (k != '_hx_disable_getattr'):
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                d = o.__dict__
                keys1 = d.keys()
                for k in keys1:
                    a.append(k)
        return a

    @staticmethod
    def simpleField(o,field):
        if (field is None):
            return None
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def hasField(o,field):
        if isinstance(o,_hx_AnonObject):
            return o._hx_hasattr(field)
        return hasattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

    @staticmethod
    def getInstanceFields(c):
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        sc = python_Boot.getSuperClass(c)
        if (sc is None):
            return f
        else:
            scArr = python_Boot.getInstanceFields(sc)
            scMap = set(scArr)
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                if (not (f1 in scMap)):
                    scArr.append(f1)
            return scArr

    @staticmethod
    def getSuperClass(c):
        if (c is None):
            return None
        try:
            if hasattr(c,"_hx_super"):
                return c._hx_super
            return None
        except BaseException as _g:
            None
        return None

    @staticmethod
    def getClassFields(c):
        if hasattr(c,"_hx_statics"):
            x = c._hx_statics
            return list(x)
        else:
            return []

    @staticmethod
    def unhandleKeywords(name):
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            real = HxString.substr(name,python_Boot.prefixLength,None)
            if (real in python_Boot.keywords):
                return real
        return name


class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    __slots__ = ()
    _hx_statics = ["_get", "_set"]

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        l = len(x)
        while (l < idx):
            x.append(None)
            l = (l + 1)
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        return v


class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "eq", "stringOrNull", "arrayGet"]

    @staticmethod
    def iterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def arrayGet(a,i):
        if isinstance(a,list):
            x = a
            if ((i > -1) and ((i < len(x)))):
                return x[i]
            else:
                return None
        else:
            return a[i]


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)



class HxString:
    _hx_class_name = "HxString"
    __slots__ = ()
    _hx_statics = ["charCodeAt", "indexOfImpl", "substring", "substr"]

    @staticmethod
    def charCodeAt(s,index):
        if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
            return None
        else:
            return ord(s[index])

    @staticmethod
    def indexOfImpl(s,_hx_str,startIndex):
        if (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        return s.find(_hx_str, startIndex)

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        if (startIndex < 0):
            startIndex = 0
        if (endIndex is None):
            return s[startIndex:]
        else:
            if (endIndex < 0):
                endIndex = 0
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        if (_hx_len is None):
            return s[startIndex:]
        else:
            if (_hx_len == 0):
                return ""
            if (startIndex < 0):
                startIndex = (len(s) + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            return s[startIndex:(startIndex + _hx_len)]


class sys_net_Socket:
    _hx_class_name = "sys.net.Socket"
    __slots__ = ("_hx___s", "input", "output")
    _hx_fields = ["__s", "input", "output"]
    _hx_methods = ["__initSocket", "close", "connect", "shutdown", "setTimeout", "fileno"]

    def __init__(self):
        self.output = None
        self.input = None
        self._hx___s = None
        self._hx___initSocket()
        self.input = sys_net__Socket_SocketInput(self._hx___s)
        self.output = sys_net__Socket_SocketOutput(self._hx___s)

    def _hx___initSocket(self):
        self._hx___s = python_lib_socket_Socket()

    def close(self):
        self._hx___s.close()

    def connect(self,host,port):
        host_str = host.toString()
        self._hx___s.connect((host_str, port))

    def shutdown(self,read,write):
        self._hx___s.shutdown((python_lib_Socket.SHUT_RDWR if ((read and write)) else (python_lib_Socket.SHUT_RD if read else python_lib_Socket.SHUT_WR)))

    def setTimeout(self,timeout):
        self._hx___s.settimeout(timeout)

    def fileno(self):
        return self._hx___s.fileno()



class python_net_SslSocket(sys_net_Socket):
    _hx_class_name = "python.net.SslSocket"
    __slots__ = ("hostName",)
    _hx_fields = ["hostName"]
    _hx_methods = ["__initSocket", "connect"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = sys_net_Socket


    def __init__(self):
        self.hostName = None
        super().__init__()

    def _hx___initSocket(self):
        context = python_lib_ssl_SSLContext(python_lib_Ssl.PROTOCOL_SSLv23)
        context.verify_mode = python_lib_Ssl.CERT_REQUIRED
        context.set_default_verify_paths()
        context.options = (context.options | python_lib_Ssl.OP_NO_SSLv2)
        context.options = (context.options | python_lib_Ssl.OP_NO_SSLv3)
        context.options = (context.options | python_lib_Ssl.OP_NO_COMPRESSION)
        context.options = (context.options | python_lib_Ssl.OP_NO_TLSv1)
        self._hx___s = python_lib_socket_Socket()
        self._hx___s = context.wrap_socket(self._hx___s,False,True,True,self.hostName)

    def connect(self,host,port):
        self.hostName = host.host
        super().connect(host,port)



class sys_Http(haxe_http_HttpBase):
    _hx_class_name = "sys.Http"
    __slots__ = ("noShutdown", "cnxTimeout", "responseHeaders", "chunk_size", "chunk_buf", "file")
    _hx_fields = ["noShutdown", "cnxTimeout", "responseHeaders", "chunk_size", "chunk_buf", "file"]
    _hx_methods = ["request", "customRequest", "writeBody", "readHttpResponse", "readChunk"]
    _hx_statics = ["PROXY", "requestUrl"]
    _hx_interfaces = []
    _hx_super = haxe_http_HttpBase


    def __init__(self,url):
        self.file = None
        self.chunk_buf = None
        self.chunk_size = None
        self.responseHeaders = None
        self.noShutdown = None
        self.cnxTimeout = 10
        super().__init__(url)

    def request(self,post = None):
        _gthis = self
        output = haxe_io_BytesOutput()
        old = self.onError
        err = False
        def _hx_local_0(e):
            nonlocal err
            _gthis.responseBytes = output.getBytes()
            err = True
            _gthis.onError = old
            _gthis.onError(e)
        self.onError = _hx_local_0
        post = ((post or ((self.postBytes is not None))) or ((self.postData is not None)))
        self.customRequest(post,output)
        if (not err):
            self.success(output.getBytes())

    def customRequest(self,post,api,sock = None,method = None):
        self.responseAsString = None
        self.responseBytes = None
        url_regexp = EReg("^(https?://)?([a-zA-Z\\.0-9_-]+)(:[0-9]+)?(.*)$","")
        url_regexp.matchObj = python_lib_Re.search(url_regexp.pattern,self.url)
        if (url_regexp.matchObj is None):
            self.onError("Invalid URL")
            return
        secure = (url_regexp.matchObj.group(1) == "https://")
        if (sock is None):
            if secure:
                sock = python_net_SslSocket()
            else:
                sock = sys_net_Socket()
            sock.setTimeout(self.cnxTimeout)
        host = url_regexp.matchObj.group(2)
        portString = url_regexp.matchObj.group(3)
        request = url_regexp.matchObj.group(4)
        if ((("" if ((0 >= len(request))) else request[0])) != "/"):
            request = ("/" + ("null" if request is None else request))
        port = ((443 if secure else 80) if (((portString is None) or ((portString == "")))) else Std.parseInt(HxString.substr(portString,1,(len(portString) - 1))))
        multipart = (self.file is not None)
        boundary = None
        uri = None
        if multipart:
            post = True
            boundary = (((Std.string(int((python_lib_Random.random() * 1000))) + Std.string(int((python_lib_Random.random() * 1000)))) + Std.string(int((python_lib_Random.random() * 1000)))) + Std.string(int((python_lib_Random.random() * 1000))))
            while (len(boundary) < 38):
                boundary = ("-" + ("null" if boundary is None else boundary))
            b_b = python_lib_io_StringIO()
            _g = 0
            _g1 = self.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                b_b.write("--")
                b_b.write(Std.string(boundary))
                b_b.write("\r\n")
                b_b.write("Content-Disposition: form-data; name=\"")
                b_b.write(Std.string(p.name))
                b_b.write("\"")
                b_b.write("\r\n")
                b_b.write("\r\n")
                b_b.write(Std.string(p.value))
                b_b.write("\r\n")
            b_b.write("--")
            b_b.write(Std.string(boundary))
            b_b.write("\r\n")
            b_b.write("Content-Disposition: form-data; name=\"")
            b_b.write(Std.string(self.file.param))
            b_b.write("\"; filename=\"")
            b_b.write(Std.string(self.file.filename))
            b_b.write("\"")
            b_b.write("\r\n")
            b_b.write(Std.string(((("Content-Type: " + HxOverrides.stringOrNull(self.file.mimeType)) + "\r\n") + "\r\n")))
            uri = b_b.getvalue()
        else:
            _g = 0
            _g1 = self.params
            while (_g < len(_g1)):
                p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                if (uri is None):
                    uri = ""
                else:
                    uri = (("null" if uri is None else uri) + "&")
                uri = (("null" if uri is None else uri) + HxOverrides.stringOrNull((((HxOverrides.stringOrNull(python_lib_urllib_Parse.quote(p.name,"")) + "=") + HxOverrides.stringOrNull(python_lib_urllib_Parse.quote(("" + HxOverrides.stringOrNull(p.value)),""))))))
        b = haxe_io_BytesOutput()
        if (method is not None):
            b.writeString(method)
            b.writeString(" ")
        elif post:
            b.writeString("POST ")
        else:
            b.writeString("GET ")
        if (sys_Http.PROXY is not None):
            b.writeString("http://")
            b.writeString(host)
            if (port != 80):
                b.writeString(":")
                b.writeString(("" + Std.string(port)))
        b.writeString(request)
        if ((not post) and ((uri is not None))):
            if (HxString.indexOfImpl(request,"?",0) >= 0):
                b.writeString("&")
            else:
                b.writeString("?")
            b.writeString(uri)
        b.writeString(((" HTTP/1.1\r\nHost: " + ("null" if host is None else host)) + "\r\n"))
        if (self.postData is not None):
            self.postBytes = haxe_io_Bytes.ofString(self.postData)
            self.postData = None
        if (self.postBytes is not None):
            b.writeString((("Content-Length: " + Std.string(self.postBytes.length)) + "\r\n"))
        elif (post and ((uri is not None))):
            def _hx_local_4(h):
                return (h.name == "Content-Type")
            if (multipart or (not Lambda.exists(self.headers,_hx_local_4))):
                b.writeString("Content-Type: ")
                if multipart:
                    b.writeString("multipart/form-data")
                    b.writeString("; boundary=")
                    b.writeString(boundary)
                else:
                    b.writeString("application/x-www-form-urlencoded")
                b.writeString("\r\n")
            if multipart:
                b.writeString((("Content-Length: " + Std.string(((((len(uri) + self.file.size) + len(boundary)) + 6)))) + "\r\n"))
            else:
                b.writeString((("Content-Length: " + Std.string(len(uri))) + "\r\n"))
        b.writeString("Connection: close\r\n")
        _g = 0
        _g1 = self.headers
        while (_g < len(_g1)):
            h = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            b.writeString(h.name)
            b.writeString(": ")
            b.writeString(h.value)
            b.writeString("\r\n")
        b.writeString("\r\n")
        if (self.postBytes is not None):
            b.writeFullBytes(self.postBytes,0,self.postBytes.length)
        elif (post and ((uri is not None))):
            b.writeString(uri)
        try:
            if (sys_Http.PROXY is not None):
                sock.connect(sys_net_Host(sys_Http.PROXY.host),sys_Http.PROXY.port)
            else:
                sock.connect(sys_net_Host(host),port)
            if multipart:
                self.writeBody(b,self.file.io,self.file.size,boundary,sock)
            else:
                self.writeBody(b,None,0,None,sock)
            self.readHttpResponse(api,sock)
            sock.close()
        except BaseException as _g:
            None
            e = haxe_Exception.caught(_g).unwrap()
            try:
                sock.close()
            except BaseException as _g:
                pass
            self.onError(Std.string(e))

    def writeBody(self,body,fileInput,fileSize,boundary,sock):
        if (body is not None):
            _hx_bytes = body.getBytes()
            sock.output.writeFullBytes(_hx_bytes,0,_hx_bytes.length)
        if (boundary is not None):
            bufsize = 4096
            buf = haxe_io_Bytes.alloc(bufsize)
            while (fileSize > 0):
                size = (bufsize if ((fileSize > bufsize)) else fileSize)
                _hx_len = 0
                try:
                    _hx_len = fileInput.readBytes(buf,0,size)
                except BaseException as _g:
                    None
                    if Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof):
                        break
                    else:
                        raise _g
                sock.output.writeFullBytes(buf,0,_hx_len)
                fileSize = (fileSize - _hx_len)
            sock.output.writeString("\r\n")
            sock.output.writeString("--")
            sock.output.writeString(boundary)
            sock.output.writeString("--")

    def readHttpResponse(self,api,sock):
        b = haxe_io_BytesBuffer()
        k = 4
        s = haxe_io_Bytes.alloc(4)
        sock.setTimeout(self.cnxTimeout)
        while True:
            p = sock.input.readBytes(s,0,k)
            while (p != k):
                p = (p + sock.input.readBytes(s,p,(k - p)))
            if ((k < 0) or ((k > s.length))):
                raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
            b.b.extend(s.b[0:k])
            k1 = k
            if (k1 == 1):
                c = s.b[0]
                if (c == 10):
                    break
                if (c == 13):
                    k = 3
                else:
                    k = 4
            elif (k1 == 2):
                c1 = s.b[1]
                if (c1 == 10):
                    if (s.b[0] == 13):
                        break
                    k = 4
                elif (c1 == 13):
                    k = 3
                else:
                    k = 4
            elif (k1 == 3):
                c2 = s.b[2]
                if (c2 == 10):
                    if (s.b[1] != 13):
                        k = 4
                    elif (s.b[0] != 10):
                        k = 2
                    else:
                        break
                elif (c2 == 13):
                    if ((s.b[1] != 10) or ((s.b[0] != 13))):
                        k = 1
                    else:
                        k = 3
                else:
                    k = 4
            elif (k1 == 4):
                c3 = s.b[3]
                if (c3 == 10):
                    if (s.b[2] != 13):
                        continue
                    elif ((s.b[1] != 10) or ((s.b[0] != 13))):
                        k = 2
                    else:
                        break
                elif (c3 == 13):
                    if ((s.b[2] != 10) or ((s.b[1] != 13))):
                        k = 3
                    else:
                        k = 1
            else:
                pass
        _this = b.getBytes().toString()
        headers = _this.split("\r\n")
        response = (None if ((len(headers) == 0)) else headers.pop(0))
        rp = response.split(" ")
        status = Std.parseInt((rp[1] if 1 < len(rp) else None))
        if ((status == 0) or ((status is None))):
            raise haxe_Exception.thrown("Response status error")
        if (len(headers) != 0):
            headers.pop()
        if (len(headers) != 0):
            headers.pop()
        self.responseHeaders = haxe_ds_StringMap()
        size = None
        chunked = False
        _g = 0
        while (_g < len(headers)):
            hline = (headers[_g] if _g >= 0 and _g < len(headers) else None)
            _g = (_g + 1)
            a = hline.split(": ")
            hname = (None if ((len(a) == 0)) else a.pop(0))
            hval = ((a[0] if 0 < len(a) else None) if ((len(a) == 1)) else ": ".join([python_Boot.toString1(x1,'') for x1 in a]))
            hval = StringTools.ltrim(StringTools.rtrim(hval))
            self.responseHeaders.h[hname] = hval
            _g1 = hname.lower()
            _hx_local_2 = len(_g1)
            if (_hx_local_2 == 17):
                if (_g1 == "transfer-encoding"):
                    chunked = (hval.lower() == "chunked")
            elif (_hx_local_2 == 14):
                if (_g1 == "content-length"):
                    size = Std.parseInt(hval)
            else:
                pass
        self.onStatus(status)
        chunk_re = EReg("^([0-9A-Fa-f]+)[ ]*\r\n","m")
        self.chunk_size = None
        self.chunk_buf = None
        bufsize = 1024
        buf = haxe_io_Bytes.alloc(bufsize)
        if chunked:
            try:
                while True:
                    _hx_len = sock.input.readBytes(buf,0,bufsize)
                    if (not self.readChunk(chunk_re,api,buf,_hx_len)):
                        break
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof):
                    raise haxe_Exception.thrown("Transfer aborted")
                else:
                    raise _g
        elif (size is None):
            if (not self.noShutdown):
                sock.shutdown(False,True)
            try:
                while True:
                    _hx_len = sock.input.readBytes(buf,0,bufsize)
                    if (_hx_len == 0):
                        break
                    api.writeBytes(buf,0,_hx_len)
            except BaseException as _g:
                None
                if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                    raise _g
        else:
            api.prepare(size)
            try:
                while (size > 0):
                    _hx_len = sock.input.readBytes(buf,0,(bufsize if ((size > bufsize)) else size))
                    api.writeBytes(buf,0,_hx_len)
                    size = (size - _hx_len)
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof):
                    raise haxe_Exception.thrown("Transfer aborted")
                else:
                    raise _g
        if (chunked and (((self.chunk_size is not None) or ((self.chunk_buf is not None))))):
            raise haxe_Exception.thrown("Invalid chunk")
        if ((status < 200) or ((status >= 400))):
            raise haxe_Exception.thrown(("Http Error #" + Std.string(status)))
        api.close()

    def readChunk(self,chunk_re,api,buf,_hx_len):
        if (self.chunk_size is None):
            if (self.chunk_buf is not None):
                b = haxe_io_BytesBuffer()
                b.b.extend(self.chunk_buf.b)
                if ((_hx_len < 0) or ((_hx_len > buf.length))):
                    raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
                b.b.extend(buf.b[0:_hx_len])
                buf = b.getBytes()
                _hx_len = (_hx_len + self.chunk_buf.length)
                self.chunk_buf = None
            s = buf.toString()
            chunk_re.matchObj = python_lib_Re.search(chunk_re.pattern,s)
            if (chunk_re.matchObj is not None):
                p_pos = chunk_re.matchObj.start()
                p_len = (chunk_re.matchObj.end() - chunk_re.matchObj.start())
                if (p_len <= _hx_len):
                    cstr = chunk_re.matchObj.group(1)
                    self.chunk_size = Std.parseInt(("0x" + ("null" if cstr is None else cstr)))
                    if (self.chunk_size == 0):
                        self.chunk_size = None
                        self.chunk_buf = None
                        return False
                    _hx_len = (_hx_len - p_len)
                    return self.readChunk(chunk_re,api,buf.sub(p_len,_hx_len),_hx_len)
            if (_hx_len > 10):
                self.onError("Invalid chunk")
                return False
            self.chunk_buf = buf.sub(0,_hx_len)
            return True
        if (self.chunk_size > _hx_len):
            _hx_local_2 = self
            _hx_local_3 = _hx_local_2.chunk_size
            _hx_local_2.chunk_size = (_hx_local_3 - _hx_len)
            _hx_local_2.chunk_size
            api.writeBytes(buf,0,_hx_len)
            return True
        end = (self.chunk_size + 2)
        if (_hx_len >= end):
            if (self.chunk_size > 0):
                api.writeBytes(buf,0,self.chunk_size)
            _hx_len = (_hx_len - end)
            self.chunk_size = None
            if (_hx_len == 0):
                return True
            return self.readChunk(chunk_re,api,buf.sub(end,_hx_len),_hx_len)
        if (self.chunk_size > 0):
            api.writeBytes(buf,0,self.chunk_size)
        _hx_local_5 = self
        _hx_local_6 = _hx_local_5.chunk_size
        _hx_local_5.chunk_size = (_hx_local_6 - _hx_len)
        _hx_local_5.chunk_size
        return True

    @staticmethod
    def requestUrl(url):
        h = sys_Http(url)
        r = None
        def _hx_local_0(d):
            nonlocal r
            r = d
        h.onData = _hx_local_0
        def _hx_local_1(e):
            raise haxe_Exception.thrown(e)
        h.onError = _hx_local_1
        h.request(False)
        return r



class sys_net_Host:
    _hx_class_name = "sys.net.Host"
    __slots__ = ("host", "name")
    _hx_fields = ["host", "name"]
    _hx_methods = ["toString"]

    def __init__(self,name):
        self.host = name
        self.name = name

    def toString(self):
        return self.name



class sys_net__Socket_SocketInput(haxe_io_Input):
    _hx_class_name = "sys.net._Socket.SocketInput"
    __slots__ = ("_hx___s",)
    _hx_fields = ["__s"]
    _hx_methods = ["readByte", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,s):
        self._hx___s = s

    def readByte(self):
        r = None
        try:
            r = self._hx___s.recv(1,0)
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g
        if (len(r) == 0):
            raise haxe_Exception.thrown(haxe_io_Eof())
        return r[0]

    def readBytes(self,buf,pos,_hx_len):
        r = None
        data = buf.b
        try:
            r = self._hx___s.recv(_hx_len,0)
            _g = pos
            _g1 = (pos + len(r))
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                data.__setitem__(i,r[(i - pos)])
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g
        if (len(r) == 0):
            raise haxe_Exception.thrown(haxe_io_Eof())
        return len(r)



class sys_net__Socket_SocketOutput(haxe_io_Output):
    _hx_class_name = "sys.net._Socket.SocketOutput"
    __slots__ = ("_hx___s",)
    _hx_fields = ["__s"]
    _hx_methods = ["writeByte", "writeBytes", "close"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,s):
        self._hx___s = s

    def writeByte(self,c):
        try:
            self._hx___s.send(bytes([c]),0)
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g

    def writeBytes(self,buf,pos,_hx_len):
        try:
            data = buf.b
            payload = data[pos:pos+_hx_len]
            r = self._hx___s.send(payload,0)
            return r
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),BlockingIOError):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            else:
                raise _g

    def close(self):
        super().close()
        if (self._hx___s is not None):
            self._hx___s.close()



class sys_thread_EventLoop:
    _hx_class_name = "sys.thread.EventLoop"
    __slots__ = ("mutex", "oneTimeEvents", "oneTimeEventsIdx", "waitLock", "promisedEventsCount", "regularEvents")
    _hx_fields = ["mutex", "oneTimeEvents", "oneTimeEventsIdx", "waitLock", "promisedEventsCount", "regularEvents"]
    _hx_methods = ["loop"]

    def __init__(self):
        self.regularEvents = None
        self.promisedEventsCount = 0
        self.waitLock = sys_thread_Lock()
        self.oneTimeEventsIdx = 0
        self.oneTimeEvents = list()
        self.mutex = sys_thread_Mutex()

    def loop(self):
        events = []
        while True:
            now = python_lib_Time.time()
            eventsToRun = events
            eventsToRunIdx = 0
            nextEventAt = -1
            self.mutex.lock.acquire(True)
            while self.waitLock.semaphore.acquire(True,0.0):
                pass
            current = self.regularEvents
            while (current is not None):
                if (current.nextRunTime <= now):
                    tmp = eventsToRunIdx
                    eventsToRunIdx = (eventsToRunIdx + 1)
                    python_internal_ArrayImpl._set(eventsToRun, tmp, current.run)
                    current.nextRunTime = (current.nextRunTime + current.interval)
                    nextEventAt = -2
                elif ((nextEventAt == -1) or ((current.nextRunTime < nextEventAt))):
                    nextEventAt = current.nextRunTime
                current = current.next
            self.mutex.lock.release()
            _g = 0
            _g1 = eventsToRunIdx
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                (eventsToRun[i] if i >= 0 and i < len(eventsToRun) else None)()
                python_internal_ArrayImpl._set(eventsToRun, i, None)
            eventsToRunIdx = 0
            self.mutex.lock.acquire(True)
            _g2_current = 0
            _g2_array = self.oneTimeEvents
            while (_g2_current < len(_g2_array)):
                _g3_value = (_g2_array[_g2_current] if _g2_current >= 0 and _g2_current < len(_g2_array) else None)
                _g3_key = _g2_current
                _g2_current = (_g2_current + 1)
                i1 = _g3_key
                event = _g3_value
                if (event is None):
                    break
                else:
                    tmp1 = eventsToRunIdx
                    eventsToRunIdx = (eventsToRunIdx + 1)
                    python_internal_ArrayImpl._set(eventsToRun, tmp1, event)
                    python_internal_ArrayImpl._set(self.oneTimeEvents, i1, None)
            self.oneTimeEventsIdx = 0
            hasPromisedEvents = (self.promisedEventsCount > 0)
            self.mutex.lock.release()
            _g2 = 0
            _g3 = eventsToRunIdx
            while (_g2 < _g3):
                i2 = _g2
                _g2 = (_g2 + 1)
                (eventsToRun[i2] if i2 >= 0 and i2 < len(eventsToRun) else None)()
                python_internal_ArrayImpl._set(eventsToRun, i2, None)
            if (eventsToRunIdx > 0):
                nextEventAt = -2
            r_nextEventAt = nextEventAt
            r_anyTime = hasPromisedEvents
            _g4 = r_anyTime
            _g5 = r_nextEventAt
            _g6 = _g5
            if (_g6 == -2):
                pass
            elif (_g6 == -1):
                if _g4:
                    self.waitLock.semaphore.acquire(True,None)
                else:
                    break
            else:
                time = _g5
                timeout = (time - python_lib_Time.time())
                _this = self.waitLock
                timeout1 = (0 if (python_lib_Math.isnan(0)) else (timeout if (python_lib_Math.isnan(timeout)) else max(0,timeout)))
                _this.semaphore.acquire(True,timeout1)



class sys_thread__EventLoop_RegularEvent:
    _hx_class_name = "sys.thread._EventLoop.RegularEvent"
    __slots__ = ("nextRunTime", "interval", "run", "next")
    _hx_fields = ["nextRunTime", "interval", "run", "next"]

    def __init__(self,run,nextRunTime,interval):
        self.next = None
        self.run = run
        self.nextRunTime = nextRunTime
        self.interval = interval



class sys_thread_Lock:
    _hx_class_name = "sys.thread.Lock"
    __slots__ = ("semaphore",)
    _hx_fields = ["semaphore"]

    def __init__(self):
        self.semaphore = Lock(0)



class sys_thread_Mutex:
    _hx_class_name = "sys.thread.Mutex"
    __slots__ = ("lock",)
    _hx_fields = ["lock"]

    def __init__(self):
        self.lock = sys_thread__Mutex_NativeRLock()



class sys_thread__Thread_Thread_Impl_:
    _hx_class_name = "sys.thread._Thread.Thread_Impl_"
    __slots__ = ()
    _hx_statics = ["processEvents"]

    @staticmethod
    def processEvents():
        sys_thread__Thread_HxThread.current().events.loop()


class sys_thread__Thread_HxThread:
    _hx_class_name = "sys.thread._Thread.HxThread"
    __slots__ = ("events", "nativeThread")
    _hx_fields = ["events", "nativeThread"]
    _hx_statics = ["threads", "threadsMutex", "mainThread", "current", "create"]

    def __init__(self,t):
        self.events = None
        self.nativeThread = t
    threads = None
    threadsMutex = None
    mainThread = None

    @staticmethod
    def current():
        sys_thread__Thread_HxThread.threadsMutex.lock.acquire(True)
        ct = threading.current_thread()
        if (ct == threading.main_thread()):
            sys_thread__Thread_HxThread.threadsMutex.lock.release()
            return sys_thread__Thread_HxThread.mainThread
        if (not (ct in sys_thread__Thread_HxThread.threads.h)):
            sys_thread__Thread_HxThread.threads.set(ct,sys_thread__Thread_HxThread(ct))
        t = sys_thread__Thread_HxThread.threads.h.get(ct,None)
        sys_thread__Thread_HxThread.threadsMutex.lock.release()
        return t

    @staticmethod
    def create(callb,withEventLoop):
        nt = None
        t = None
        def _hx_local_0():
            try:
                callb()
                if withEventLoop:
                    t.events.loop()
            except BaseException as _g:
                e = haxe_Exception.caught(_g)
                sys_thread__Thread_HxThread.threadsMutex.lock.acquire(True)
                sys_thread__Thread_HxThread.threads.remove(nt)
                sys_thread__Thread_HxThread.threadsMutex.lock.release()
                raise haxe_Exception.thrown(e)
            sys_thread__Thread_HxThread.threadsMutex.lock.acquire(True)
            sys_thread__Thread_HxThread.threads.remove(nt)
            sys_thread__Thread_HxThread.threadsMutex.lock.release()
        wrappedCallB = _hx_local_0
        nt = Thread(None,wrappedCallB)
        t = sys_thread__Thread_HxThread(nt)
        if withEventLoop:
            t.events = sys_thread_EventLoop()
        sys_thread__Thread_HxThread.threadsMutex.lock.acquire(True)
        sys_thread__Thread_HxThread.threads.set(nt,t)
        sys_thread__Thread_HxThread.threadsMutex.lock.release()
        nt.start()
        return t


Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi
sys_thread__Thread_HxThread.threads = haxe_ds_ObjectMap()
sys_thread__Thread_HxThread.threadsMutex = sys_thread_Mutex()
sys_thread__Thread_HxThread.mainThread = sys_thread__Thread_HxThread(threading.current_thread())
sys_thread__Thread_HxThread.mainThread.events = sys_thread_EventLoop()

python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")
sys_Http.PROXY = None

Main.main()
sys_thread__Thread_Thread_Impl_.processEvents()
