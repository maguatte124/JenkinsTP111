def fact(n):
    if(n==0):
        return 1
    else :
        return fact(n-1)*n
def saisie(n):
    t = []
    for i in range(n):
        #c = int(input(f"élément {i} : "))
        t.append(i)
    return t
def INV(t):
    n=len(t)
    tab=[]
    for i in range(n):
        tab.append((t[n-i-1]))
        #tab[i]=t[n-i-1]
    return tab

n=10
t=saisie(n)
print(t)
inverse=INV(t)
print(inverse)
som=[]
for i in range(n):
    som.append(t[i]+inverse[i])
print(som)
#for i in range(n):
#    print(fact(i))