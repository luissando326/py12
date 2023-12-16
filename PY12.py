import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Task a: Select all authors’ last names in descending order
cursor.execute("SELECT last FROM authors ORDER BY last DESC")
authors_last_names = cursor.fetchall()
print("Authors' Last Names (Descending Order):")
for last_name in authors_last_names:
    print(last_name[0])

# Task b: Select all book titles in ascending order
cursor.execute("SELECT title FROM titles ORDER BY title ASC")
book_titles = cursor.fetchall()
print("\nBook Titles (Ascending Order):")
for title in book_titles:
    print(title[0])

# Task c: INNER JOIN to select books for a specific author
author_name = "Author's Name"  # Replace with the desired author's name
cursor.execute("""
    SELECT titles.title, titles.copyright, titles.ISBN
    FROM titles
    INNER JOIN author_ISBN ON titles.ISBN = author_ISBN.ISBN
    INNER JOIN authors ON author_ISBN.author_id = authors.author_id
    WHERE authors.last = ? 
    ORDER BY titles.title ASC
""", (author_name,))
author_books = cursor.fetchall()
print(f"\nBooks by {author_name} (Alphabetically by Title):")
for book in author_books:
    print(f"Title: {book[0]}, Copyright: {book[1]}, ISBN: {book[2]}")

# Task d: Insert a new author into the authors table
new_author = ("New Author's First Name", "New Author's Last Name")
cursor.execute("INSERT INTO authors (first, last) VALUES (?, ?)", new_author)
conn.commit()
print(f"\nNew author {new_author[0]} {new_author[1]} added to the authors table.")

# Task e: Insert a new title for an author
new_title = ("New Book Title", 2023, "New Book ISBN")
cursor.execute("INSERT INTO titles (title, copyright, ISBN) VALUES (?, ?, ?)", new_title)
conn.commit()
print(f"\nNew title '{new_title[0]}' added to the titles table.")

# Close the database connection
conn.close()
