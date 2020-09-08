a=0
b=5
try:
    c = b/a
    print(c)
except Exception as e:
    print(e)
finally:
    print('Finally always executed')