import time

numer_pesel = input("Twój numer PESEL to: ... ? ")
wiek20=list(range(0,13))
wiek21=list(range(20,33))

if len(numer_pesel) == 11 and numer_pesel.isdigit() and int(numer_pesel[2]) == 0 or 1 or 2 or 3:
    print("Numer PESEL powinien być poprawny")
    time.sleep(1)
    if  int(numer_pesel[9]) %2==1:
        print("Jestes mezczyzna")
    elif int(numer_pesel[9]) %2==0:
        print("Jestes kobieta")
    time.sleep(1)
    if int(numer_pesel[2]) in {0,1}:
        print(f"Twoja data urodzenia to {numer_pesel[4]}{numer_pesel[5]}.{numer_pesel[2]}{numer_pesel[3]}.19{numer_pesel[0]}{numer_pesel[1]}")
    elif int(numer_pesel[2]) in{2,3}:
        print(f"Twoja data urodzenia to {numer_pesel[4]}{numer_pesel[5]}.{int(numer_pesel[2])-2}{numer_pesel[3]}.20{numer_pesel[0]}{numer_pesel[1]}")
    else:
        print("Twoj numer pesel nie isnieje")

    time.sleep(1)


else:   
    print("Twoj numer PESEL jest niepoprawny, sprawdz czy sklada sie z 11 cyfr")