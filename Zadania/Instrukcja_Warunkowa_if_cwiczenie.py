print("Witaj w programie Beata, podaj dwie liczby.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugę liczbę: "))

if a > b:
    print("Liczba " + str(a) + " jest wieksza od liczby " + str(b))

elif a == b:
    print("Liczba", a, "jest równa liczbie", b)

elif a < b:
    wynik = b/a

    print("Liczba", a, "jest mniejsza od liczby", b,
          "\na wynik dzielenia drugiej liczny przez pierwsza wynosi: ", wynik)


