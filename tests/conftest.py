import pytest

@pytest.fixture
def inventory_data():
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
        }
    ]
    return book_inventory
