def diff(p):
    "Compute the derivative of p(x)."
    deg_p = len(p) - 1
    if deg_p == [0]:
        return[0]
    else:
        return [p[k]*k for k in range(1,deg_p+1)]
    
def evalp(p,a):
    "Compute p(a)"
    return sum([p[k]*a**k for k in range(0,len(p))])