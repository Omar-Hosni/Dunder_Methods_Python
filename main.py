class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return self.title + ' written by ' + self.author

    def __len__(self):
        return 'the length of book is is ' + str(self.pages)

    def __del__(self):
        print("A book object has been deleted")

b = Book('Python rocks', 'Jose', 200)
print(b.__str__())
print(b.__len__())
del b # this is equal to b.__del__()
