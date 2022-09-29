def Swap(a,b):
    z=a
    a=b
    b=z
    
    return a,b
    
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

x, y = Swap(x,y)

print("x =",x,"e y =", y)
