x = int(input("Podaj wsp x: "))
y = int(input("Podaj wsp y: "))

wym_x = int(input("Wymiar x: "))
wym_y = int(input("Wymiar y: "))

# dalej zakładamy, ze marginesy to 0.1 wymiaru


if x > wym_x or y > wym_y or x < 0 or y < 0:
    print("Wypadłeś z planszy")
elif x > 0.9 * wym_x and y > 0.9 * wym_y:
    print("Jesteś w prawy górnym rogu")
elif x > 90 and y < 0.1 * wym_y:
    print("Jesteś w prawy dolnym rogu")
elif x < 0.1 * wym_x and y < 10 * wym_y:
    print("Jesteś w lewym dolnym rogu")
elif x < 0.1 * wym_x and y < 90 * wym_y:
    print("Jesteś w lewym górnym rogu")
elif x < 0.1 * wym_x:
    print("Jesteś na lewej krawędzi")
elif x > 0.9 * wym_x:
    print("Jesteś na prawej krawędzi")
elif y < 0.1 * wym_y:
    print("Jesteś na dolnej krawędzi")
elif y > 0.9 * wym_y:
    print("Jesteś na górnej krawędzi")
else:
    print("Print jesteś w centrum")

