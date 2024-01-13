from queue import Queue

# There are some other module for queue problem
from queue import PriorityQueue
from queue import LifoQueue
from queue import SimpleQueue

class Solution:
    def modifyQueue(self, q, k):
        # Create a temporary stack to store the first k elements
        stack = []
        
        u = Queue()
        
        for element in q:
            u.put(element)
        
        q=u
        
        # Dequeue the first k elements from the queue and push them onto the stack
        for _ in range(k):
            stack.append(q.get())
        
        # Pop the elements from the stack and enqueue them back into the queue
        while stack:
            q.put(stack.pop())
        
        # Dequeue the remaining elements from the queue and enqueue them back
        for _ in range(q.qsize() - k):
            q.put(q.get())
        
        # Convert the queue to a list for returning
        modified_queue = list(q.queue)
        
        return modified_queue
    

