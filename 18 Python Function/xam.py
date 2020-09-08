# function func is called with the name and message as the keyword arguments
def func(name, message):
    print("printing the message with", name, "and ", message)

    # name and message is copied with the values John and hello respectively
    func(name="John", message="hello")