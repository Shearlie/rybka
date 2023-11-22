import random
import time
print("Gra w kamien papier nozyce")

time.sleep(1)

opcje=["kamien","papier","nozyce"] 

wybor_gracza=input("ka-mien pa-pier no-zy-ce..?")
wybor_komputera=random.choice(opcje)

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
    print("Przegrałeś")


print("dziekuje za gre fani")


njnjnh