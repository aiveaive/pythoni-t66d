i = 0
print("Sisesta nullist suurem arv, mida soovid korrutada 1-12!")
x = int(input())
while i < 12:
    i = i + 1
    y = int(x * i)
    print(str(x) + " * " + str(i) + " =  " + str(y))