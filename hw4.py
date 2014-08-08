#!/usr/bin/env python

from cryptutil import *

ct = '20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d'
pt1 = 'Pay Bob 100$' 
pt2 = 'Pay Bob 500$' 


cta = hex2array(ct)
pta = np.pad(byte2array(pt1), (0,4), mode='constant')
ptb = np.pad(byte2array(pt2), (0,4), mode='constant')

cta[:16] = np.bitwise_xor(np.bitwise_xor(cta[:16], pta), ptb)
print array2hex(cta)


