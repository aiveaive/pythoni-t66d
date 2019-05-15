datadict = {
    "name" : "Aive",
    "lastname" : "Pähn",
    "year" : 1969,
    "place" : "Kõrkküla",
    "food" : "Kreembrülee"
}
print (datadict)
x = datadict["place"]
print (x)
y = datadict.get("place")
print (y)
datadict["food"] = "Pavlova"
print (datadict)
for x in datadict:
  print(x)
for x in datadict:
  print(datadict[x])
for x in datadict.values():
  print(x)
for x, y in datadict.items():
  print(x, y)
if "isikukood" in datadict:
  print("Jah, isikukood on nimekirjas")
else:
      print("Ei, isikukoodi ei ole nimekirjas")
print(len(datadict))      
datadict["pikkus"] = 167
print(datadict)
datadict.pop("year")
print(datadict)
datadict.popitem()
print(datadict)
datadict.popitem()
print(datadict)
del datadict["lastname"]
print(datadict)
datadict.clear()
print(datadict)