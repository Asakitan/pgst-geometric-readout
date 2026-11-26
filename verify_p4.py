"""Exact checks of the P4 example in Z[phi] and of its endpoint symmetry."""
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])

def neg(a):
    return (-a[0],-a[1])

def multiply(a,b):
    x,y=a
    u,v=b
    return (x*u+y*v,x*v+y*u+y*v)  # phi^2=phi+1

def power(a,n):
    out=(1,0)
    for _ in range(n):
        out=multiply(out,a)
    return out

def trace(a):
    return 2*a[0]+a[1]

def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

if __name__=="__main__":
    phi=(0,1)
    # The tridiagonal path recurrence is f_j=z f_(j-1)-f_(j-2).
    f0,f1=[1],[0,1]
    for k in range(2,5):
        p=[0]+f1
        for i,c in enumerate(f0):
            p[i]-=c
        f0,f1=f1,p
    assert f1==[1,0,-3,0,1]
    roots=(phi,(-1,1),(1,-1),neg(phi))
    a=[[int(abs(i-j)==1) for j in range(4)] for i in range(4)]
    a3=matmul(matmul(a,a),a)
    assert all(a3[i][j]-2*a[i][j]==int(i+j==3)
               for i in range(4) for j in range(4))
    for j,r in enumerate(roots):
        s=(1,0) if j%2==0 else (-1,0)
        assert add(add(power(r,4),multiply((-3,0),power(r,2))),(1,0))==(0,0)
        assert add(power(r,3),multiply((-2,0),r))==s
        assert trace(r)==s[0]
    rho=power(phi,6)
    assert rho==(5,8) and (rho[0]%4,rho[1]%4)==(1,0)
    assert multiply(phi,(1,-1))==(-1,0)  # |phi'|=phi^-1
    print("P4: exact characteristic polynomial, endpoint signs, traces, and mod-4 ratio verified.")
