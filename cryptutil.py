import numpy as np
import itertools as it

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return it.izip_longest(fillvalue=fillvalue, *args)

def hex2array(hex_string):
	return np.array([int('%c%c' % x, 16) for x in grouper(hex_string, 2, 0)])

def array2hex(byte_array):
	return ''.join(['%02x' % x for x in byte_array])

def array2ascii(byte_array):
	return ''.join(['%c' % x for x in byte_array])
	
def xor2hex(hex1, hex2):
	if len(hex1) > len(hex2):
		hex1,hex2 = hex2,hex1

	a1 = hex2array(hex1)
	a2 = hex2array(hex2)

	return array2ascii(np.bitwise_xor(a1, a2[:len(a1)]))

def most_common(chars, predicate=lambda x: str(x).isalpha()):
	counts = [(x,sum(1 for _ in y)) for x,y in it.groupby(sorted(chars))]
	for v in sorted(counts, key=lambda x: x[1], reverse=True):
		p = str(v[0])
		if p.isalpha():
			return p


