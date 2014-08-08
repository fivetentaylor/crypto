#!/usr/bin/env python

import ipdb
import numpy as np
from cryptutil import *
import urllib2
import sys

ct='f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
def query(q, TARGET='http://crypto-class.appspot.com/po?er='):
	target = TARGET + urllib2.quote(q)    # Create query URL
	#print target
	req = urllib2.Request(target)         # Send HTTP request to server
	try:
		f = urllib2.urlopen(req)          # Wait for response
	except urllib2.HTTPError, e:          
		if e.code == 404:
			return True # good padding
		return False # bad padding

def padAttack(BS=16):
	a = hex2array(ct)
	pt = np.zeros(len(a), dtype=np.uint8)
	pad = np.zeros(len(a), dtype=np.uint8)
	for i in xrange(len(a) / BS, 1, -1):
		pad[:] = 0
		block = i*BS
		mask = pad[:block].copy()
		mask[:-BS] = 0xff
		for j in xrange(1,BS+1):
			pad[BS*(i-1)-j:BS*(i-1)] = j
			for k in xrange(256):
				pt[((i-1)*BS) - j] = k
				#ipdb.set_trace()
				if query(array2hex(a[:block] ^ (pt[:block] & mask) ^ pad[:block])):
					break
			print "original: \n", a
			print "mask: \n", mask
			print "plain text: \n", pt[:block] & mask
			print "padding: \n", pad[:block]
			print "query: \n", a[:block] ^ (pt[:block] & mask) ^ pad[:block]
			print array2ascii(pt)
	return array2ascii(pt)


if __name__ == "__main__":
	print padAttack()





