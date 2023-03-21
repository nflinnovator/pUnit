import unittest

from main.python.WasRun import WasRun

class TestStringMethods(unittest.TestCase):

    def test_wasrun():
        test = WasRun("testMethod")
        print(test.wasRun)
        test.testMethod()
        print(test.wasRun)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()