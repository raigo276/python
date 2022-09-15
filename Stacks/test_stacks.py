import unittest

from stacks import LinkedList, Stack, Element

class TestStacks(unittest.TestCase):
    def test_stacks(self):
        # Test cases
        # Set up some Elements
        e1 = Element(1)
        e2 = Element(2)
        e3 = Element(3)
        e4 = Element(4)

        # Start setting up a Stack
        stack = Stack(e1)
        self.assertEqual(stack.ll.head.value, 1)
        # Test stack functionality push
        stack.push(e2)
        self.assertEqual(stack.ll.head.value, 2)
        stack.push(e3)
        self.assertEqual(stack.ll.head.value, 3)

        # Test stack functionality pop        
        self.assertEqual(stack.pop().value, 3)
        self.assertEqual(stack.pop().value, 2)
        self.assertEqual(stack.pop().value, 1)
        self.assertEqual(stack.pop(), None)
        
        stack.push(e4)
        self.assertEqual(stack.pop().value, 4)
        


unittest.main()