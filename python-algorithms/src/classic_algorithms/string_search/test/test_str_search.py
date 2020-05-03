from kmp_search import kmp_search
from naive_search import naive_search
from unittest import TestCase
from datetime import datetime
import random


class TestStrSearch(TestCase):

    def test_naive_search(self):
        self.assertEqual(4, naive_search('asdfbkfc', 'bkfc'))
        self.assertEqual(-1, naive_search('asdfasfa', 'fad'))
        self.assertEqual(4, naive_search('jsdfasfa', 'a'))
        self.assertEqual(-1, naive_search('jsdfasfa', 'ab'))

    def test_kmp_search(self):
        self.assertEqual(5, kmp_search('skgihboris', 'boris'))
        self.assertEqual(-1, kmp_search('skgihboris', 'borisa'))
        self.assertEqual(0, kmp_search('abdskgihboris', 'ab'))
        self.assertEqual(1, kmp_search('abdskgihboris', 'bds'))
        self.assertEqual(1, kmp_search('abdskgihboris', 'bdsk'))

    def test_time(self):
        search_str = ['a', 'b', 'c'] * 100000
        random.shuffle(search_str)
        search_str = ''.join(search_str)
        substrings = []
        for i in range(1, 10, 1):
            index = random.randint(50000, len(search_str) - 1000)
            substrings.append(search_str[index:index+(i*10)])
        for substring in substrings:
            initial_time = datetime.now()
            naive_search(search_str, substring)
            print(f'length: {len(substring)}')
            print(f'naive search: {(datetime.now() - initial_time).microseconds}')
            initial_time = datetime.now()
            kmp_search(search_str, substring)
            print(f'kmp search: {(datetime.now() - initial_time).microseconds}')


