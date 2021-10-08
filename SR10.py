def alg(a):
        c=1
        b=0
        while a>9:
            b=a%10
            a=a//10
            if(((b%2) == 0) & (b!=0)):
                c=c*b
                b=0
            else:
                b=0
        if (((a%2) == 0) & (a!=0)):
            c=c*a
        if c==1:
            print("Нет чётных чисел")
        else:
            print(c)
try:
    print("Введите натуральное число")
    a=int(input())
except ValueError:
    print("Incorrect value")
    exit()
alg(a)
    

    
