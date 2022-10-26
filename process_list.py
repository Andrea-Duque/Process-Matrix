from functools import reduce

def process_list(elements):
    """
    Recibe una lista de numeros y devuelve una nueva con los elemenos
    cambiados. Cada elemento de la nueva será el promedio del valor antiguo y el de sus
    vecinos.
    """
    #Creo una lista vacía donde iré acumulando
    processed_list = []

    if len(elements) == 1:
        processed_list = elements
    else:

        #por cada element de la lista.
        for index, element in enumerate(elements):
            #lo proceso
            new_element = process_element(index, elements)
            #lo añado a la lista
            processed_list.append(new_element)
    #devuelvo la nueva lista
    return processed_list

def process_element(index, elements):
    """
    Recibe el índice de un elemento de una lista, 
    calcula su promedio con sus vecinos y devuelve dicho promedio
    """
    #obtengo la lista de vecinos
    indices = get_neighbours_indices(index, elements)
    values = get_neighbor_values(indices, elements)
    # calculo su promedio
    average = get_average(values)
    # lo promedio con el elemento en sí
    # devuelvo el valor final
    return average

def get_neighbours_indices(index, elements):
    """
    La lista de índices de los vecinos. Se incluye al propio elemento
    """
    """
    indices = []
    if index == 0:
        #el primero
        indices.append(index + 1)
    elif index == len(elements) - 1:
        # el último
        indices.append(index - 1)
    else:
        indices.append(index + 1)
        indices.append(index - 1)
    #incluyo al propio elemento como vecino de si mismo
    indices.append(index)
    return indices
    """
    indices = []

    indices.append(index + 1)
    indices.append(index - 1)
    #incluyo al propio elemento como vecino de sí mismo
    indices.append(index)
 
    #elimino los índices imposibles (menores que cero y mayores o iguales a la longitud de la lista)
    indices = list(filter(lambda x : x >= 0 and x < len(elements), indices)) #deberes: hacerle un filter a indices para eliminar valores imposibles (menor a cero o mayor o igual a la longitud de lista)
   
    return indices


def get_neighbor_values(indices, elements):
    values = []
    for index in indices:
        values.append(elements[index])
    return values

def get_average(values):
    """
    Recibe una lista de número y devuelve su promedio
    """
    return reduce(lambda a, b : a + b, values, 0) / len(values)



 