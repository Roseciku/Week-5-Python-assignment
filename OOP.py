#Assignment 1
#creating a class and adding attributes and methods
class Book:
    genre = ""

    def read(self):
        print("Reading the book")

#creating an object
my_book =Book()
my_book.genre = "fiction"
print(my_book.genre)

my_book.read()

#Use constructors to initialize each object with unique values.

class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        
    #Method to display book details
    def display_info(self):
        print(f"Title:{self.title}, Author: {self.author}")

#Creating objects with unique attributes
book1 = Book("Angel", "Rosemary Wanjiku")
book2 = Book("To kill", "Mark Harper")

print(book1.author)
print(book2.title)

#Adding inheritance layer to explore polymorphism  
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size #additional attribute

    # Overriding the display_info method to include file size
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, File Size: {self.file_size}MB")

#Creating an EBook oject
ebook = EBook("1984", "George Orwell", 26)

# Displaying information to demonstrate polymorphism
ebook.display_info() 

#Assignment 2:
# Defining the base class
class Vehicle:
    def move(self):
        pass  # This will be overridden in derived classes

# Defining the Car class inheriting from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving")

# Defining the Plane class inheriting from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Defining the Boat class inheriting from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Creating objects of each class
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
vehicles = [car, plane, boat]
for vehicle in vehicles:
    vehicle.move()

