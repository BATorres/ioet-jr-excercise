from index import *
import unittest

example_one_dir = 'files\example.txt'
example_two_dir = 'files\example2.txt'

class TestIndex(unittest.TestCase):
    def test_example(self):
        self.assertAlmostEqual(read_file(os.path.join(script_dir, example_one_dir)), 'RENE-ASTRID: 2\nRENE-ANDRES: 2\nASTRID-ANDRES: 3\n')

    def test_example2(self):
        self.assertAlmostEqual(read_file(os.path.join(script_dir, example_two_dir)), 'RENE-ASTRID: 3\n')
