def add(lis):
    title = input("Enter the book title: ")
    for item in lis:
        if title in item:
            cnt = int(input("Enter number of books"))
            item[4] += cnt
            break
    else:
        print("Title not found in the list...")
        new_book = []
        new_book.append(input("Enter the author of the book: "))
        new_book.append(title)
        new_book.append(int(input("Enter the price of the book: ")))
        new_book.append(input("Enter the name of the publisher: "))
        new_book.append(int(input("Enter the current number of books: ")))
        lis.append(new_book)
    
def display(lis):
    print(book, end='\n')

def remove(lis):
    title = input("Enter the title to remove: ")
    for item in lis:
        if title in item:
            cnt = int(input("Enter number of books to remove: "))
            item[4] -= cnt
            break
    else:
        print("Title not found in the list...")
        return

def delete(lis):
    title = input("Enter the title to delete: ")
    for item in lis:
        if title in item:
            del lis[lis.index(item)]
            break
    else:
        print("Title not found in the list...")
        return

book = []
while (True):
    choice = input("Enter the operation to perform: ")
    if choice.lower() == "add":
        add(book)
    elif choice.lower() == "display":
        display(book)
    elif choice.lower() == "remove":
        remove(book)
    elif choice.lower() == "delete":
        delete(book)
    else:
        break
