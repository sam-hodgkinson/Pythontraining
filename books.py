

books ={
"John Smith" : ["Hunger Games", "Hunger Games Catching Fire", "Hunger Games Mockingjay"],
"JK Rowling" : ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince"],
"Jane Austen" : ["Pride and Predjudice", "Sense and Sensibility"],
"Stephen King" : ["IT"]
}

author = input("Enter the name of the author: ")

key = books.keys
for key in books:
    authorname = input("Please enter autor name: ")
    if authorname == key:
        print(f"Book title {books[key]}")