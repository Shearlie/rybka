import random
import time

time.sleep(1)

print("Gra w kamien papier nozyce")

time.sleep(1.5)

opcje=["kamien","papier","nozyce"]

punkty_gracza=0
punkty_komputera=0


while True:

    wybor_gracza=input("Wybierz kamien papier lub nozyce")
    wybor_komputera=random.choice(opcje)

    if wybor_gracza=="kamien" or "papier" or "nozyce":
        if wybor_gracza=="kamien" and wybor_komputera=="kamien":
            print("kamien vs kamien")
            time.sleep(1)
            print("Remis!")
        elif wybor_gracza=="kamien" and wybor_komputera=="papier":
            print("kamien vs papier")
            time.sleep(1)
            print("Przegrales!")
            punkty_komputera=punkty_komputera+1
        elif wybor_gracza=="kamien" and wybor_komputera=="nozyce":
            print("kamien vs nozyce")
            time.sleep(1)
            print("Wygrales")
            punkty_gracza=punkty_gracza+1
        elif wybor_gracza=="papier" and wybor_komputera=="kamien":
            print("papier vs kamien")
            time.sleep(1)
            print("Wygrales!")
            punkty_gracza==punkty_gracza+1
        elif wybor_gracza=="papier" and wybor_komputera=="papier":
            print("papier vs papier")
            time.sleep(1)
            print("Remis!")
        elif wybor_gracza=="papier" and wybor_komputera=="nozyce":
            print("papier vs nozyce")
            time.sleep(1)
            print("Przegrales")
            punkty_komputera=punkty_komputera+1
        elif wybor_gracza=="nozyce" and wybor_komputera=="kamien":
            print("nozyce vs kamien")
            time.sleep(1)
            print("Przegrales")
            punkty_komputera=punkty_komputera+1
        elif wybor_gracza=="nozyce" and wybor_komputera=="papier":
            print("nozyce vs papier")
            time.sleep(1)
            print("Wygrales")
            punkty_gracza=punkty_gracza+1
        elif wybor_gracza=="nozyce" and wybor_komputera=="nozyce":
            print("nozyce vs nozyce")
            time.sleep(1)
            print("Remis!")
            
            time.sleep(1)
            print(f"Wynik to {punkty_gracza} : {punkty_komputera}")
            time.sleep(1)
           
            print("Kolejna runda!")
        else:
            print("Wybierz kamien papier lub nozyce wpisujac te slowa")
            time.sleep(1)
            print("Wynik nie ulegl zmianie")
        

    time.sleep(2)