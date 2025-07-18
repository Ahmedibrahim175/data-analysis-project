def list_multiplication_table(x):
    l1=[]
    for i in range(1,x+1):
        l2=[]
        for j in range(i,(i*i)+i,i):
            l2.append(j)
        l1.append(l2)
        del l2
    print(l1)

n=int(input("Enter your number:  "))
list_multiplication_table(n)

# example 
n=int(3)
list_multiplication_table(n)

