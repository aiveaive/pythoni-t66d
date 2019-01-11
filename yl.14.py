def mitu_tais(txt):
    '''täishäälikute arv '''
    tais = 'AEIOUÕÄÖÜ'
    mitu = 0
    for t in txt:
       if t.upper() in tais:
        mitu += 1
    return mitu
tekst = input("Sisesta tekst")
n = mitu_tais(tekst)
print ("Täishäälikuid on:",n)