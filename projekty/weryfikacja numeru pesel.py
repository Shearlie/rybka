""" numer_pesel=int(input("Twój numer PESEL to: ..."))

cyfry=[0,1,2,3,4,5,6,7,8,9]

if len(numer_pesel)==11:
    print("ur mom") """

numer_pesel = input("Twój numer PESEL to: ...")

if not len(numer_pesel) == 11 and numer_pesel.isdigit():
    print("Błąd! Numer PESEL powinien składać się z 11 cyfr.")

