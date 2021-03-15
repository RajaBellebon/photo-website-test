### Problem 4

#### Write a Python program to check whether a specified value is contained in a group of values.
#### Example :
### 3 -> [1, 5, 8, 3] : True
###-1 -> [1, 5, 8, 3] : False
###

list_1 = [1, 5, 8, 3]

def is_element_in_list(element, list_param):
       return element in list_param

print(is_element_in_list(1, list_1))
