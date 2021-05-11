
####
def suit_fibronacci(number_of_terms):
    counter = 0 

    first = 0
    second = 1
    temp = 0

    while counter <= int(number_of_terms):
        print(first)
        temp = first + second
        first = second
        second = temp
        counter = counter + 1
print("a is the rank of the number expected of the Fibonacci list")  
a = input("Please enter the number a :") 

print(suit_fibronacci(a))
suit_fibronacci(a)



####
# Program to display the Fibonacci sequence up to n-th term

def fibo_with_entry():
    nterms = int(input("How many terms?"))
    
    #first tow terms
    n1, n2 = 0, 1
    count= 0

    #check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive interger")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count<nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 += nth 
        count += 1


fibo_with_entry()


    