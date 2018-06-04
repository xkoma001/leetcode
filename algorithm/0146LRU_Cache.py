
class Node:
    def __init__(self, key, val):
        self.next = None
        self.val = val
        self.key = key


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache_len = 0
        self.capacity = capacity
        self.dummy = Node(0, 0)
        self.tail = self.dummy
        self.hash_prev = dict()

    def adjust_link(self, prev, val):
        cur_node = prev.next
        cur_node.val = val
        if cur_node == self.tail:
            return
        prev.next = cur_node.next
        self.hash_prev[cur_node.next.key] = prev
        self.tail.next = cur_node
        cur_node.next = None
        self.hash_prev[cur_node.key] = self.tail
        self.tail = cur_node
        return

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_prev:
            cur_val = self.hash_prev[key].next.val
            self.adjust_link(self.hash_prev[key], cur_val)
            return cur_val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.hash_prev:
            self.adjust_link(self.hash_prev[key], value)
        else:
            assert self.capacity > 0
            if self.cache_len == self.capacity:
                del self.hash_prev[self.dummy.next.key]
                self.dummy.next = self.dummy.next.next
                if self.dummy.next:
                    self.hash_prev[self.dummy.next.key] = self.dummy
            else:
                self.cache_len += 1
            self.hash_prev[key] = self.tail
            cur_node = Node(key, value)
            self.tail.next = cur_node
            self.tail = cur_node
        return

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)


class Node2:
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v


class LRUCache2:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.len_em = 0
        self.head = Node2(0, 0)
        self.tail = Node2(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_em = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_em:
            return -1

        node = self.hash_em[key]
        self._adjust_tail(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.hash_em:
            new_node = Node2(key, value)
            self.hash_em[key] = new_node
            self._add_node(new_node)
            if self.len_em == self.capacity:
                del self.hash_em[self.head.next.key]
                self._remove_node(self.head.next)
            else:
                self.len_em += 1
        else:
            self._adjust_tail(self.hash_em[key])
            self.hash_em[key].val = value
        return

    def _adjust_tail(self, node):
        cur_node = self._remove_node(node)
        self._add_node(cur_node)
        return

    def _add_node(self, node):
        p = self.tail.prev
        node.next = self.tail
        node.prev = p
        self.tail.prev = node
        p.next = node

    def _remove_node(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    l = LRUCache(1)
    l.put(2, 1)
    # l.put(2,2)
    # l.get(1)
    # l.get(2)
    # l.put(4,4)
    l.get(2)
    l.put(3, 2)
    l.get(2)
    l.get(3)
    # l.get(4)
    # ["LRUCache", "put", "get", "put", "get", "get"]
    # [[1], [2, 1], [2], [3, 2], [2], [3]]
