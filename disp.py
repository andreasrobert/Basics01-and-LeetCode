def lol(n):

    for i in range(2,n//2):

        if n % i == 0 :
            print(i)
            return False
            
    return True



print(lol(29))


def lol1():

    for i in range(15):

        print(i)
            
    return True



print(lol1())
