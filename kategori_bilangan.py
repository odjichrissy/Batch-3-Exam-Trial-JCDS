'''
========================================================================================
Kategori Bilangan
========================================================================================
'''

angka = input('Masukkan angka: ')

bilangan = [
    'Bulat', 'Negativ', 'Cacah', 'Nol', 
    'Asli', 'Ganjil', 'Genap', 'Prima', 
    'Komposit'
]

def bulat(x):
    kategori.append(bilangan[0])


def negativ(x):
    kategori.append(bilangan[1])


def cacah(x):
    kategori.append(bilangan[2])
   

def nol(x):
    kategori.append(bilangan[3])
 

def asli(x):
    kategori.append(bilangan[4])


def ganjil(x):
    kategori.append(bilangan[5])


def genap(x):
    kategori.append(bilangan[6])
 

def prima(x):
    kategori.append(bilangan[7])

def komposit(x):
    kategori.append(bilangan[8])


x = int(angka)
kategori = []


if x >= 0:
    bulat(x)

if x < 0:
    negativ(x)

if x > 0:
    cacah(x)

if x == 0:
    nol(x)

if x > 0:
    asli(x)

if x % 2 == 1:
    ganjil(x)

if x % 2 == 0:
    genap(x)

if x > 1:
        for i in range(2, x//2):
            if x % i == 0:
                komposit(x)
                break
            else:
                prima(x)

print('Angka yang anda masukkan termasuk bilangan:', kategori)