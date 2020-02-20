class Problem:
    def __init__(self, n_books, n_libraries, n_days, scores):
        self.n_books = n_books
        self.n_libraries = n_libraries
        self.n_days = n_days
        self.scores = scores
        self.libraries = []
        self.scanned_books = set()

    def add_library(self, library):
        self.libraries.append(library)

    # def scan_library(self, i):
    def book_score(self, n_repetitions, book_value):
        return (1 - n_repetitions / self.n_libraries) * book_value
