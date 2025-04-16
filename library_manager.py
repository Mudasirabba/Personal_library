import os
import json

LIBRARY_FILE = 'library.txt'

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

# Display menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == 'yes' else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    removed = False
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            removed = True
            print("Book removed successfully!")
            break
    if not removed:
        print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter the title: " if choice == '1' else "Enter the author: ")

    matches = []
    for book in library:
        if (choice == '1' and query.lower() in book['title'].lower()) or \
           (choice == '2' and query.lower() in book['author'].lower()):
            matches.append(book)

    if matches:
        print("Matching Books:")
        for idx, book in enumerate(matches, 1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display statistics
def display_statistics(library):
    total = len(library)
    read_books = sum(1 for book in library if book['read'])
    percent_read = (read_books / total * 100) if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

# Main program
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
