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
        self.custid = int(input("Enter the customer id: "))
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

    def search(self, pid):
        if self.prodcode == pid:
            return self.display()
        else:
            raise NotFound("Product ID not found. . . ")

    def display(self):
        print(f"Product Code: {self.prodcode}")
        print(f"Product Name: {self.prodname}")
        print(f"Product Amount: {self.quan}")
        print(f"Price per Item: {self.ppi}")

class Order(Customer, Product):
    def __init__(self):
        Customer.__init__(self)
        Product.__init__(self)
        self.totprice = 0
        self.products_ordered = []  # A list to store products in the order.

    def create_order(self):
        try:
            self.getinput()
        except DuplicateCustomer as e:
            print(e)
        except Exception as e:
            print(e)

    def remove(self, pid):
        try:
            flag = 0
            for item in self.products_ordered:
                if item.prodcode == pid:
                    flag == 1
                    self.products_ordered.remove(item)
            if not flag:
                raise NotFound("Product does not exist")
        except NotFound as e:
            print(e)
        
    def add_product_to_order(self, product):
        self.products_ordered.append(product)

    def calculate_total_price(self):
        total_price = 0
        for product in self.products_ordered:
            total_price += product.quan * product.ppi
        self.totprice = total_price
        return total_price


