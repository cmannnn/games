# this is alpha_counter

# function version of character counter
# import string for translation
import string

# initiate empty dictionary and list for counting 
dic = dict()
lst = list()

# main func
def alpha_count(fname):
	try:
		fname = open(inny)
	except:
		return('File not found', inny)
	
	#begin by reading in file
	for line in fname:
		line = line.lower()
		line = line.rstrip()
		words = line.translate(str.maketrans('', '', '!"#$%&()*+,-./:;<=>?@[]^_`{|}~1234567890\'\t '))
	
		# counting letters
		for word in words:
			if word not in dic:
				dic[word] = 1
			else:
				dic[word] += 1	

	for key, value in dic.items():
		lst.append((key, value))
		lst.sort()
		# return key, value

	for key, value in lst:
		print(key, '      ', value)

# input
inny = input('Enter a file name: ')			

# formatting heading	
print('LETTER\t COUNT')
print('-------\t ------')

print(alpha_count(inny))







