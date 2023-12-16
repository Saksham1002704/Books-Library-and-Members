class Library:
    List_books=[]
    List_Members=[]

    def add_book(self):
        a=input("Enter name of book to Add:  ")
        self.List_books.append(a)
    def remove_book(self):
        a= input("Enter name of book to Remove: ")
        self.List_books.remove(a)
    def add_mem(self):
        a= input("Enter name of member to Add: ")
        self.List_Members.append(a)
    def remove_mem(self):
        a= input("Enter name of member to Remove: " )
        self.List_Members.remove(a)
    def checkout_book(self):
        a= input("Enter name of book to Lend: " )
        self.List_books.remove(a)
    def return_book(self):
        a= input("Enter name of book to Return: " )
        self.List_books.append(a)
    def all_books(self):
        print("Books List  : " )
        for i in self.List_books:
            print(i)
Lib= Library()
while True:
    a= int(input("""
    1.Add Book
    2.Remove Book
    3.Checkout Book
    4.Return Book
    5.All Books
    6.Add Member 
    7.Remove Member
    8.Exit Loop
    """))
    if a==1:
        Lib.add_book()
    elif a==2:
        Lib.remove_book()
    elif a==3:
        Lib.checkout_book()
    elif a==4:
        Lib.return_book()
    elif a==5:
        Lib.all_books()
    elif a==6:
        Lib.add_mem()
    elif a==7:
        Lib.remove_mem()
    else:
        break