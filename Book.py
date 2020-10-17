#this is an OOP example
class Book():
    def __init__(self,author,title,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} in {self.pages} pages" 
    def __len__(self):
        return self.pages
myBook = Book("author","title",50)
len(myBook)
print(myBook)
