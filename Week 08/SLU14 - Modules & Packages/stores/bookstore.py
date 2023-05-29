class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = float(price)
        
    def get_book_info(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Price: " + self.price + "."

    def get_total_price(self, book_list):
        total_price = 0
    
        for book in book_list:
            total_price += self.price
        print(total_price)
    
    description = "this is a module named bookstore"
    
if __name__ == "__main__":
    Book = [
        ("To Kill a Mockingbird", "Harper Lee", 2),
        ("The Great Gatsby", "F. Scott Fitzgerald", 5),
        ("Pride and Prejudice", "Jane Austen", 7),
        ("The Catcher in the Rye", "J.D. Salinger", 6),
        ("1984", "George Orwell", 15)
    ]
    
    print(get_total_price())
    print(get_book_info())