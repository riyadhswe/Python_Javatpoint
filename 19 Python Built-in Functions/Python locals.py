def localsAbsent():
    return locals()


def localsPresent():
    present = True
    return locals()


print('localsNotPresent:', localsAbsent())
print('localsPresent:', localsPresent())