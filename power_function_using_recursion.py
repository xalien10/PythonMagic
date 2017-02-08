#This small program shows how to use recursion to get power of a number in python

def power(x,n):
    if(n==0):
        return 1;
    return x*power(x,n-1)

print("cube of 2 is: %f" %power(2,4))
