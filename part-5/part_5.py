### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def add_new_book(book_source):
    title = input("Please add the title to your book here: ")
    author = input("Please add the author to your book here: ")
    
    try:
        year = int(input("What year was the book published? "))
    except:
        year = int(input("Please enter a number? "))
    try:        
        rating = float(input("From 0 to 5, what would you rate this book? "))
    except:
        rating = float(input("Please enter a number? "))
    try:        
        pages = int(input("How many pages is in this book? "))
    except:
        pages = int(input("Please enter a number? "))    

    with open(book_source, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
        
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,  
        "pages": pages    
        }

    return book_dictionary

print(add_new_book())    
    

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def view_books(book_source):
    
    print("Here are all your books")
    
    with open(book_source, 'r') as f:
        file = f.readlines()
        
        for line in file:
            title, author, year, rating, pages = line.split(', ')
            
            print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def main_menu(books_source):
    
    active = True
    
    while active:
        options = input(" Select 1 to add your book. Select 2 to see all your books. Select 3 to exit.  ")
        
        if __name__ == "__main__":
            main_menu()
        elif options == "1": 
            books_source.append(add_new_book())
        elif options == "2": 
            print(books_source)    
        elif options == "3": 
            print("Exiting")
            active = False
        else:
            print("Please enter a number for one of the options.") 
        
            
main_menu()            

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_books = [
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown", 
        "year": 2003,
        "rating": 4.70,
        "pages": 489
    },
    
    {
        "title": "The Pillars of the Earth",
        "author": "Ken Follett", 
        "year": 1989,
        "rating": 4.60,
        "pages": 806 
    },
    
    {
         "title": "The Hardy Boys: Series",
        "author": "Frank W. Dixon", 
        "year": 1927-2005,
        "rating": 4.10,
        "pages": 48-100
    },
    
    {
         "title": "My Side of the Mountain",
        "author": "Jean Craighead George", 
        "year": 1959,
        "rating": 4.10,
        "pages": 177
    }
    
]

def book_parser(book_dictionary):
    
    book_string = f"{book_dictionary['author']} is the author of {book_dictionary['title']}. This book was published in {book_dictionary['year']}, it has a rating of {book_dictionary['rating']} stars, and is {book_dictionary['pages']} pages long."
    
    return book_string

print(book_parser(my_book))
    
def get_book_title(book_dictionary):
    book_title = book_dictionary["title"]
    return book_title

print(get_book_title(my_book))

def get_book_author(book_dictionary):  
    book_author = book_dictionary["author"] 
    return book_author

print(get_book_author(my_book))


def get_book_year(book_dictionary):
    book_year = book_dictionary["year"]
    return book_year

print(get_book_year(my_book))

def get_book_rating(book_dictionary):
    book_rating = book_dictionary["rating"]
    return book_rating

print(get_book_rating(my_book))

def get_book_pages(book_dictionary):
    book_pages = book_dictionary["pages"]
    return book_pages

print(get_book_pages(my_book))
    
def get_average_ratings(book_dictionary_list):
    average_rating = 0
    num_books = 4
    
    for book_dictionary in book_dictionary_list:   
        average_rating += book_dictionary["rating"]/ num_books
        
    return average_rating

print(get_average_ratings(my_books))    

def get_set_of_book_titles(book_dictionary_list):   
    book_title_set = set()
    
    for book_dictionary in book_dictionary_list: 
        book_title_set.add(book_dictionary["title"])
        
    return book_title_set

print(get_set_of_book_titles(my_books))   

def add_new_book(book_source):

    title = input("Please add the title to your book here: ")
    author = input("Please add the author to your book here: ")
    
    try:
        year = int(input("What year was the book published? "))
    except:
        year = int(input("Please enter a number? "))
    try:        
        rating = float(input("From 0 to 5, what would you rate this book? "))
    except:
        rating = float(input("Please enter a number? "))
    try:        
        pages = int(input("How many pages is in this book? "))
    except:
        pages = int(input("Please enter a number? "))    
    with open(book_source, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
        
    

   

print(add_new_book())

def main_menu(books_source):
    
    active = True
    
    while active:
        options = input(" Select 1 to add your book. Select 2 to see all your books. Select 3 to exit.  ")
        
        if options == "1": 
            books_source.append(add_new_book())
        elif options == "2": 
            print(books_source)    
        elif options == "3": 
            print("Exiting")
            active = False
        else:
            print("Please enter a number for one of the options.") 
            
main_menu("library.txt")            
         