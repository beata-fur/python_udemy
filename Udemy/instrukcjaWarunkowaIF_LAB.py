min_likes: int = 500
min_shares = 100

num_likes = 1500
num_shares = 55

if num_likes >= min_likes and num_shares >= min_shares:
    print("Dostaniesz 10% znizki na zakupy")
else:
    if num_likes < min_likes:
        print("Daj lajka a bedzie znizka, potrzeba wiecej lajkow")
    else:
        print("Brakuje udostepien by dostac znizke")

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Dostaniesz kupon na hamburger")
else:
    if isWeekend:
        print("Musisz zamowic poza weekendem by dostac znizke")
    else:
        print( "Musisz zamowic pizze lub duzy napoj by dostac znizke.")



diskSize = 240
diskSizeUsed = 133
fileSize = 10

if (diskSize - diskSizeUsed) >= fileSize:
    print("File can be downloaded")
else:
    print("File cannot be downloaded")







