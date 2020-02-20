import operator
from parser import read_input

import ipdb

fname = "b_read_on.txt"
problem, all_books, all_books_list = read_input(fname)
days_consumed = 0
while True:
    book_score = {}
    library_score = {}
    scanned_books = []
    scanned_libraries = []
    for library in problem.libraries:
        for book in library.books:
            if book in scanned_books:
                book_score[book] = 0
            else:
                book_value = all_books.get(book)
                book_score[book] = problem.book_score(all_books_list.count(book), book_value)
    print("Finish calculations")
    for library in problem.libraries:
        library_score[library] = library.total_score(book_score)
    selected_library = max(library_score, key=library_score.get)
    scanned_books.append(selected_library.books)
    days_consumed += selected_library.days_to_sign
    scanned_libraries.append((selected_library, selected_library.books))
    problem.libraries.remove(selected_library)
    print(f"{days_consumed/problem.n_days*100}%")
    if days_consumed > problem.n_days or len(scanned_libraries) == len(problem.libraries):
        break
print("WRITING TO FILE")
with open(f"out/{fname}", "w") as f:
    f.write(f"{len(scanned_libraries)}\n")
    for library, books in scanned_libraries:
        f.write(f"{library.i} {len(library.books)}\n")
        for book in library.books:
            f.write(f"{book} ")

        f.write("\n")
ipdb.set_trace()
