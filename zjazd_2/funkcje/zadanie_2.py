def wiecej_niz(napis, prog):
    return {znak for znak in napis if napis.lower().count(znak) > prog}

if __name__ == "__main__":
    print(wiecej_niz("Ala ma kota", 2))
