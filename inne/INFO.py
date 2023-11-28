print("Hello world")

#komentarz

zmienna=10
rzeczywista=10.5

print(zmienna)
print('%.20f'%rzeczywista)

tekst1="hello world"
tekst2='hello world'
tekst3="lorem ipsum 'dolor sit amet' consectetur"

print(tekst2)
print(tekst3)


print("Wartość zmiennej zmienna to:", zmienna)
print(f"Wartość zmiennej zmienna to: {zmienna}")
print("Wartość zmiennej zmienna to %.2f"%zmienna)
print("Wartość zmiennej zmienna to:" + str(zmienna))

#imie=input("Jak masz na imię? ")
#wiek=int(input("Ile masz lat? "))

#print("cześć, ", imie)
#print("masz ",wiek, "lat")

import random
los=random.randint(1, 20)
print(los)

import math
potega=math.pow(2, 3)
print(potega)

suma=2+2
roznica=4-2
iloczyn=4*2
iloraz=4/2
potega2=3**2
modulo=5%2


# liczba=int(input("podaj liczbe: "))

# if liczba>0:
#     print("Liczba jest wieksza od zera")
# elif liczba==0:
#     print("Liczba jest rowna zero")
# else:
#     print("Liczba jest mniejsza od zera")

#print("Liczba jest podzielna przez 2") if liczba%2==0 else print("Liczba nie jest podzielna przez 2")


for i in range(3):
    print("Numer: ", i)

for i in range(1, 101):
    if i%2==0:
        print(i)

for i in range(1, 101, 2):
    print(i)

for i in range(100, 0, -1):
    print(i)

for litera in "slowo":
    if litera=="o":
        break
    print(litera)

for litera in "slowo":
    if litera=="o":
        continue
    print(litera)


# liczba=int(input("Podaj liczbe: "))

# while liczba<0:
#     liczba=int(input("Podaj liczbe jeszcze raz: "))


# while True:
#     print("prawda")

def powitanie():
    print("Cześć!")

powitanie()

def powitanie_imienne(a):
    print("Cześć,", a)

powitanie_imienne("Jacek")

def dzielenie(dzielna, dzielnik):
    if dzielnik==0:
        return "Nie dziel przez 0"
    else:
        return dzielna/dzielnik
    
print(dzielenie(5,2))
print(dzielenie(3,0))
iloraz=dzielenie(3,4)
print(iloraz)

lista=[1,2,3,9,6,7,5]
print(type(lista))

print(lista)
print(*lista)
print(*lista, sep=";")

lista.sort()
print(lista)

lista.reverse()
print(lista)

lista.sort(reverse=True)
print(lista)

print(lista.count(3))

lista.remove(3)
print(lista)

lista.append(1)
print(lista)

print(lista[0])
print(len(lista))

lista[0]=1
print(lista)

for i in lista:
    print(i)

krotka=(1,2,3)
print(krotka)

krotka2=1,2,3,2.5,"abc"
print(krotka2)

krotka3=("abc",)
print(type(krotka3))

print(len(krotka2))  

kontakty={}
kontakty["Jan"] = 123456789
kontakty["Jacek"] = 234567890