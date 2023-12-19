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
    pp=figura_podstawy_graniastoslupa(0 - "a*a", 1 - "a*b")
    h=input("Ile wynosi wysokosc tego graniastoslupa? ")
    objetosc_figury=pp*h

