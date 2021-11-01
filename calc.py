def c():
    n1,a,n2=input().split()
    n1=int(n1)
    n2=int(n2)
    r=0
    if a=='+': r=n1+n2
    elif a=='-': r=n1-n2
    elif a=='*': r=n1*n2
    elif a=='/': r=n1/n2
    elif a=='**': r=n1**n2
    elif a=='//': r=n1//n2
    elif a=='%': r=n1%n2
    print(f'{n1} {a} {n2} = {r}')