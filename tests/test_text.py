import unittest
from NLP.text.text import TextProcess as tp


class TestTextProcessing(unittest.TestCase):

    def setUp(self):
        self.text = "abcdefg"

    def test_remove_url(self):
        got = tp.remove_url(['oh well whatever nevermind https://t.co/asd',
                             'come as you are www.nirvana.se'])
        expected = ['oh well whatever nevermind  ', 'come as you are  ']
        self.assertEqual(got, expected)

    def test_tokenize_text(self):
        got = tp.tokenize_text(self.text)
        expected = [['a'], ['b'], ['c'],
                    ['d'], ['e'], ['f'],
                    ['g']
                    ]
        self.assertEqual(got, expected)

    def test_untokenize_text(self):
        got = tp.untokenize_text(tp.tokenize_text(self.text))
        expected = ['a ', 'b ', 'c ',
                    'd ', 'e ', 'f ',
                    'g '
                    ]
        self.assertEqual(got, expected)

    def test_get_text_cloud(self):
        got = tp.get_text_cloud(tp.tokenize_text(self.text))
        expected = "a b c d e f g "
        self.assertEqual(got, expected)

    def test_get_freq_dist_list(self):
        got = tp.get_freq_dist_list(tp.tokenize_text(self.text))
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.assertEqual(got, expected)

    def test_remove_emoticons(self):
        got = tp.remove_emoticons("😁")
        expected = ['']
        self.assertEqual(got, expected)
