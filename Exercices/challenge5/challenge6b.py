
list1 = ['y','r','m','p','t','i','b','w','a']
list2 = ['s','m','v','z','i','q','z','a']
list3 = [x for x in list1 if x in list2]
print(list3)


###
list1 = ['y','r','m','p','t','i','b','w','a']
list2 = ['s','m','v','z','a','q','z','i']

set1= set (list1)
set2= set(list2)

set3= set1 & set2
list3 = list(set3)

print(list3)
print("She is the most cute Princess :)")
###