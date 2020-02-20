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
    problem = Problem(n_books=B, n_libraries=L, n_days=D, scores=books_score)
    for l1, l2 in grouper(2, lines[2:]):
        library = Library(*[int(i) for i in l1.strip().split(" ")])
        books = [(int(i)) for i in l2.strip().split(" ")]
        all_books += books
        library.add_books(books)
        problem.add_library(library)
    return problem, all_books
