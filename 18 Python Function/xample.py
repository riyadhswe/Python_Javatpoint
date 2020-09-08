#The function simple_interest(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case
def simple_interest(p,t,r):
    return (p*t*r)/100
print("Simple Interest: ",simple_interest(t=10,r=10,p=1900))