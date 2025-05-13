"""
Problem Statement:
You're developing an inventory management system for an online bookstore. 
Create a Python program that uses dictionaries to manage the book inventory 
and perform various operations.
Tasks:
	1.	Create a dictionary called book_inventory with the following initial books:
	▪	"Python Crash Course" with ISBN "978-1593279288", price $29.99, and 
	15 copies in stock
	▪	"Automate the Boring Stuff" with ISBN "978-1593279929", price $39.95, 
	and 10 copies in stock
	▪	"Fluent Python" with ISBN "978-1492056355", price $59.99, and 5 copies in stock
	2.	Write a function add_book(inventory, title, isbn, price, stock) 
	that adds a new book to the inventory.
	3.	Write a function update_stock(inventory, title, quantity) that updates 
	the stock quantity of a book. If the book doesn't exist, print an 
	appropriate error message.
	4.	Write a function get_total_inventory_value(inventory) that calculates 
	and returns the total value of all books in the inventory (price × stock 
	for each book).
	5.	Write a function find_books_in_range(inventory, min_price, max_price)
	that returns a list of book titles with prices within the specified range.
	6.	Write a function remove_out_of_stock(inventory) that removes all
	books with 0 stock from the inventory.
	7.	Demonstrate all the functions with appropriate test cases.

"""
import pprint
class DuplicateBookError(Exception):
    pass


book_inventory = [
    {
        "book_name": "Python Crash Course",
        "ISBN": "978-1593279288",
        "price": 29.99,
        "currency": "USD",
        "copies": 15
    },
    {
        "book_name": "Automate the Boring Stuff",
        "ISBN": "978-1593279929",
        "price": 39.95,
        "currency": "USD",
        "copies": 10
    },
    {
        "book_name": "Fluent Python",
        "ISBN": "978-1492056355",
        "price": 59.99,
        "currency": "USD",
        "copies": 5
    }
]

"""Write a function add_book(inventory, title, isbn, price, stock) that adds a new book to the inventory.
	that adds a new book to the inventory."""

def add_book(book_inventory, title, isbn, price, stock):
    for book in book_inventory:
        if book["book_name"] == title or book["ISBN"] == isbn:
            raise DuplicateBookError(f"Book with title '{title}' or ISBN '{isbn}' already exists.")

    new_book = {
        "book_name": title,
        "ISBN": isbn,
        "price": price,
        "currency": "USD",
        "copies": stock
    }
    book_inventory.append(new_book)
    return new_book

#pprint.pprint(book_inventory)
#add_book("Database", "978-1583279929", 19.99, 3)


"""Write a function update_stock(inventory, title, quantity) that updates the stock quantity of a book. 
If the book doesn't exist, print an appropriate error message."""

def update_stock(book_inventory, title, quantity):
    for updated_book in book_inventory:
        if updated_book["book_name"].lower() == title.lower():
            updated_book["copies"] = quantity
            return updated_book, "book found"
    return None, "The book does not exist. Please check the book name"
#update_stock("Database", 2)
#pprint.pprint(book_inventory)

"""Write a function get_total_inventory_value(inventory) 
that calculates and returns the total value of all books in the inventory (price × stock for each book)."""

def get_total_inventory_value(book_inventory):
    total = 0
    for book in book_inventory:
        total += book["price"] * book["copies"]
    return round(total, 2)

"""Write a function find_books_in_range(inventory, min_price, max_price) 
	that returns a list of book titles with prices within the specified range."""
def find_books_in_range(book_inventory, min_price, max_price):
    books_in_range = []
    for book in book_inventory:
        if min_price <= book["price"] <= max_price:
            books_in_range.append(book["book_name"])
    return books_in_range


"""Write a function remove_out_of_stock(inventory) that removes all
	books with 0 stock from the inventory."""
def remove_out_of_stock(book_inventory):
    return [book for book in book_inventory if book["copies"] > 0]


new_book = add_book(book_inventory, "Python", "1234", 10.99, 3)
print(new_book)



