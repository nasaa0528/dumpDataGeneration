import pickle as pl 
'''
Generate phone number combinations and store it in 'phone.pk' file.
Then we'll use this file to create correct length of names, registrations and other purpose

@Author: Nasantogtokh Amarsaikhan 
@Date: 08/Jul/2020
'''
preps = [99,96,95,92,91,90,89,88,85,80,77]
phoneNums = []
for prep in preps: 
	for phone in range(1000000):
		phoneNums.append(str(prep) + "{:06d}".format(phone))
with open('phones.pk', 'wb') as pfile: 
	pl.dump(phoneNums, pfile)
