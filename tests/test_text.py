import unittest

from text.text import (remove_url, remove_emoticons, tokenize_text, 
                       untokenize_text, get_text_cloud, get_freq_dist_list)


class TestTextProcessing(unittest.TestCase):

    def setUp(self):
        self.text = "abcdefg"

    def test_remove_url(self):
        got = remove_url(['oh well whatever nevermind https://t.co/asd',
                          'come as you are www.nirvana.se'])
        expected = ['oh well whatever nevermind  ', 'come as you are  ']
        self.assertEqual(got, expected)

    def test_tokenize_text(self):
        got = tokenize_text(self.text)
        expected = [['a'], ['b'], ['c'],
                    ['d'], ['e'], ['f'],
                    ['g']
                    ]
        self.assertEqual(got, expected)

    def test_untokenize_text(self):
        got = untokenize_text(tokenize_text(self.text))
        expected = ['a ', 'b ', 'c ',
                    'd ', 'e ', 'f ',
                    'g '
                    ]
        self.assertEqual(got, expected)

    def test_get_text_cloud(self):
        got = get_text_cloud(tokenize_text(self.text))
        expected = "a b c d e f g "
        self.assertEqual(got, expected)

    def test_get_freq_dist_list(self):
        got = get_freq_dist_list(tokenize_text(self.text))
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.assertEqual(got, expected)

    def test_remove_emoticons(self):
        got = remove_emoticons("😁")
        expected = ['']
        self.assertEqual(got, expected)
