from random import randint
while True:
    print("Vajuta kas kivi(1), paber(2) või käärid(3) ja enter! Kui soovid lõpetada, vajuta(4)!")
    kasutaja = int(input())
    arvuti = randint(1, 3)
    if arvuti == kasutaja:
        print("Viik")
    elif arvuti != kasutaja:
        if arvuti == 1:
            if kasutaja == 2:
                print("Arvuti valis kivi ja sina võitsid!")
            if kasutaja == 3:
                print("Arvuti valis kivi ja võitis!")
        elif arvuti == 2:
            if kasutaja == 1:
                print("Arvuti valis paberi ja võitis")
            if kasutaja == 3:
                print("Arvuti valis paberi ja sina võitsid!")
        elif arvuti == 3:
            if kasutaja == 1:
                print("Arvuti valis käärid ja sina võitsid!")
            if kasutaja == 2:
                print("Arvuti valis käärid ja võitis!")
    if kasutaja == 4:
       break
