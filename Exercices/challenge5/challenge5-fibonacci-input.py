
### Problem 5

### Wtite a program that asks the user hox many Fibonacci numbers to generate and then generates them

### the Fibonacci sequence looks like this: 1,1,2,3,5,8,13,21, ...


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
a = int(input('Please enter a number')) 
print(suit_fibronacci(a))

      

