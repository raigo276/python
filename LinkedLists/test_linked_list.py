import unittest

from linked_list import Element, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        # Test cases
        # Set up some Elements
        e1 = Element(1)
        e2 = Element(2)
        e3 = Element(3)
        e4 = Element(4)

        # Start setting up a LinkedList
        ll = LinkedList(e1)
        ll.append(e2)
        ll.append(e3)

        #Test get_position
        self.assertEqual(ll.get_position(3).value, 3)

        # Test insert
        ll.insert(e4, 3)
        self.assertEqual(ll.get_position(3).value, 4)

        # Test delete
        ll.delete(1)
        self.assertEqual(ll.get_position(1).value, 2)
        self.assertEqual(ll.get_position(2).value, 4)
        self.assertEqual(ll.get_position(3).value, 3)
unittest.main()