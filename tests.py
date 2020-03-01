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




if __name__ == '__main__':
    unittest.main()
