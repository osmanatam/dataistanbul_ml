# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:08:27 2019

@author: DIPRBAYINDIR
"""

import gzip
import sys

opener =gzip.open


if __name__ == '__main__':
    f = gzip.open(sys.argv[1],mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()