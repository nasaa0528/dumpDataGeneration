# dumpDateGeneration
## About - English 
The code is used for generating dump data for testing VBA codes in Excel. Generated dump file is in Mongolian (with cyrilic alphabets). Main goal of dump data is getting .xlsx file. However, above code will give you only csv file, then we need to import csv file from Excel application with correct encoding (which is UTF-8). 

Steps to run codes: 
1. Run nameGenerator.py - it generates names.pk binary file that has list of random generated names from Mongolian most common names.
2. Run phoneNumberGenerator.py - it generates phones.pk file that has phone numbers from Mongolian Cell phone prefix like 99, 96 etc. 
3. Then finally run dataGenerator.py - This file reads previous two pk files and then generates random datas for date, registration number, position etc. Final 'dump_data.csv' file has 11000000 x 12 sized data. 
Example: 
```
$: python3 nameGenerator.py && python3 phoneNumberGenerator.py && python3 dataGenerator.py
```


## Програмын тухай - Монгол
Энэхүү кодыг ажиллуулснаар бид санамсаргүй байдлаар үүсгэсэн бодит бус хүмүүсийн мэдээллийг үүсгэх юм. Улмаар үүсгэсэн мэдээллээ Excel програмын VBA кодыг туршиж үзэхэд ашиглана. Хэдийгээр бидэнд .xlsx өргөтгөлтэй файл хэрэгтэй боловч, энэхүү кодын үр дүнд бид CSV файлтай болно. Улмаар CSV файлаа Excel дотроос import хийж оруулснаар **(UTF-8 encoding ашиглан)** бид өөрсдийн хүссэн өгөгдлийг гаргаж авах болно. 

Програмыг ажиллуулах алхмууд: 
1. nameGenerator.py - кодыг ажиллуулах. Энэ код нь names.pk гэсэн бинари файл үүсгэх ба энэхүү файлд түгээмэл Монгол нэрсийг ашиглан, санамсаргүйгээр үүсгэсэн нэрс агуулагдана. 
2. phoneNumberGenerator.py - кодыг ажиллуулах. Энэ код нь phones.pk файлыг үүсгэх ба энэ файлд Монгол улсад ашиглагддаг боломжит бүх төрлийн утасны дугаар агуулагдана. Жишээлбэл 99, 95 гэх мэт эхлэлтэй утасны дугаарууд байна гэсэн үг. 
3. Эцэст нь dataGenerator.py - кодыг ажиллуулснаар, энэхүү файл нь өмнө нь үүсгэгдсэн 2 файлыг ашиглан, мөн үүн дээр нэмэлт үүсгэх шаардлагатай мэдээллүүдийг зохиомлоор үүсгэж улмаар танд 'dump_data.csv' гэсэн нэр бүхий 12 багана 11 сая мөр бүхий файлыг өгнө. Энэхүү CSV 	файлыг та Excel дотроос дуудаж оруулж улмаар файлаа .xlsx өргөтгөлтэй хадгалах боломжтой байна. 

Програмыг ажиллуулах жишээ: 
```
$: python3 nameGenerator.py && python3 phoneNumberGenerator.py && python3 dataGenerator.py
```
