def message():
    alt = 1
    print("Hello, World!")
    print(alt)


message()

a = 1


def fun():
    a = 2
    print(a)


fun()
print(a)

a = 1


def fun():
    global a
    a = 2
    print(a)


fun()
a = 3
print(a)

a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()
print(a)

