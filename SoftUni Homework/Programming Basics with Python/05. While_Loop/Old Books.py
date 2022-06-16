favourite_book = input()
book_cnt = 0
book = input()

while book != "No More Books":
    if favourite_book == book:
        print(f"You checked {book_cnt} books and found it.")
        break
    book_cnt += 1
    book = input()

if book == "No More Books":
    print("The book you search is not here!\n"
          f"You checked {book_cnt} books.")
