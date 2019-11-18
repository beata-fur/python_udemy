import sys

print("Witaj w prostym kalkulatorze")
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

if b == 0:
    print("Nie wolno dzielic przez 0 !")
    sys.exit()

c = int(input("Wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie, "
              "5 - potegowanie, 6 - pierwiastkowanie: "))
if c == 1:
    wynik = a + b
elif c == 2:
    wynik = a - b
elif c == 3:
    wynik = a * b
elif c == 4:
    wynik = a / b
elif c == 5:
    wynik = a ** b
elif c == 6:
    wynik = a ** (1.0/b)


else:
    print("Dokonales zlego wyboru")

print("Wynik dzialania to: ", wynik)

