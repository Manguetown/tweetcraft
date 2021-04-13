import unittest

from text.text import remove_emoticons

class TestTextProcessing(unittest.TestCase):

    def test_remove_emoticons(self):
        self.assertEqual(remove_emoticons("😁"), [''])
