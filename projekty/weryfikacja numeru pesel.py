import time

numer_pesel = input("Twój numer PESEL to: ...")

if len(numer_pesel) == 11 and numer_pesel.isdigit():
    print("Numer PESEL jest poprawny")
else:
    print("Twoj numer PESEL jest niepoprawny, powinien sie skladac z 11 cyfr")

