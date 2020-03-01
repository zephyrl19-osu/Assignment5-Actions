import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def circleTest(self):
        expected = 28.27431
        self.assertEqual(expected, task.computecirclearea(3))

    def listTest(self):
        expected = 1, 0
        inputlist = [1, 4, 5, 6, 7, 8, 9, 0]
        self.assertEqual(expected, task.returnfirstandlast(inputlist))


if __name__ == '__main__':
    unittest.main()
