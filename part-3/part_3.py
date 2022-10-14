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

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(book_dictionary):
    
    book_string = f"{book_dictionary['author']} is the author of {book_dictionary['title']}. This book was published in {book_dictionary['year']}, it has a rating of {book_dictionary['rating']} stars, and is {book_dictionary['pages']} pages long."
    
    return book_string

print(book_parser(my_book))
    


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

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
    
    
    
# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

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

def get_title_author(book_dictionary_list):     
    
    for title, author in book_dictionary_list: 
        
   
    
print(get_title_author(my_books))    
       
