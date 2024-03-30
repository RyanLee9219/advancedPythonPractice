import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')
    def test_do_stuff(self):
        '''HIIIIIIIIIIIII!'''
        test_pram = 10
        result = main.do_stuff(test_pram)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_pram = 'fdsjfkldf'
        result = main.do_stuff(test_pram)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_pram = None
        result = main.do_stuff(test_pram)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_pram = ''
        result = main.do_stuff(test_pram)
        self.assertEqual(result, 'please enter number')

    def tearDown(self):
        print('cleaning up')
if __name__ =='__main__':
    unittest.main()