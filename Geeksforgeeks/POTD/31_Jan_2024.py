# Your Python code here
"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    def insert(self, root, key):
        for char in key:
            nextNode = root.children[ord(char)-97]
            if not nextNode:
                newNode = TrieNode()
                root.children[ord(char)-97] = newNode
                root = newNode
            else:
                root = nextNode
        root.isEndOfWord = True

    def search(self, root, key):
        for char in key:
            nextNode = root.children[ord(char)-97]
            if not nextNode:
                return False
            else:
                root = nextNode
        return root.isEndOfWord is True