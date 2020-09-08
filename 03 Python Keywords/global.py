def my_func():
    global a
    a = 10
    b = 20
    c = a + b
    print(c)


my_func()


def func():
    print(a)


func()