
#write a program that returns a list that contains only the common element 
#between thises two lists

a = [1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# call list c the list which will contain the common elements 
# and use the list comprehension
def comon_element(a,b):
    c= x for x in a if value in b]
    c.append(x)
    return c

print(comon_element(a,b))

print(c)



###


a = [1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for x in a:
    if x in b:
        c.append(x)

print( "The Common numbers are",(c))

###

# Does this program works with longer lists?
# We are using the random module for built two longer lists

import random

list_numbers1=[]
for i in range (23):
    list_numbers1.append(random.randint(1,100))
print(list_numbers1)
###


d = [8, 14, 61, 65, 19, 11, 79, 62, 59, 95, 15, 42, 1, 72, 77, 2, 52, 19, 10, 21]
e = [48, 99, 85, 15, 48, 45, 27, 72, 71, 8, 66, 65, 89, 99, 28, 39, 49, 17, 31, 17, 3, 54, 69]
f = []
for x in d:
    if x in e:
        f.append(x)

print( "The Common numbers are",(f))
print("The program works with lists longer than a and b" )

print("Does it works with lists builts with letters ?")


g = [ y, r, m, p, t, i, b, w, a ]
h = [ s, m, v, z, i, u, k, z, a ]
i = []
for x in g:
    if x in h:
        i.append(x)

print( "The Common letters are",(i))

