def scope_test():
    x = 123
    return x


x = scope_test()
print(x)
def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
def my_function():
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

