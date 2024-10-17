disk_mb = 1.44
disk_kb = disk_mb * 1024
disk_b = disk_kb * 1024
pages = 100
lines = 50
symbols_in_one_line = 25
total_symbols = pages * lines * symbols_in_one_line
one_book_size = total_symbols * 4
total_books =int(disk_b / one_book_size)
print("Количество книг, помещающихся на дискету:", total_books)