'''
Final dump file generator fo Excel VBA and Python tutorial
@Author: Nasantogtokh Amarsaikhan 
@Date: 8/Jul/2020

Credits for Registration number generation part: 
	https://medium.com/beyond-data-science/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B8%D0%B9%D0%BD-%D0%B4%D1%83%D0%B3%D0%B0%D0%B0%D1%80-%D1%82%D0%B0%D0%BD%D1%8B-%D1%82%D1%83%D1%85%D0%B0%D0%B9-%D1%8E%D1%83-%D3%A9%D0%B3%D2%AF%D2%AF%D0%BB%D0%BD%D1%8D-%D0%B2%D1%8D-r-python-sql-%D0%BA%D0%BE%D0%B4-d471bbd036aa by Nyamkhuu Demberelsuren 
	I have tried to make generated registration numbers as consistent as registration number generation.
	Please remembere, I didn't check uniqueness of Registration number, although it is most important part of Registration generation, it was too time consuming to check for 11M dataset. 
'''
import csv, random
import pickle as pl 
import time
import datetime
import pandas as pd 

# 65 - 18 years old dattimes generation
def birthdateGenerator(): 
	start_date = datetime.datetime.now() - datetime.timedelta(days=65*365)
	end_date = datetime.datetime.now() - datetime.timedelta(days=18*365)

	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)
	return random_date.date()

def location2Date(province):
	location2char = {
	u'Архангай': u'А',
	u'Баян-Өлгий': u'Б',
	u'Баянхонгор': u'В',
	u'Булган': u'Г',
	u'Говь-Алтай': u'Д',
	u'Дорноговь': u'Е',
	u'Дорнод': u'Ж',
	u'Дундговь': u'З',
	u'Завхан': u'И',
	u'Өвөрхангай': u'Й',
	u'Өмнөговь': u'К',
	u'Сүхбаатар': u'Л',
	u'Сэлэнгэ': u'М',
	u'Төв': u'Н',
	u'Увс': u'О',
	u'Ховд': u'П',
	u'Хөвсгөл': u'Р',
	u'Хэнтий': u'С',
	u'Дархан-Уул': u'Т',
	u'Орхон': u'Ф',
	u'Говьсүмбэр': u'Х',
	u'Улаанбаатар':[u'У', u'Ч'],
	}
	if province != u'Улаанбаатар':
		return location2char[province] + random.choice(regPre)
	else: 
		return random.choice(location2char[province]) + random.choice(regPre)


provinces = [
	u'Баян-Өлгий',
	u'Баянхонгор',
	u'Булган',
	u'Говь-Алтай',
	u'Дорноговь',
	u'Дорнод',
	u'Дундговь',
	u'Завхан',
	u'Өвөрхангай',
	u'Өмнөговь',
	u'Сүхбаатар',
	u'Сэлэнгэ',
	u'Төв',
	u'Увс',
	u'Ховд',
	u'Хөвсгөл',
	u'Хэнтий',
	u'Дархан-Уул',
	u'Орхон',
	u'Говьсүмбэр',
	u'Улаанбаатар', 
	]
gender_list = [u'эрэгтэй', u'эмэгтэй']
degree_list = [u'Бүрэн дунд', u'Тусгай дунд', u'Дээд', u'Магистр', u'Доктор']
company_list = [u'MCS', u'Хаанбанк', u'Голомтбанк', u'Монголшуудан', u'Сүү ХК', u'ШУТИС', u'МУИС', u'ЦЕГ', u'Гаалийн Ерөнхий газар', u'Татварын Ерөнхий газар', u'Улсын онцгой комисс', u'Хил Хамгаалах Ерөнхий газар', u'Зэвсэгт Хүчний Жанжин Штаб', u'АПУ', u'Монос', u'Магнай Трэйд']
position_list = [u'Газрын дарга', u'Мэргэжилтэн', u'Ахлах мэргэжилтэн', u'Цагдаа', u'Менежер', u'Ахлах менежер', u'Эрсдэлийн шинжээч', u'Прорам зохиогч', u'Аюулгүй байдлын инженер', u'Захирал', u'Цэвэрлэгч', u'Тогооч', u'Жолооч'] 
regPre = u'АБВГДЕЁЖЗИЙКЛМНОӨПРСТУҮФХЦЧШЩЫЭЮЯ'

with open('names.pk', 'rb') as pkNameFO, open('phones.pk', 'rb') as pkPhoneFO: 
	fullNames = pl.load(pkNameFO) 
	phoneNums = pl.load(pkPhoneFO) 

numPeople = len(fullNames) 

genders = [] 
birthDates = [] 
birthPlaces = [] 
rds = [] 
degrees = [] 
companies = [] 
positions = [] 
experiences = [] 
salaries = [] 
bonuses = [] 
def rdGenerator(birthplace, birthdate, gender): 
	rd = location2Date(birthplace)
	rd += str(birthdate.year)[-2:] 
	if birthdate.year >= 2000: 
		rd += str(birthdate.month + 20)
	else: 
		rd += "{:02d}".format(birthdate.month)
	rd += "{:02d}".format(birthdate.day)
	if gender == 'эрэгтэй': 
		rd += random.choice('13579') 
	else: 
		rd += random.choice('02468') 
	rd += str(random.randint(0,9))
	return rd 
# name, gender, birthDate, birthPlace, rd, phoneNum, degree, comp, position, experience, salary, bonus 
for i in range(numPeople): 
	gender = random.choice(gender_list) 
	genders.append(gender) 
	birthdate = birthdateGenerator()
	birthDates.append(birthdate) 
	birthplace = random.choice(provinces)
	birthPlaces.append(birthplace) 
	rd = rdGenerator(birthplace, birthdate, gender) 
	rds.append(rd) 
	degree = random.choice(degree_list) 
	degrees.append(degree) 
	company = random.choice(company_list) 
	companies.append(company) 
	position = random.choice(position_list) 
	positions.append(position) 
	experience = datetime.datetime.now().date().year - birthdate.year - 18 
	experiences.append(experience)
	if experience < 10: 
		salary = 1500000
	elif experience < 20: 
		salary = 2000000
	elif experience < 30: 
		salary = 2500000
	else: 
		salary = 3000000
	salaries.append(salary) 
	bonus = round(salary * 0.1) 
	bonuses.append(bonus) 

d = {
	'fullname': fullNames, 
	'gender': genders, 
	'birthdate': birthDates, 
	'birthplace': birthPlaces, 
	'rd': rds, 
	'phonenum': phoneNums, 
	'degree': degrees, 
	'company': companies, 
	'position': positions, 
	'experience': experiences, 
	'salary': salaries, 
	'bonus': bonuses,
}
df = pd.DataFrame(data = d) 
df.to_csv('dump_data.csv')
