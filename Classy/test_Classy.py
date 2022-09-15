import unittest

from module_Classy import Classy

class TestClassy(unittest.TestCase):
    def test_getClassiness(self):
        me = Classy()      
        print(me.show_excitement())
        self.assertEqual(me.getClassiness(), 0)
        me.addItem("tophat")
        self.assertEqual(me.getClassiness(), 2)
        me.addItem("bowtie")
        me.addItem("jacket")
        me.addItem("monocle")
        self.assertEqual(me.getClassiness(), 11)
        me.addItem("bowtie")
        self.assertEqual(me.getClassiness(), 15)

unittest.main()