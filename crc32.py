POLY = 0xEDB88320

def crc32(data):
	'''crc32 calculating function'''
	crc_table = [0]*256

	for i in range(256):	#l
		cell = i
		for j in range(8):
			if cell & 1:
				cell = (cell >> 1) ^ POLY
			else:
				cell >>= 1
		crc_table[i] = cell

	crc = 0xffffffff
	for c in data:
		crc = (crc >> 8) ^ crc_table[(crc ^ ord(c)) & 0xff]
	return hex(crc ^ 0xfffffffF)


#print(crc32("asdfasdfasdfasdfasdfasdfasdfsf"))