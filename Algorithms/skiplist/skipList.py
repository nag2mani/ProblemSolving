import random


class SkipNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
        self.below = None
        self.above = None


class SkipList:
    def __init__(self):
        self.head = SkipNode(float("-inf"))
        self.tail = SkipNode(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def search(self, value):
        curr = self.head
        while curr:
            if curr.next.value == value:
                return curr.next
            elif curr.next.value > value:
                curr = curr.below
            else:
                curr = curr.next
        return None

    def insert(self, value):
        prev_nodes = []
        curr = self.head
        while curr:
            if curr.next.value > value:
                prev_nodes.append(curr)
                curr = curr.below
            else:
                curr = curr.next
        prev_node = prev_nodes.pop()
        node = SkipNode(value)
        node.prev = prev_node
        node.next = prev_node.next
        prev_node.next.prev = node
        prev_node.next = node
        self._add_upwards(node, prev_nodes)


    def _add_upwards(self, node, prev_nodes):
        while random.random() < 0.5 and prev_nodes:
            prev_node = prev_nodes.pop()
            above_node = SkipNode(node.value)
            above_node.below = node
            node.above = above_node
            above_node.next = prev_node.next.above
            above_node.prev = prev_node.next.above.prev
            prev_node.next.above.prev.above = above_node
            prev_node.next.above = above_node
            node = above_node


    def delete(self, value):
        node = self.search(value)
        if not node:
            return False

        while node:
            node.prev.next = node.next
            node.next.prev = node.prev
            node = node.above
        return True

    def display(self):
        curr_level = self.head
        while curr_level:
            curr_node = curr_level.next
            while curr_node != self.tail:
                print(curr_node.value, end=" ")
                curr_node = curr_node.next
            print()
            curr_level = curr_level.below

# Example usage:
skip_list = SkipList()
skip_list.insert(3)
skip_list.insert(6)
skip_list.insert(7)
skip_list.insert(9)
skip_list.insert(12)
skip_list.display()

print("Searching for 7:", skip_list.search(70).value)
print("Deleting 7")
skip_list.delete(7)
skip_list.display()
