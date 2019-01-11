a = float(input("Sisesta kolmnurga esimese külje pikkus: "))
b = float(input("Sisesta kolmnurga teise külje pikkus: "))
c = float(input("Sisesta kolmnurga kolmanda külje pikkus: "))
if a == b and b == c:
    print("See on võrdkülgne kolmnurk.")
if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print("See on võrdhaarne kolmnurk.")
if (a + b < c) or (b + c < a) or (a + c < b):
    print("Sellist kolmnurka pole olemas.")
else:
    print("See on erikügne kolmnurk.") 

