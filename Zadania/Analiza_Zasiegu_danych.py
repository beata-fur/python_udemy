x = 1


def function():
    global x
    global y
    x = 2
    y = 3
    print("funkcja x=", x, "y =", y)
    return


print(x)
function()
print(x)
print(y)
