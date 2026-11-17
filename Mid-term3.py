def fx2(n, gn):
    true=1
    for i in range(n):
        for j in range(gn):
            if(true>gn):
                true=1
            if(true==j+1 and true<=gn+1):
                print(f'{i+1}號是第{j+1}組')
        true+=1
#fx2(15,4)
a=int(input("共幾人"))
b=int(input("共幾組"))
fx2(a,b)
