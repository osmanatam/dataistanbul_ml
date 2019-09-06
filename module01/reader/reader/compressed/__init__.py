# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:07:00 2019

@author: DIPRBAYINDIR
"""
 
from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener','gzip_opener']