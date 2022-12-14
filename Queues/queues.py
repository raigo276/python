"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)
        pass

    def peek(self):
        if len(self.storage) > 0:
            return self.storage[0]
        return None

    def dequeue(self):
        if len(self.storage) > 0:
            delete_element = self.storage[0]
            self.storage.remove(self.storage[0])        
            return delete_element
        return None
