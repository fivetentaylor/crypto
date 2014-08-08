#!/usr/bin/env python

from cryptutil import *

cipher_texts = [
	["7b50baab", "07640c3d", "ac343a22", "cea46d60"],
	["7c2822eb", "fdc48bfb", "325032a9", "c5e2364b"],
	["e86d2de2", "e1387ae9", "1792d21d", "b645c008"],
	["5f67abaf", "5210722b", "bbe033c0", "0bc9330e"]
]

for ct in cipher_texts:
	print np.bitwise_xor(hex2array(ct[0]), hex2array(ct[2]))

messages = [
	'We see immediately that one needs little information to begin to break down the process.',
	'An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.',
	'The most direct computation would be for the enemy to try all 2^r possible keys, one by one.',
	'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.'
]

for m in messages:
	print len(m)



