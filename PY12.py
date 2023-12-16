'''
Luis Sandoval
'''

import sqlite3

# Connect
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Task a
cursor.execute("SELECT last FROM authors ORDER BY last DESC")
authors_last_names = cursor.fetchall()
print("Authors' Last Names (Descending Order):")
for last_name in authors_last_names:
    print(last_name[0])

# Task b
cursor.execute("SELECT title FROM titles ORDER BY title ASC")
book_titles = cursor.fetchall()
print("\nBook Titles (Ascending Order):")
for title in book_titles:
    print(title[0])

# Task c
author_name = "Wald"
cursor.execute("""
    SELECT titles.title, titles.copyright, titles.ISBN
    FROM titles
    INNER JOIN author_ISBN ON titles.ISBN = author_ISBN.isbn
    INNER JOIN authors ON author_ISBN.id = authors.id
    WHERE authors.last = ? 
    ORDER BY titles.title ASC
""", (author_name,))
author_books = cursor.fetchall()
print(f"\nBooks by {author_name} (Alphabetically by Title):")
for book in author_books:
    print(f"Title: {book[0]}, Copyright: {book[1]}, ISBN: {book[2]}")

# Task d
new_author = ("Luis", "Sandoval")
cursor.execute("INSERT INTO authors (first, last) VALUES (?, ?)", new_author)
conn.commit()
print(f"\nNew author {new_author[0]} {new_author[1]} added to the authors table.")

# Task e
new_title = ("Python Experts", 2023, "123456")
cursor.execute("INSERT INTO titles (isbn, title, edition, copyright) VALUES (?, ?, ?, ?)", (new_title[2], new_title[0], 1, new_title[1]))
cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES ((SELECT id FROM authors WHERE first = ? AND last = ?), ?)", (new_author[0], new_author[1], new_title[2]))
conn.commit()
print(f"\nNew title '{new_title[0]}' added to the titles table.")

conn.close()

