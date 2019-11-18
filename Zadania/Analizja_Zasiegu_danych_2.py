global a
a = 1
b = 2


def function(z):
    d = 3
    print(a * b * d * z)
    z += 1
    return


c = int(input("Podaj zmienna liczbowa: "))
function(c)
print("c =", c)
