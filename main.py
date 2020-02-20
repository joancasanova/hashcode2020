from parser import read_input

import ipdb

book_score = {}
scanned_books = []
problem, all_books = read_input("a_example.txt")
for library in problem.libraries:
    for book in library.books:
        if book in scanned_books:
            book_score[book] = 0
        else:
            book_score[book] = problem.book_score(all_books.count(book), book)
for library in problem.libraries:
    print(library.total_score(book_score))
ipdb.set_trace()
