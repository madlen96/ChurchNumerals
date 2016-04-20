#!/usr/bin/python
#Church numerals testing

#definition of several Church numerals
zero = lambda f: lambda x:x
one = lambda f: lambda x:f(x)
two = lambda f: lambda x:f(f(x))
three = lambda f: lambda x:f(f(f(x)))
four = lambda f: lambda x:f(f(f(f(x))))
five = lambda f: lambda x:f(f(f(f(f(x)))))

#definition of successor 
succ = lambda n: lambda f: lambda x: (f)(n(f)(x))

#definition of functions on Church numerals -> arithmetic operations on numbers

def add(m,n): #addition
    return lambda f: lambda x: m(f)(n(f)(x))
      
def mul(m,n): #multiplying
    return lambda f: lambda x: m(n(f))(x)

def exp(m,n): #exponentiation
    return lambda f: lambda x: (n)(m)(f)(x)

# Church numerals -> decimal numbers

def dec(n):
    return n(lambda x: x+1)(0)

#testing Church numerals: values and several operations

print("~~~~~~~~~ Let's test! ~~~~~~~~")
print("Zero = ",dec(zero))
print("One = ",dec(succ(zero)))
print("Two + Four = ",dec(add(two,four)))
print("Four + Five = ",dec(succ(succ(succ(succ(succ(four)))))))
print("One + Three = ",dec(add(one,three)))
print("Two * Two + 1 = ",dec(succ(mul(two,two))))
print("Two * Three = ",dec(mul(two,three)))
print("Two ^ Three = ",dec(exp(two,three)))
