#!/usr/bin/env python

import ipdb

from Crypto.Cipher import AES
from Crypto import Random

from cryptutil import *

#
# key = b'Sixteen byte key'
# iv = Random.new().read(AES.block_size)
# cipher = AES.new(key, AES.MODE_CFB, iv)
# msg = iv + cipher.encrypt(b'Attack at dawn')

cbc_k1 = '140b41b22a29beb4061bda66b6747e14'
cbc_ct1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

cbc_k2 = '140b41b22a29beb4061bda66b6747e14'
cbc_ct2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'

ctr_k1 = '36f18357be4dbd77f050515c73fcf9f2'
ctr_ct1 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'

ctr_k2 = '36f18357be4dbd77f050515c73fcf9f2'
ctr_ct2 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'

def cbc_decrypt(ct, key):
	cta = hex2array(ct)
	ka = hex2array(key)
	cipher = AES.new(ka)
	iv = cta[:16]
	pt = []
	for block in grouper(cta[16:], 16):
		#ipdb.set_trace()
		ctb = np.array(block, dtype=np.uint8)
		pt.append(np.bitwise_xor(byte2array(cipher.decrypt(ctb)), iv))
		iv = np.array(block, dtype=np.uint8)
	return ''.join([array2ascii(x) for x in pt])
		
print cbc_decrypt(cbc_ct1, cbc_k1)
print cbc_decrypt(cbc_ct2, cbc_k2)

def ctr_decrypt(ct, key):
	cta = hex2array(ct)
	ka = hex2array(key)
	cipher = AES.new(ka)
	#ipdb.set_trace()
	iv,cta = cta[:16], cta[16:]
	cta = np.pad(cta, (0,16 - (len(cta)%16)), 'constant')	
	mask = np.tile(iv, len(cta) / 16).view('>u4')
	for i in xrange(len(mask[3::4])):
		mask[3+i*4] += i
	res = np.bitwise_xor(cta, byte2array(cipher.encrypt(mask.view(np.uint8))))
	return array2ascii(res)
	
print ctr_decrypt(ctr_ct1, ctr_k1)
print ctr_decrypt(ctr_ct2, ctr_k2)



