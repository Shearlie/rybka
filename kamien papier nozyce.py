import random
import time

time.sleep(1)

print("Gra w kamien papier nozyce")

time.sleep(1.5)

opcje=["kamien","papier","nozyce"] 

wybor_gracza=input("Wybierz kamien papier lub nozyce")
wybor_komputera=random.choice(opcje)



while True:
    if wybor_gracza=="kamien" and wybor_komputera=="kamien":
        print("kamien vs kamien")
        time.sleep(1)
        print("Remis!")
    elif wybor_gracza=="kamien" and wybor_komputera=="papier":
         print("kamien vs papier")
         time.sleep(1)
         print("Wygrales!")
    elif wybor_gracza=="kamien" and wybor_komputera=="nozyce":
         print("kamien vs nozyce")
         time.sleep(1)
         print("Przegraleś")
    elif wybor_gracza=="papier" and wybor_komputera=="kamien":
        print("papier vs kamien")
        time.sleep(1)
        print("Wygrales!")
    elif wybor_gracza=="papier" and wybor_komputera=="papier":
        print("papier vs papier")
        time.sleep(1)
        print("Remis!")
    elif wybor_gracza=="papier" and wybor_komputera=="nozyce":
        print("papier vs nozyce")
        time.sleep(1)
        pritn("Przegrales")
    elif wybor_gracza=="nozyce" and wybor_komputera=="kamien":
        print("nozyce vs kamien")
        time.sleep(1)
        print("Przegrales")
    elif wybor_gracza=="nozyce" and wybor_komputera=="papier":
        print("nozyce vs papier")
        time.sleep(1)
        print("Wygrales")
    elif wybor_gracza=="nozyce" and wybor_komputera=="nozyce":
        print("nozyce vs nozyce")
        time.sleep(1)
        print("Remis!")
        
        
        
        print("dziekuje za gre fani")