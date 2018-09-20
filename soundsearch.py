# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:15:03 2018
@author: david
Perform fast fourier transform on saved sound file or incoming stream
"""

import matplotlib.pyplot as plt
from scipy.io import wavefile as wav
from scipy.fftpack import fft
import numpy as np
