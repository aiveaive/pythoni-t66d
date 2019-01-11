from random import randint
arv = randint(0,100) # juhuslik täisarv
print("Arva ära täisarv nullist sajani!")
arvamus = int(input())
while arvamus != arv:
    if arv > arvamus:
        print("Arv on suurem!")
    else:
        print("Arv on väiksem!")
    print("Paku veel!")
    arvamus = int(input())
print("Õige arv!")