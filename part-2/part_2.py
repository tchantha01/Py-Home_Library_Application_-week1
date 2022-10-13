### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['Dan Brown', 'Ken Follett', 'J.K. Rowling', 'Frank W. Dixon', 'Jean Craighead George', 'R.L.Stine', 'Steven King']
# print(my_authors)
# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append('H.G. Wells')
# Example: my_authors.append("H.G. Wells")
# print(my_authors)

# Now let's remove an element in the list

my_authors.remove('H.G. Wells')
# Example: my_authors.remove("H.G. Wells")
# print(my_authors)

# Now access an element by it's index. (Remember it indexes start at 0.)

my_authors[4]
# Example: my_authors[2]
# print(my_authors[4])

# Now slice the list.

my_authors[2:6]
# Example: my_authors[1:4]
# print(my_authors[2:6])

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

my_author_tuple = ('Dan Brown', 'Ken Follett', 'J.K. Rowling', 'Frank W. Dixon', 'Jean Craighead George', 'R.L.Stine', 'Steven King')
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
# print(my_author_tuple)

### Step 3 - Sets ###

# Create a set with your authors.

my_author_set = {'Dan Brown', 'Ken Follett', 'J.K. Rowling', 'Frank W. Dixon', 'Jean Craighead George', 'R.L.Stine', 'Steven King'}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
# print(my_author_set)

# Add a new author to your set.

my_author_set.add('J.R.R. Tolkien')
# Example: my_author_set.add("J.R.R. Tolkien")
# print(my_author_set)

# Try adding the same author again, and be sure to print your set.

my_author_set.add('J.R.R. Tolkien')
# Example: my_author_set.add("J.R.R. Tolkien")
# print(my_author_set)




### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

for book in my_authors:
    print(book)
    
for book in my_author_set:
    print(book)
    
for book in my_author_tuple:
    print(book)        
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

