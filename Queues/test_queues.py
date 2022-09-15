import unittest

from queues import Queue

class TestQueues(unittest.TestCase):
    def test_queues(self):
        # Setup
        q = Queue(1)
        q.enqueue(2)
        q.enqueue(3)

        # Test peek
        self.assertEqual(q.peek(), 1)

        # Test dequeue
        self.assertEqual(q.dequeue(), 1)

        # Test enqueue
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)

        # Test peek
        q.enqueue(5)
        self.assertEqual(q.peek(), 5)

unittest.main()
