# Some common functions
def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)

#Example
print(factorial(5))

def harmonic(n):
    if(n==1): 
        return 1.0
    return harmonic(n-1) + 1.0/n

#Example
print(harmonic(2))
print(harmonic(10))
print(harmonic(100))

