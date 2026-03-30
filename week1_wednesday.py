
def whatever(x):
    x = x.strip()
    x = x.title()
    x = " ".join(x.split())

    print(x)

name = input("What is your full name? ")    

whatever(name)