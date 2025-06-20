def sum(n):
    return n*(n+1)/2

sum(5)

def arraySum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

a= [14,13,5,12]

arraysum(a)

def summ(n):
    if (n<=0):
        return 
    return n + summ(n-1)

summ(5)

