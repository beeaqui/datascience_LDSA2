class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = price
        
    def get_book_info(self):
        print("Title: " + str(self.title) + ", Author: " + str(self.author) + ", Price: " + str(self.price))
        return "Title: " + str(self.title) + ", Author: " + str(self.author) + ", Price: " + str(self.price)

    
def get_total_price(book_list):
    total_price = 0

    for book in book_list:
        total_price += book[2]
    return total_price
    
description = "this is a module named bookstore"