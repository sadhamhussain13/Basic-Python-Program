class Library():
    def __init__(self,list):
        self.books_list = list
        self.available_books_list = list[:]
        self.books_lent = {}  #key-book value-user

    def display_available_books(self):
        for book in self.available_books_list:
            print (book)

    def display_all_books(self):
        for book in self.books_list:
            print (book)

    def display_borrow_books(self,name,book):
        if book not in self.books_list:
            print("Incorrect Book name.please check book list\n")
            return
        if book in self.available_books_list:
            self.books_lent.update({book:name})  #update book in dict
            self.available_books_list.remove(book)
            print("Now you can take the book\n")
        else:
            print("The book is already taken by",self.books_lent[book],'\n')

    def display_return_books(self,book):
        del self.books_lent[book]
        self.available_books_list.append(book)

if __name__=="__main__":
    lib = Library(["The Life Divine", "Da Vinci Code", "The Alchemist", "Educated", "Harry Potter",'\n'])
    while True:
        print("1.Display available books")
        print("2.Display all books ")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Quit\n")
        user_choice = int(input())
        if user_choice == 1 :
            lib.display_available_books()
        elif user_choice == 2 :
            lib.display_all_books()
        elif user_choice == 3 :
            name = input("Enter User name: ")
            book = input("Enter Book Name: ")
            lib.display_borrow_books(name,book)
        elif user_choice == 4 :
            book = input("Enter Book Name: ")
            lib.display_return_books(book)
        elif user_choice == 5 :
            break
        else:
            print("Invalid Choice")