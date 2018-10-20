napis = input("Podaj napis: ")

SAMOGLOSKI = 'aeiou'
ile_samoglosek = 0

for znak in napis:
    # jeśli samogłoska to powiększ licznik
    if znak in SAMOGLOSKI:
        ile_samoglosek += 1

print(f"W tekście: {napis}, znajduje sie {ile_samoglosek} samogłoski")
