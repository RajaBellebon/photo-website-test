
liste1 = ['y','r','m','p','t','i','b','w','a']
liste2 = ['s','m','v','z','i','q','z','a']
intersection = [x for x in liste2 if x in liste1]
print(intersection)



#try to delete the duplicates numbers

a = [1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]

for x in a:
    if x in b:
        if x in c:
            print (x)
        else:
            c.append(x)

print( "The Common numbers are",(c))
