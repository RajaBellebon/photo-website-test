 
###Enter the rank fo the number of Fibronacci list that you want generate

def suit_fibronacci(n):
 
    if n==1 or n==2:
        return 1
    else:
        x=1
        y=1
        for i in range (n-2):
            z=x+y
            x=y
            y=z
        return y
for i in range (1,12):
    print(suit_fibronacci(i))

suit_fibronacci(i)

####

### With the recursive method

def suit_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return suit_fibonacci(n-1) + suit_fibonacci(n-2)
n = int(input('Please enter a number: ')) 
for n in range(1, n):
    print(n, ":", suit_fibonacci(n))

suit_fibonacci(n)
