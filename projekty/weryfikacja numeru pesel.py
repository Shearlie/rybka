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
    if int(numer_pesel[2]) in {0,1}:
        print(f"Twoja data urodzenia to {numer_pesel[4]}{numer_pesel[5]}.{numer_pesel[2]}{numer_pesel[3]}.10{numer_pesel[0]}{numer_pesel[1]}")
    elif int(numer_pesel[2]) in{2,3}:
        print(f"Twoja data urodzenia to               efwhufhuiewhufiewuhifewhuifeuwhfuhiwfiuhewih       ")
    else:
        print("Twoj numer pesel nie isnieje")




else:   
    print("Twoj numer PESEL jest niepoprawny, powinien sie skladac z 11 cyfr")