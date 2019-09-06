# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:52:47 2019

@author: DIPRBAYINDIR
"""

import socket

def resolve(host):
    return socket.gethostbyname(host)

resolve


resolve('google.com')