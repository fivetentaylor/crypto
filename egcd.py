#!/usr/bin/env python

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def mygcd(a, b):
	if a < b:
		a,b = b,a
	while b > 0:
		q, r = a // b, a % b
		print "%4d / %-4d = %3d * %-3d + %-3d" % (a,b,q,b,r)
		a = b
		b = r
