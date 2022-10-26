from functools import reduce

def process_matrix(matrix):
    processed_matrix = []

    for i, column in enumerate(matrix):
        processed_list = []
        for j, value in enumerate(column):
            new_value = process_elements(i, j, matrix)
            processed_list.append(new_value)

        processed_matrix.append(processed_list)
    return processed_matrix

def process_elements(matrix_index, list_index, elements):

    indices_normal = get_neighbours_indices(list_index, elements[matrix_index])
    neighbor_list = get_other_neighbors_list(list_index, elements)
    indices_neighbor = get_neighbours_indices(matrix_index, neighbor_list)

    values_normal = get_neighbor_values(indices_normal, elements[matrix_index])
    values_normal.append(elements[matrix_index][list_index])
    values_neighbor = get_neighbor_values(indices_neighbor, neighbor_list)

    values = values_normal + values_neighbor
    average = get_average(values)
    return average

def get_neighbours_indices(index, elements):

    indices = []

    indices.append(index + 1)
    indices.append(index - 1)
 
    indices = list(filter(lambda x : x >= 0 and x < len(elements), indices))
   
    return indices

def get_other_neighbors_list(index, elements):
    neighbors = []
    for column in elements:
        neighbors.append(column[index])

    return neighbors


def get_neighbor_values(indices, elements):
    values = []
    for index in indices:
        values.append(elements[index])
    return values

def get_average(values):

    return reduce(lambda a, b : a + b, values, 0) / len(values)


matrix = [[2,3,5,1], [4,7,9,3], [5,1,8,7], [6,4,2,3]]

print(process_matrix(matrix))

