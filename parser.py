from itertools import zip_longest

from book import Book
from library import Library
from problem import Problem


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def read_input(fname):
    with open(f"data/{fname}") as f:
        lines = f.readlines()
    metadata = lines[0].split(" ")
    B = int(metadata[0])
    L = int(metadata[1])
    D = int(metadata[2])
    all_books = []
    books_score = [int(i) for i in lines[1].strip().split(" ")]
    all_books = {i: books_score[i] for i in range(len(books_score))}
    all_books_list = []
    problem = Problem(n_books=B, n_libraries=L, n_days=D, scores=books_score)
    for i, group in enumerate(grouper(2, lines[2:])):
        l1, l2 = group[0], group[1]
        if l2 is None:
            break
        try:
            library = Library(i, *[int(i) for i in l1.strip().split(" ")])
        except Exception:
            import ipdb

            ipdb.set_trace()
        books = [(int(i)) for i in l2.strip().split(" ")]
        all_books_list.append(books)
        library.add_books(books)
        problem.add_library(library)
    return problem, all_books, all_books_list
