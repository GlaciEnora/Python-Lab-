class NotFound(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class DuplicateCustomer(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
class Customer:
    def __init__(self):
        self.custid = 0
        self.custname = ""
    
    def getinput(self):
        custid = int(input("Enter the customer id: "))
        if custid == self.custid:
            raise DuplicateCustomer("Customer Already Exists . . . ")
        else:
            self.custid = custid
        self.custname = input("Enter the customer name: ")
        
class Product:
    def __init__(self):
        self.prodcode = 0
        self.prodname = ""
        self.quan = 0
        self.ppi = 0

    def getinput(self):
        self.prodcode = int(input("Enter the product code: "))
        self.prodname = input("Enter the product name: ")
        self.quan = int(input("Enter the product amount: "))
        self.ppi = int(input("Enter the price per item: "))

    def remove(self, pid):
        if self.prodcode == pid:
            del self.prodcode
        else:
            raise NotFound("Product ID not found. . . ")

    def search(self, pid):
        if self.prodcode != pid:
            raise NotFound("Product ID not found. . . ")
        else:
            display()

    def display(self)
class Order(Customer, Product):
    def __init__(self):
        Customer.__init__(self)
        Product.__init__(self)
        self.totprice = 0
        
