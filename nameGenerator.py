'''
Generate cyrilic fullnames from 50 common names with lenght of all possible phone numbers 
'''
import pickle as pl 
import random 
phoneNums = [] 
# phones.pk is previously created possible phone numbers combinations of Mongolia 
with open('phones.pk', 'rb') as pfile: 
	phoneNums = pl.load(pfile)

# Common names from https://www.1212.mn/sonirkholtoi/GivenName/ as of 2020 July
commonNames = [
							u'Бат-Эрдэнэ', 
							u'Тэмүүлэн',
							u'Хулан', 
							u'Номин-Эрдэнэ', 
							u'Билгүүн', 
							u'Төгөлдөр', 
							u'Мөнх-Эрдэнэ', 
							u'Дөлгөөн', 
							u'Отгонбаяр', 
							u'Энхжин', 
							u'Мишээл', 
							u'Алтанцэцэг', 
							u'Болормаа', 
							u'Батбаяр', 
							u'Оюунчимэг',
							u'Нандин-Эрдэнэ',
							u'Лхагвасүрэн',
							u'Анужин',
							u'Гантулга',
							u'Энхжаргал',
							u'Мөнхбат',
							u'Хонгорзул',
							u'Энхтуяа',
							u'Эрдэнэчмэг',
							u'Хүслэн',
							u'Мөнхцэцэг',
							u'Анхбаяр', 
							u'Мөнхжаргал', 
							u'Ганзориг', 
							u'Азжаргал', 
							u'Пүрэвсүрэн', 
							u'Наранцэцэг', 
							u'Уянга', 
							u'Батцэцэг', 
							u'Амин-Эрдэнэ', 
							u'Анхбаяр', 
							u'Батжаргал', 
							u'Нарантуяа', 
							u'Алтангэрэл', 
							u'Ганболд', 
							u'Баярсайхан', 
							u'Бямбасүрэн', 
							u'Баярмаа', 
							u'Оюунцэцэг', 
							u'Мягмарсүрэн', 
							u'Баттулга', 
							u'Солонго', 
							u'Ганбаатар', 
							u'Мөнхзул', 
							u'Энэрэл', 
							]

fullnames = [] 
for i in range(len(phoneNums)): 
	first = random.choice(commonNames)
	last = random.choice(commonNames)
	while (first == last): 
		last = random.choice(commonNames)
	fullname = last + u" " + first 
	fullnames.append(fullname)
print(fullnames)
with open('names.pk', 'wb') as pfile: 
	pl.dump(fullnames, pfile)

