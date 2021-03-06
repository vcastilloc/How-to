'''
This is a simple code that solves the differential equation
$\frac{dN}{dt}=-\alpha N$
'''
#Definition of functions
def dNdt(N,t):
    aux=1.
    return -aux*N
#Initial conditions
dt=0.001
N0=1.
t0=0.
n=10000
#Integration by using the simples method
for i in range(n):
    N0+=dt*dNdt(N0,t0)
    t0+=dt
    print(t0,N0)
