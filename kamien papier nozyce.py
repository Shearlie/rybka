import random
print("Gra w kamien papier nozyce")
opcje= [ kamien, papier, nozyce ] 
print(opcje)
wybor_gracza=int(input("kamien/papier/nozyce"))
wybor_komputera=random.randrange["kamien", "papier", "nozyce"]
if wybor_gracza=="kamien" and wybor_komputera=="kamien":
    print("remis!")
