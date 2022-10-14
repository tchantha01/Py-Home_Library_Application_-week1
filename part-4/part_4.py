### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

def add_new_book():
    
    title = input("Please add the title to your book here: ")
    author = input("Please add the author to your book here: ")
    year    = input("What year was the book published? ")
    rating = input("From 0 to 5, what would you rate this book? ")
    pages = input("HOw many pages is in this book? ")
    
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,  
        "pages": pages    
        }

    return book_dictionary

print(add_new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

title = input("Please add the title to your book here: ")
author = input("Please add the author to your book here: ")
year = int(input("What year was the book published? "))
rating = float(input("From 0 to 5, what would you rate this book? "))
pages = int(input("How many pages is in this book? "))
        


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

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



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

books_source = [
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

def main_menu(books_source):
    
    options = input("Select 1 to add your book. Select 2 to see all your books. Select 3 to exit.  ")
    
    if options == "1": 
        books_source.append(add_new_book())
    elif options == "2": 
        print(books_source)    
    elif options == "3": 
        print("Exiting")
    else:
        print("Please enter a number for one of the options.")        
        
main_menu()    
# print(books_source)

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

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
            
main_menu()            
         