### Problem 3

#### Write a Python program to display the first and last colors from the following list.

#### color_list = ["Red","Green","White" ,"Black"]


color_list = ["Red","Green","White","Black"]
print(color_list)
del color_list[1:2]
del color_list[1:2]
print(color_list)


list_1 = ["Red","Green","White" ,"Black"]
def first_last(list_1): 
    print("first element is"+list_1[0]+"last element is"+[len(list_1)-1])
    