import time

numer_pesel = input("Twój numer PESEL to: ... ")
wiek20=list(range(0,13))
wiek21=list(range(20,33))

if len(numer_pesel) == 11 and numer_pesel.isdigit():
    print("Numer PESEL jest poprawny")
    time.sleep(1)
    if  int(numer_pesel[9]) %2==1:
        print("Jestes plci meskiej")
    elif int(numer_pesel[9]) %2==0:
        print("Jestes plci zenskiej")
    if int(numer_pesel[2,3]) in wiek20:
        print("Urodziles/as sie w 20 wieku")
    elif int(numer_pesel[2,3]) in wiek21:
        print("Urodziles/as sie w 21 wieku")
    else:
        print("Twoj numer pesel nie isnieje")




else:
    print("Twoj numer PESEL jest niepoprawny, powinien sie skladac z 11 cyfr")