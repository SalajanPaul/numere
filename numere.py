
def adunare():
    print("Va rog introduceti un numar natural de doua cifre:")
    x =int(input())
    z = x // 10
    u = x % 10
    print("Numarul rezultat prin adunarea cifrei zecilor si unitatilor este: ", z+u)

def adunare3():
    print("Va rog introduceti un numar natural de trei cifre:")
    x=int(input())
    s = x // 100
    z = x // 10 % 10
    u = x % 10
    print("Numarul rezultat prin adunarea cifrei zecilor si unitatilor este: ", s+z+u)

def oraminute():
    print("Va rog introduceti o ora:")
    o=int(input())
    print("Va rog introduceti minutele:")
    m=int(input())
    print("Va rog introduceti numarul de minute pe care doriti sa il adaugati:")
    x=int(input())
    om = o*60 + m + x
    print("Ora noua este: ", om // 60, " , minute ", om%60)





if __name__ == '__main__':
    #adunare()
    #adunare3()
    oraminute()



