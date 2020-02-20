class Problem:
    def __init__(self, n_books, n_libraries, n_days, scores):
        self.n_books = n_books
        self.n_libraries = n_libraries
        self.n_days = n_days
        self.scores = scores
        self.libraries = []

    def add_library(self, library):
        self.libraries.append(library)
