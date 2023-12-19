import time

time.sleep(1)

wybrana_figura=input("Jakiej figury pole chcesz obliczyc? ")

figury_geometryczne=["prostopadloscian", "szescian", "graniastoslup", "kula", "stozek", "ostroslup"]


figura_podstawy_graniastoslupa=["kwadrat","prostokat", "trojkat", "trapez"]

if not wybrana_figura in figury_geometryczne:
    print("Popelniony zostal blad w wybieraniu figury od obliczenia pola. Sproboj jeszcze raz")

if wybrana_figura==figury_geometryczne[0]:
    a=input("Ile wynosi dlugosc pierwszego boku podstawy prostopadloscianu? ")
    b=input("Ile wynosi dlugosc drugiego boku podstawy prostopadloscianu? ")
    h=input("Ile wynosi wysokosc tego prostopadloscianu? ")
    objetosc_figury=a*b*h 
    
elif wybrana_figura==figury_geometryczne[1]:
    a=input("Ile wynosi dlugosc krawedzi tego szczesciau")
    objetosc_figury=a*a*a

elif wybrana_figura==figury_geometryczne[2]:
    pp_graniastoslupa=input("Z jakiego wielokata utworzona jest podstawa tego graniastoslupa? ")
    if  pp_graniastoslupa not in figura_podstawy_graniastoslupa:
        print("Błąd.")
    if pp_graniastoslupa==figura_podstawy_graniastoslupa[0]:
        a=input("Ile wynosi dlugosc boku tego kwadratu? ")
    elif pp_graniastoslupa==figura_podstawy_graniastoslupa[1]:
        a=input("Ile wynosi dlugosc pierwszego boku tego prostokata? ")
        b=input("Ile wynosi dlugosc drugiego boku tego prostokata? ")
    elif pp_graniastoslupa==figura_podstawy_graniastoslupa[2]:
        a=input("Ile wynosi dlugosc boku tego trojkata? ")
        g=input("Ile wynosi dlugosc wysokosci poprowadzonej z boku a tego trojkata? ")
    elif pp_graniastoslupa==figura_podstawy_graniastoslupa[3]:
        a=input("Ile wynosi dlugosc pierwszej podstawy tego trapezu? ")
        b=input("Ile wynosi dlugosc drugiej podstawy tego trapezu? ")
        g=input("Ile wynosi wysokosc poprowadzona od jednej do drugiej podstawy tego trapezu? ")


#OBLICZYC TERAZ WPROWADZIC POLA DO TEGO GRANIASTOSLUPA


        figura_podstawy_graniastoslupa[1]="a*b"RERE
    
        figura_podstawy_graniastoslupa[2]="a*h/2"
        figura_podstawy_graniastoslupa[3]="(a+b)*h/2"
    h=input("Ile wynosi wysokosc tego graniastoslupa? ")
    objetosc_figury=pp*h

