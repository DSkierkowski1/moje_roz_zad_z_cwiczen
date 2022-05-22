# import math
# import sys
# napisz skrypt wyświetlający poszczególne wyrażenia
# import math
# a=math.e**10
# print(a)
# from math import *
# a = exp(10)
# print(a)
#
# sinus = sin(8)**2
# logarytm = log(5 + sinus) ** (1/6)
# # b = pow(logarytm, 1/6)
# print(logarytm)
# from math import *
# c = floor(3.55)
# print(c)
# d = ceil(4.8)
#zad 5
# print(d)
# a = "daniel"
# b = "skierkowski"
# print(a.capitalize() + " " + b.capitalize())
#zad 6
# a="la la la la la la la la "
# b=a.count("la")
# print(b)
#zad 7
# z= "tekst do sprawdzenia"
# print(z[1] + " " + z[-1])
#zad 8
# z= "tekst do sprawdzenia"
# print(z.split())
#zad 9
# napis= "ale urwał"
# print("%s\nale to było dobre" % napis)
# l = 7.3232323
# print("Ulubiona liczba to %(z1).0f" % {"z1" : l})
# pi = 3.14159265359
# print("Ile wynosi pi zaokrąglona do dwóch miejsc po przecinku??"
#       "\nPi = %(z1).2f" % {"z1" : pi} )
# zajęcia 2

#zad 1
# sporty = ["koszykówka", "siatkówka", "carlnig", "kickboxing"]
# print(sporty)
# sporty.reverse()
# sporty.append("carling")
# print(sporty)
#zad 2
# slownik = {"np": "na przykład", "pt" : "pod tytułem"}
# print(slownik)
# print(len(slownik))
#zad 4
# zdanie = input("Wpisz zdanie: ")
# print(zdanie.count("a"))
#zad 5
# sys.stdout.write("podaj a: ")
# a = sys.stdin.readline()
# a = int(a)
# sys.stdout.write("podaj b: ")
# b = sys.stdin.readline()
# b = int(b)
# sys.stdout.write("podaj c: ")
# c = sys.stdin.readline()
# c = int(c)
# sys.stdout.write(str(math.pow(a,b)+c))
# zad 6
# a = input("Wprowadz liczbe a:")
# b = input("Wprowadz liczbe b:")
# c = input("Wprowadz liczbe c:")
# a = int(a)
# b = int(b)
# c = int(c)
# if a == b == c:
#     print("Wprowadziłeś te same liczby")
# elif a>= b:
#     if a > c:
#         print("Liczba c jest największa")
#     else:
#         print("Liczba a jest największa")
# elif b > a:
#     if b > c:
#         print("Liczba b jest liczbą największą")
#     else:
#         print("Liczba c jest liczbą największą")
# zad7
# lista = [1, 2, 3 ,4 ,5 ,6 ,7]
# for a in lista:
#     print(a**2)
# zad8
# licznik = 0
# liczby_parzyste = []
# while licznik<10:
#     try:
#         liczba = input("Podaj liczbę: ")
#         if float(liczba):
#             liczba = float(liczba)
#             if liczba % 2 == 0:
#                 liczby_parzyste.append(liczba)
#             licznik += 1
#     except ValueError:
#         print("nie wczytano liczby")
# print(liczby_parzyste)
# print(len(liczby_parzyste))
# zad8
# licznik = 0
# liczby_pazyste = []
# while licznik < 10:
#     try:
#         liczba = input('wprowadź liczbę: ')
#         if float(liczba):
#             liczba = float(liczba)
#             if liczba % 2 == 0:
#                 liczby_pazyste.append(liczba)
#                 licznik += 1
#     except ValueError:
#         print('nie wczytano liczby')
# print(liczby_pazyste)
# print(len(liczby_pazyste))
#zad 9
# a = input("Podaj liczbę: ")
# try:
#     a = int(a)
#     pierwiastek = math.sqrt(a)
#     print(pierwiastek)
# except ValueError:
#     if type(a) != int:
#         print("Podałeś liczbę która nie jest całkowita")
#     elif a<0:
#         print("Liczba a jest mniejsza od zera")
# import random
# from math import *
# import ciagi.arytmetyczny
# from ciagi import *

#zad 1
# a = [1-x for x in range(1,11)]
# print(a)
# b = [4**x for x in range(0,7)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)
# zad 2
# import random
# lista1 = []
# licznik = 0
# while licznik != 10:
#     a = random.randint(0, 100)
#     lista1.append(a)
#     licznik +=1
# print(lista1)
# nowalista = [x for x in lista1 if x % 2 == 0]
# print(nowalista)
# zad3
# slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
# lista = [key for key in slownik.keys() if slownik[key] == 'sztuki']
# print(lista)
# zad 4
# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 = c**2:
#         return "trójkąt prostokątny"
#     else:
#         return " trójkąt nie jest prostokątny"
# print(trojkat_prostokatny(1,2,3))
# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         return 'trójtkąt prostokątny'
#     else:
#         return 'trójkąt nie jest prostokątny'
# print(trojkat_prostokatny(3, 4, 5))
# zad6
# def iloczyn(a=1, b=4, ile=10):
#     licznik = 0
#     while licznik != ile:
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn())