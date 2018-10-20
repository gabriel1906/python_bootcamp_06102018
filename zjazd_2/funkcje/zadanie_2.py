def wiecej_niz(napis, prog):
    return {y for y in napis if napis.lower().count(y) > prog}

if __name__ == "__main__":
    print(wiecej_niz("Ala ma kota", 2))
