barcode = "03600029145"
numbers = list(barcode)
numbers2 = []

print(numbers)
for i in numbers:
    i = int(i)
    numbers2.append(i)
odd = sum(numbers2[0::2])
print(odd)
odd = odd * 3
print(odd)
nodd = sum(numbers2[1::2])
print(nodd)
total = odd + nodd
print(total)
M = total % 10
print(M)
if M == 0:
    print("Kontrollarv on 0")
if M >0:
    print("Kontrollarv on "+ str(10 - M))
    




