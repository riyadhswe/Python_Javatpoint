def outside_function():
    a = 20
    def inside_function():
        nonlocal a
        a = 30
        print("Inner function: ",a)
    inside_function()
    print("Outer function: ",a)
outside_function()