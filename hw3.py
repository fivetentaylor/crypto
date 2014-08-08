#!/usr/bin/env python

import ipdb
import os
import sys
from Crypto.Hash import SHA256
import cryptutil

def chunk(path, block=1024):
	f = open(path, 'rb')
	size = os.stat(path).st_size - 1
	start = (size / block) * block
	for index in xrange(start, -1, -block):
		#ipdb.set_trace()
		f.seek(index)
		yield f.read(block)
	f.close()
		
h0 = b''
h = None
for data in chunk(sys.argv[1]):
	#ipdb.set_trace()
	h = SHA256.new()
	h.update(data + h0)
	h0 = h.digest()

print h.hexdigest()



