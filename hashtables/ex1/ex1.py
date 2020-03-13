#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    answer = []
    """
    YOUR CODE HERE
    """
    if length == 1:
        return None
    
    for i, val_1 in enumerate(weights):
        for j, val_2 in enumerate(weights):
            if i != j:
                total = val_1 + val_2
                if total == limit:
                    if i > j:
                        answer.append(i)
                        answer.append(j)
                    else:
                        answer.append(j)
                        answer.append(i)
    

    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
