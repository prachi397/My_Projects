#_______________________________________________________________________LIBRARY MANAGEMENT SYSTEM________________________________________________________________________
"""create a libraray class
define some methods -->
1)to display all books -> display_book
2)to lend any book -> lend_book -> who owns the book if not present in the library
3)to donate book in library -> add_book() 
4)to return the book -> return book

Purpose --> I want to make a library to use this class
HarryLibrary = Library(listofbooks, library_name) ->constructor
you can maintane a dictionary(books: nameofperson)
create a main function and run an infinite while loop asking users for their input
"""

class Library():
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}  #it is empty dictionary which stores the info that who took which book

    def display_book(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Book dictionary for lend the book has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def add_book(self, book):
        self.bookList.append(book)
        print("Book has been added to the booklist")
    
    def return_book(self, book):
        self.lendDict.pop(book)
       
if __name__ == '__main__':
    prachi = Library(["Python", "Rich Dad Poor Dad", "Harry Potter", "c++ basics", "Algorithm"], "Prachi'sLibrary")

    while(True):
        print(f"Welcome to the {prachi.name} library. Enter yur choice to continue:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            prachi.display_book()
            
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            prachi.lend_book(user, book)
            
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            prachi.add_book(book)

            
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            prachi.return_book(book)

            
        else:
            print("Not a valid option")

        print("press q to quit and c to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
               
            elif user_choice2 == "c":
                continue

            
      

        








    
