class Book:
    def __init__(self, title, author, price, volume, stock):
        self.title = title
        self.author = author
        self.price = price
        self.volume = volume
        self.stock = stock
        
    def addBook(self, title, author, price, volume, stock):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Author must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(volume, int) or not volume.strip():
            raise ValueError("Volume must be a non-empty string.")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("Stock must be a non-negative integer.")
        
        print("BOOK ADDED!")
        return Book(title, author, price, volume, stock)

    def displayInfo(self, title, author, price, volume, stock):
        print(f"TITLE: {self.title}")
        print(f"AUTHOR: {self.author}")
        print(f"PRICE: ${self.price:.2f}")
        print(f"VOLUME: {self.volume}")
        print(f"STOCK: {self.stock}")

    def updateStock(self, newStock):
        if not isinstance(newStock, int) or newStock < 0:
            raise ValueError("Stock must be a non-negative integer.")
        
        self.stock = newStock
        print(f"{self.title} HAS {self.stock} UNITS AVAILABLE.")
