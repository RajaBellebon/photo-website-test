
list_a = [1, 1, 2 ,3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_c = []
intersection = []
for i in range (len(list_a)):
    for j in range (len(list_b)):
        if list_a[i] == list_b[j]:
            intersection.append(list_a[i])
print("The common numbers are"":")
print(intersection)