#!/bin/env python
# -*- coding:utf-8 -*-
# Date: 2016/4/14
# Author: shuai.li(286287737@qq.com)
import matplotlib.pyplot as plt
import numpy as np

import math

def genHamWin(frame_size):
    factor = 2 * math.pi / frame_size
    return [0.54 - 0.46 * math.cos(factor * i) for i in range(frame_size)]

if __name__ == '__main__':
    frame_size = 100
    factor = 2 * math.pi / frame_size
    x = np.arange(frame_size)
    y = genHamWin(frame_size)
    y2 = -np.cos(x * factor)
    y3 = np.sin(x * factor)

    plt.subplot(3, 1, 1)
    plt.plot(x, y)
    plt.subplot(3, 1, 2)
    plt.plot(x, y2)
    plt.subplot(3, 1, 3)
    plt.plot(x, y3)
    plt.show()
