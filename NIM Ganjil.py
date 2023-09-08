#Soal nomor 1
#Konversi suhu dalam derajat Celsius menjadi derajat Fahrenheit
#Rumus Celsius to Fahrenheit 9/5*c+32

print('Konversi suhu Celsius ke Fahrenheit')
celsius=int(input('masukan suhu celsius :'))
r1 = 9/5
r2 = 32
rumuscelsiustofahrenheit = r1*celsius
rumus2 = rumuscelsiustofahrenheit + r2
print('Maka suhu Fahrenheitnya adalah :', rumus2, '*f')

#Soal nomor 2
#Koversi suhu dalam derajat Fahrenheit menjadi derajat Celsius
#Rumus Fahrenheit to Celsius 5/9*(f-32)

print('Konversi suhu Fahrenheit ke Celsius')
fahrenheit=int(input('masukan suhu fahrenheit :'))
r1=5/9
r2=32
rumus2 = fahrenheit-r2
rumusfahrenheittocelsius = r1*rumus2
print('Maka suhu Celsiusnya adalah :', rumusfahrenheittocelsius, '*c')

#Soal nomor 3
#Konversi suhu dalam derajat Kelvin ke Celsius
#Rumus Kelvin ke Celsius k-273

print('Konversi suhu Kelvin ke Celsius')
kelvin=int(input('masukan suhu kelvin :'))
rumuskelvintocelsius = kelvin-273
print('Maka suhu Celsiusnya adalah :', rumuskelvintocelsius, '*c')
