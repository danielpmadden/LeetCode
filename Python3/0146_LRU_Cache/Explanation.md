# Building an O(1) LRU Cache with a Hash Map and Doubly Linked List in Python

## Problem Understanding
We need to design a data structure that stores key-value pairs and can quickly return values and insert new ones. When the cache reaches its capacity, it must remove the least recently used (LRU) key to make room for new data.

We must support two operations in O(1) average time:
- `get(key)`: Return the value of the key if it exists, otherwise -1.
- `put(key, value)`: Insert or update the value of the key. If the cache is full, remove the least recently used key.

Both operations must be efficient, so we cannot rely on basic lists or arrays.

## Intuition
We need two key abilities:
1. Fast lookups to check if a key exists.
2. Fast reordering of usage to track which items were recently accessed.

We can achieve this using two data structures:
- A hash map for O(1) lookups.
- A doubly linked list to track the order of use.

The most recently used node will be at the head of the list.
The least recently used node will be at the tail of the list.

## Data Structure Design
1. **Hash Map (dictionary)**  
   Maps each key to its corresponding node in the linked list.  
   Enables O(1) lookup, insert, and delete.

2. **Doubly Linked List**  
   Stores the actual order of usage.  
   When a key is used, its node is moved to the front (most recent).  
   When the cache exceeds capacity, the node at the tail is removed.

We use dummy head and tail nodes to simplify edge cases during insertion and removal.

## Operations

### get(key)
- If key not found, return -1.
- If found:
  - Move its node to the head (most recently used position).
  - Return its value.

### put(key, value)
- If key already exists, remove its old node.
- Create a new node and insert it right after the head.
- If the number of keys exceeds capacity:
  - Remove the node at the tail (least recently used).
  - Remove its key from the map.

Each operation involves at most a few pointer changes and dictionary updates, ensuring O(1) time complexity.

## Implementation

```python
class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = self.Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
