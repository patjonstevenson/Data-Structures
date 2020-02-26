import sys
# sys.path.append('../queue_and_stack/dll_stack')
from doubly_linked_list import ListNode as Node
from doubly_linked_list import DoublyLinkedList as DLL
# from dll_stack import Stack


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max_nodes = limit
        self.current_number_of_nodes = 0
        self.ordered_nodes = DLL(None)
        self.node_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        try: 
            node = self.node_dict[key]
        except KeyError:
            return None
        # if Node is None:
        #     print("\n\nThere is none!!\n\n")
        #     return None
        val = node.value[key]
        self.ordered_nodes.delete(node)
        self.ordered_nodes.add_to_tail(node)
        return val

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if len(self.ordered_nodes) + 1 > self.max_nodes and key not in self.node_dict:
            (head_key, head_val) = list(self.ordered_nodes.head.value.items())[0]
            self.ordered_nodes.remove_from_head()
            del self.node_dict[head_key]
        self.ordered_nodes.add_to_tail({key: value})
        node = self.ordered_nodes.tail
        self.node_dict[key] = node

