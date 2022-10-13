my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
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




# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below