from random import random
from random import gauss
import matplotlib.pyplot as plt

def f(x1,x2,x3):
    f=x1+2*x2+x2*x3-x1**2-x2**2-x3**2
    return f

def evol(u,v,w):
    plt.figure('Evolución de x1,x2,x3')
    plt.plot(u)
    plt.plot(v)
    plt.plot(w)
    plt.legend(('x1','x2','x3'))
    plt.ylim([-2, 2])
    plt.show()

def mutation(x,s):
    xn = x+s*gauss(0,1)
    while xn < -2 or xn > 2:
        xn = x+s*gauss(0,1)
    return xn

def sigma(s,g,m):
    ps = m/g
    c = 0.817
    if g%20 == 0:
    #if True:
        if ps > 0.2:
            s = s/c
        elif ps < 0.2:
            s = s*c
        else:
            s = s
    else:
        s = s
    return s
    
def main():
  
    x1min, x1max, x2min, x2max, x3min, x3max = [-2, 2, -2, 2, -2, 2]
    gmax = 1000           #máximo número de iteraciones
    m = 0                #número de mutaciones exitosas
    x1 = 4*random()+x1min
    x2 = 4*random()+x2min
    x3 = 4*random()+x3min
    x0y0z0 = [round(x1,6), round(x2,6), round(x3,6)]
    print("\t\t\t     x1\t      x2\tx3")
    print("Valores iniciales \t",*x0y0z0)
    padre = f(x1,x2,x3)
    s = 1
    u = [x1]
    v = [x2]
    w = [x3]
    
    for g in range(1,gmax):
        x1n = mutation(x1,s)
        x2n = mutation(x2,s)
        x3n = mutation(x3,s)
        hijo = f(x1n,x2n,x3n)
        if hijo > padre:
            x1 = x1n
            x2 = x2n
            x3 = x3n
            m += 1               #mutación exitosa
            padre = f(x1,x2,x3)
        s = sigma(s,g,m)
        u.append(x1)
        v.append(x2)
        w.append(x3)
        
    xfyfzf = [round(x1,6), round(x2,6), round(x3,6)]
    print("Valores finales \t",*xfyfzf,"\n")
    print("f(x1,x2,x3) =",round(f(x1,x2,x3),6))
    evol(u,v,w)
    
main()