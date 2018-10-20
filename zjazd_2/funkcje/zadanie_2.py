def wiecej_niz(napis, prog):
    return { x for x in napis if napis.lower().count(x) > prog}

if __name__ == "__main__":
    print(wiecej_niz("Ala ma kota", 2))
