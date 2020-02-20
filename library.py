import numpy as np


class Library:
    def __init__(self, n_books, days_to_sign, n_parallel_ship):
        self.n_books = n_books
        self.days_to_sign = days_to_sign
        self.n_parallel_ship = n_parallel_ship
        self.books = None

    def add_books(self, books_to_add):
        self.books = books_to_add

    @property
    def total_score(self):
        return sum(self.books)

    @property
    def total_days(self):
        return int(
            (self.days_to_sign + np.floor(self.n_books / self.n_parallel_ship))
            + (0 if self.n_books % self.n_parallel_ship == 0 else 1)
        )
