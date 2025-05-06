#from src.book_inventory.dict_book_inventory import add_book, book_inventory, update_stock

#from src.book_inventory import inventory
import src.book_inventory.inventory as inventory
import pytest

def test_add_book_success(inventory_data):
    title = "Database"
    isbn = "978-1583279929"
    price = 19.99
    stock = 3

    new_book = inventory.add_book(inventory_data, title, isbn, price, stock)
    assert new_book in inventory_data
    #print(book_inventory)


def test_add_existing_book(inventory_data):
    title = "Database"
    isbn = "978-1583279929"
    price = 19.99
    stock = 3
    inventory.add_book(inventory_data, title, isbn, price, stock)
    with pytest.raises(inventory.DuplicateBookError) as excinfo:
        inventory.add_book(inventory_data, title, isbn, price, stock)
    assert f"Book with title '{title}' or ISBN '{isbn}' already exists." in str(excinfo.value)

def test_update_stock_book_found():
    book_inventory = [{"book_name": "Database", "copies": 9}]
    title = "Database"
    quantity = 2
    updated_book, message = inventory.update_stock(book_inventory, title, quantity)
    assert updated_book is not None, f"Book '{title}' not found in stock!"
    assert updated_book["book_name"] == title
    assert updated_book["copies"] == quantity
    #print(book_inventory)


def test_total_inventory_value():
    book_inventory = [{"book_name": "Database", "copies": 10, "price": 29.99},
                      {"book_name": "Automate the Boring Stuff", "copies": 12, "price": 29.99},
                      {"book_name": "Fluent Python", "copies": 6, "price": 69.99},
                      {"book_name": "Python Crash Course", "copies": 4, "price": 59.99}
                      ]
    expected_total = round(sum(book["price"] * book["copies"] for book in book_inventory),2)
    inventory_value = inventory.get_total_inventory_value(book_inventory)
    assert inventory_value == expected_total
    #print(inventory_value)


def test_books_in_range():
    book_inventory = [{"book_name": "Database", "copies": 10, "price": 29.99},
                      {"book_name": "Automate the Boring Stuff", "copies": 12, "price": 29.99},
                      {"book_name": "Fluent Python", "copies": 6, "price": 69.99},
                      {"book_name": "Python Crash Course", "copies": 4, "price": 59.99}
                      ]
    min_price = 0
    max_price = 68.99
    expected_books_in_range = [book["book_name"] for book in book_inventory if min_price <= book["price"] <= max_price]
    books_in_range = inventory.find_books_in_range(book_inventory, min_price, max_price)
    assert books_in_range == expected_books_in_range
    #print(books_in_range)


def test_remove_out_of_stock():
    book_inventory = [{"book_name": "Database", "copies": 0, "price": 29.99},
                      {"book_name": "Automate the Boring Stuff", "copies": 7, "price": 29.99},
                      {"book_name": "Fluent Python", "copies": 0, "price": 69.99},
                      {"book_name": "Python Crash Course", "copies": 4, "price": 59.99}
                      ]
    expected_book_inventory = [book for book in book_inventory if book["copies"] > 0]
    in_stock_books = inventory.remove_out_of_stock(book_inventory)
    assert in_stock_books == expected_book_inventory
    #print(in_stock_books)