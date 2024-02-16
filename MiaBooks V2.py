import pandas as pd

class Library():
    
    df  = pd.DataFrame()
    def __init__(self):
        self.filename = "books.txt"
        self.file = open(self.filename, 'a+')
        self.df  = pd.read_csv("books.txt", sep=",", names=["TITLE", "AUTHOR", "RELEASE_YEAR", "PAGES"]) #    
        
    def __del__(self):
        self.df.to_csv("books.txt",index=False,header =False)
        
    def list_book(self):
        if len(self.df) > 0:
            print(self.df.drop(columns=["RELEASE_YEAR","PAGES"]))
        else:
            print("Library is empty.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")

        new_row = {'TITLE': title, 
                   'AUTHOR': author, 
                   'RELEASE_YEAR': release_year, 
                   'PAGES': pages}
        
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        
        print(f"Book '{title}' added successfully.")
        
    def remove_book(self):
        title = input("Enter book title: ")
        self.df.drop(self.df[self.df['TITLE'] == title].index, inplace = True)
        print(f"Book '{title}' removed successfully.")

lib = Library()

user_exit = 0

while user_exit == 0:
    print("\n")
    print("Please choose an action from the menu.")
    print("MENU")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("0) Exit")

    try:
        secim = int(input())
        print("\n")
        if secim == 1:
            print("*******************************************************")
            lib.list_book()
            print("*******************************************************")
        
        if secim == 2:
            lib.add_book()
            
        if secim == 3:
            lib.remove_book()
        
        if secim == 0:
            print("Are you sure?[Y/N]")
            secim_2 = input()
            if secim_2.lower() == 'y':
                del lib
                user_exit = 1
                
    except ValueError:
        print("Please choose an action from the menu!")
    