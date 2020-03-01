import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        expected = 28.27431
        self.assertEqual(expected, task.computecirclearea(3))

    def test4(self):
        expected = 1, 0
        inputlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.assertEqual(expected, task.firstandlast(inputlist))

    def test5(self):
        expected = 365
        date1 = [10, 10, 2001]
        date2 = [10, 10, 2002]

        self.assertEqual(expected, task.timebetwdates(date1, date2))


if __name__ == '__main__':
    unittest.main()
