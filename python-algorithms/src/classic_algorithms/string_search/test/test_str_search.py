from kmp_search import kmp_search
from naive_search import naive_search
from bm_search import bm_search
from rk_search import rk_search
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
        with open('../data/data.txt', 'r') as file:
            text = file.read()
            patterns = [
                'как бы черта, отделяющая живых от мертвых',
                'кость, и двадцатидвухлетний безупречный генерал',
                'тебя так; разумеется, что я тебе говорю, есть единственно',
                'духовные лица и причетники, люди (прислуга) тоже'
            ]
            search_functions = [naive_search, kmp_search, bm_search, rk_search]
            for pattern in patterns:
                results = []
                for search in search_functions:
                    start_time = datetime.now()
                    results.append(search(text, pattern))
                    print(f'Phrase="{pattern}" algo="{search.__name__}" time={(datetime.now()-start_time).microseconds}')
                assert all(result == results[0] for result in results)





