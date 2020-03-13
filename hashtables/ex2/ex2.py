#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (int(length) - 1)
    
    # construct hash table
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    check = "NONE"
    for i in range(length):
        destination = hash_table_retrieve(hashtable, check)
        if destination is not None and destination is not "NONE":
            route[i] = destination
            check = destination
    
    return route
