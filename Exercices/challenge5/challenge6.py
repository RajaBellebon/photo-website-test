
# write a program that returns a list that contains only the common element 
# between thises two lists

list_a = [1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_c = []
# call list_c the list which will contain the common elements and use the list comprehension
def comon_element(list_a , list_b):
    list_c = [x for x in list_a if x in list_b]
    return list_c

print(comon_element(list_a,list_b))

print(list_c) 
