#
#import math
import numpy as np
#

#
print('\nExample of squaring elements in a list')
print(np.square([1, 2, 3, 4, 5]))


print('\nExample of taking the square root of a list')
print(np.sqrt([1, 4, 9, 16, 25]))


print('\nExamples of taking the cube of a list')
print(np.power([1, 2, 3, 4, 5], 3))



print('\nExamples of adding lists')
list1 = [1, 2, 3]; print("list1 = ", list1)
list2 = [4, 5, 6]; print("list2 = ", list2)
print("np.add(list1,list2) = ", np.add(list1,list2))
print()

list1 = [1, 2, 3] 
list3 = [[10], 
        [20],
        [30]]
print("list3 = ", list3)
print("np.add(list1,list3) = "); print(np.add(list1,list3))
print()

list4 = [1, 2, 3, 4, 5, 6, 7]
print("list4 = ", list4)
print("np.sum(list4) = ", np.sum(list4))
# print("sum(list4) = ", sum(list4))
print()


print('\nExamples of finding out how big your matrix is')
'''numpy.argmax(array, axis = None, out = None) 
returns the index that corresponds to the maximum value in a list.
But it doesn't tell you what that value is so you need add another line.
'''
list5 = [1, -2, 3, -40, 5, 100, -7, 0] 
max_index = np.argmax(list5) # result = 5 (corresponding to 100)
i = int(max_index); print(i, type(i))
max_value = list5[i]
print('max_index =', max_index)
print('max_value =', max_value)

min_index = np.argmin(list5) # result = 3 (corresponding to -40)
j = int(min_index)
min_value = list5[j]
print('min_index =', min_index)
print('min_value =', min_value)


print('\nExample of generating a 4X3 "zero matrix" list of lists in one line') 
#
width = 3 ; height = 4
z1 = [[0.0 for i in range(width)] for j in range(height)]       # This is actually a list of lists. Note the commas between elements.
#
print ("z1 = ", z1); print ("type(z1) = ", type(z1))

