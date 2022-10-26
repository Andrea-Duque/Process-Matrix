

#if __name__ == "__main__":
    #averages = process_list(numbers)
    #print(numbers)
    #print("Averages")
    #print(averages)

#   for i in range(15):
    #averages = process_list(averages)
    #print(averages)



def get_other_neighbors(index, matrix):
    neighbors = []
    for column in matrix:
        neighbors.append(column[index])
    return neighbors

def get_neighbours_indices(index, elements):

    indices = []

    indices.append(index + 1)
    indices.append(index - 1)
    indices.append(index)
 
    indices = list(filter(lambda x : x >= 0 and x < len(elements), indices))
   
    return indices

#matrix = [[2,3,5,1], [4,7,9,3], [5,1,8,7], [6,4,2,3]]


 

# input list
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
 
# output list
output = []
 
# function used for removing nested
# lists in python using recursion
def reemovNestings(lst):
    output = []
    for i in lst:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)
    return output
 
 

def flatten(arg):
    if not isinstance(arg, list): # if not list
        return [arg]
    return [x for sub in arg for x in flatten(sub)] # recurse and collect

def flaten2(list1, list2):
    return list1 + list2


#print(flatten([[1,1],2,[1,1]])) # [1, 1, 2, 1, 1]
#print(flatten([1,[4,[6]]]))     # [1, 4, 6]

print(flaten2([1,2,3,4], [5,6,7,8]))