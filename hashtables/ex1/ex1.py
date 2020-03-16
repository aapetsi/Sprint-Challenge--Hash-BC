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
    
    if length == 2:
        if (weights[1] + weights[0]) == limit:
            answer.append(1)
            answer.append(0)
            return answer
        else:
            return None
    
    for idx, val in enumerate(weights):
        hash_table_insert(ht, val, idx)
    
    for x in range(length):
        # val = int(hash_table_retrieve(ht, weights[x]))
        check = limit - weights[x]
        # check if check is in table
        ans = hash_table_retrieve(ht, check)
        if ans is not None:
            answer.append(ans)    

    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
