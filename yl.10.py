list = ["greipfruut", "mandariin", "kirss"]
print(list)
print(list[0])
list.append("granaatõun")
print(list[-1])
list[2]= "apelsin"
print(list)
puuvili = input("Sisesta puuvili:")
if puuvili in list:
    print(puuvili + " on nimekirjas")
else:
    print(puuvili + " ei ole nimekirjas")
print(len(list))
list.remove("mandariin")
print(list)
list.reverse()
print(list)
list.sort()
print(list)
