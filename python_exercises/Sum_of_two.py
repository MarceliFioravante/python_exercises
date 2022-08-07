'''Create a function called sumOfTwo(a, b, v) with 3 parameters.
a is a list of numbers values, such as [22, 341, 21, 5, 0, -5].
b is also a list of number values, just like a.
a and b can be anything; negative, a float, etc.
v is a single number value.
The function should check if it is possible to take one number from both list a and b, and add the numbers together
to equal the number v.
If there are 2 numbers that can do this, print “True”. Otherwise, print “False”.
For example:
sumOfTwo([1, 2, 3], [10, 20, 30], 23)
The output would be “True” because 2 + 20 = 23.'''

def sumOfTwo (a, b, v):
    var = False
    for c in range(0, len(a)):
        for d in range(0, len(b)):
            if a[c] + b[d] == v:
                var = True
    print(var)

sumOfTwo([1, 2, 3], [10, 20, 30], 55)