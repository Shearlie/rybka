import random
import time

time.sleep(1)

print("Cześć!")
time.sleep(1)
print("Zagrajmy w kamien papier nozyce!")

time.sleep(1)

opcje=["kamien","papier","nozyce"]

punkty_gracza=0
punkty_komputera=0


while True:

    wybor_gracza=input("Wybierz kamien papier lub nozyce")
    wybor_komputera=random.choice(opcje)

    time.sleep(1.5)

    if wybor_gracza in opcje:
        if wybor_gracza=="kamien" and wybor_komputera=="kamien":
            print("kamien vs kamien")
            time.sleep(1)
            print("Remis!")
        elif wybor_gracza=="kamien" and wybor_komputera=="papier":
            print("kamien vs papier")
            time.sleep(1)
            print("Porazka:(")
            punkty_komputera=punkty_komputera+1
        elif wybor_gracza=="kamien" and wybor_komputera=="nozyce":
            print("kamien vs nozyce")
            time.sleep(1)
            print("Wygrana:)")
            punkty_gracza=punkty_gracza+1
        elif wybor_gracza=="papier" and wybor_komputera=="kamien":
            print("papier vs kamien")
            time.sleep(1)
            print("Wygrana:)")
            punkty_gracza==punkty_gracza+1
        elif wybor_gracza=="papier" and wybor_komputera=="papier":
            print("papier vs papier")
            time.sleep(1)
            print("Remis!")
        elif wybor_gracza=="papier" and wybor_komputera=="nozyce":
            print("papier vs nozyce")
            time.sleep(1)
            print("Porazka:(")
            punkty_komputera=punkty_komputera+1
        elif wybor_gracza=="nozyce" and wybor_komputera=="kamien":
            print("nozyce vs kamien")
            time.sleep(1)
            print("Porazka:(")
            punkty_komputera=punkty_komputera+1
        elif wybor_gracza=="nozyce" and wybor_komputera=="papier":
            print("nozyce vs papier")
            time.sleep(1)
            print("Wygrana:)")
            punkty_gracza=punkty_gracza+1
        elif wybor_gracza=="nozyce" and wybor_komputera=="nozyce":
            print("nozyce vs nozyce")
            time.sleep(1)
            print("Remis!")
            
        time.sleep(1)
        print(f"Wynik to {punkty_gracza} : {punkty_komputera}")
        time.sleep(1)


           
        kontynuacja_gry=input("Gramy dalej? wpisz tak/nie")

        time.sleep(1)

        if kontynuacja_gry== "tak" or "nie":
            if kontynuacja_gry== "tak":
                print("Kolejna runda!")
            elif kontynuacja_gry== "nie":
                print("Wielka szkoda ze juz nie gramy")
                time.sleep(1)
                print(f"Koncowy wynik to {punkty_gracza} : {punkty_komputera}, dzieki za gre!")
                break
             

    else:
            print("Wybierz kamien papier lub nozyce wpisujac te slowa")
            time.sleep(2)
            print("Wynik nie ulegl zmianie")
        

    time.sleep(1)