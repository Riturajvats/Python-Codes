#a = 250   #Global Scope
a = [1,2,3,4]
def f1():
     #a=100  #Local Scope
    a[0]= 5
    print(a)
def f2():
    a=50   #Local Scope
    print(a)

f1()
f2()
print(a)
