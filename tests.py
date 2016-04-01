import unittest
import josephus


class TestJosephus(unittest.TestCase):

    def testForOne(self):
        print 
        print "Testing for One"
        self.assertEqual(josephus.find_survivor(1), 0)

    def testForFirstCircular(self):
        print 
        print "Test for first number completing cycle"
        self.assertEqual(josephus.find_survivor(3), 2)

    def testForManuallyChecked(self):
        print 
        print "Test for some randomly checked conditions"
        print "For 5:"
        self.assertEqual(josephus.find_survivor(5), 2)
        print "For 6:"
        self.assertEqual(josephus.find_survivor(6), 4)
        print "For 7:"
        self.assertEqual(josephus.find_survivor(7), 6)


if __name__ == '__main__':
    unittest.main()