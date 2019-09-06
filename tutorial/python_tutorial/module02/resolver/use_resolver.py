# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:01:59 2019

@author: DIPRBAYINDIR
"""

from resolver import Resolver

resolve = Resolver()

resolve('google.com')

resolve.__call__('google.com')

resolve._cache

resolve('pluralsight.com')

resolve._cache


from timeit import timeit

timeit(setup = "from __main__ import resolve",stmt ="resolve('python.org')", number = 1 )


resolve1 = Resolver()

resolve1.has_host("pluralsight.com")

resolve1("pluralsight.com")


resolve1.has_host("pluralsight.com")

resolve1.clear()

resolve1.has_host("pluralsight.com")
