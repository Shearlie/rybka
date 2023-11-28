import time

print("Hello everybody")

x=0

czas_rozpoczecia=time.time()


while True:
    x=x+1
    print(x)
    if x == 5000:
        break

czas_zakonczenia=time.time()

czas_wykonywania_petli=czas_zakonczenia - czas_rozpoczecia

print("..........")
print(czas_wykonywania_petli, "sekund")