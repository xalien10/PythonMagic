# this is a python program where we calculated factorial value of a number using general approach and also by using lambda function
def Facto(n):
    if n==1 or n==1:
        return  1
    else:
        return n* Facto(n-1)

facto = lambda x: 1 if x==1 or x==0 else x*facto(x-1)


print Facto(n=input('Enter number: '))

m=input('Enter Number: ')
print facto(int(m))
