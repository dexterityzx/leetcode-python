def switchChars(str):
	lib = ['a','e','i','o','u']
	for i in xrange(len(str)/2):
		if str[i] in lib and str[-1-i] in lib:
			str = swap(str,i,-1-i)
	return str

def swap(str,idx1, idx2):
	_str = list(str)
	tmp = _str[idx1]
	_str[idx1] = _str[idx2]
	_str[idx2] = tmp
	return ''.join(_str)

testStr = 'aupuoie'
print switchChars(testStr)