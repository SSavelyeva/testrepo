#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:36:36 2021

@author: sofiya
"""


import numpy as np
from math import sin
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1)
y=[sin(i) for i in x]
plt.plot(x,y)