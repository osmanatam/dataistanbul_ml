# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:55:22 2019

@author: DIPRBAYINDIR
"""

import reader

type(reader)

reader.__file__


import reader.reader

reader.reader.__file__


r = reader.reader.Reader( 'C:\\Users\\DIPRBAYINDIR\\jupyterLAB\\dataistanbul_python\\tutorial\\reader\\Reader.py')

r.read()

r.close()

import reader

r = reader.Reader( 'C:\\Users\\DIPRBAYINDIR\\jupyterLAB\\dataistanbul_python\\tutorial\\reader\\Reader.py')

r.read()

r.close()