aasta = int(input("Sisesta aasta, mida soovid kontrollida ja vajuta enter:"))
if aasta % 4 == 0:
    if aasta % 100 == 0:
        if aasta % 400 == 0:
            print(str(aasta) + " on liigaasta.")
        else:
            print(str(aasta) + " ei ole liigaasta.")
    else:
        print(str(aasta) + " on liigaasta.")
else:
    print(str(aasta) + " ei ole liigaasta.")