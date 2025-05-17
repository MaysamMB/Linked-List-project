class Brand :
    
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.prev = None
        self.point = None

class Model :

    def __init__(self, model_name, year, price):
        self.model_Name = model_name
        self.year = year
        self.price = price
        self.next = None
        

class List :

    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self) :
        if self.head == None :
            return True
        return False
    
    def add_Brand(self, value) :
        new_brand = Brand(value)
        if self.head == None :
            self.head = new_brand
            self.tail = new_brand
        else :
            self.tail.next = new_brand
            new_brand.prev = self.tail
            self.tail = new_brand
        print("Brand Added successfully :)")

    def pop_back(self) :
        A = self.tail.prev
        A.next = None
        self.tail.prev = None
        self.tail = A

    def pop_front(self) :
        A = self.head.next
        A.prev = None
        self.head.next = None
        self.head = A

    def remove_Brand(self, value) :
        if self.Search_ForABrand(value) == False :
            print("This brand not exist !") 
            return
        if self.head == None:
            return
        cur = self.head
        if self.head == self.tail :
            self.head = None
            self.tail = None
        elif self.head.value == value :
            self.pop_front()
        elif self.tail.value == value :
             self.pop_back()
        elif self.tail.prev.value == value :
            A = self.tail.prev
            C = A.prev
            A.prev = None 
            C.next = self.tail
            A.next = None
            self.tail.prev = C
        else :
            while cur.value != value :
                cur = cur.next
            t = cur.prev
            t2 = cur.next 
            cur.prev = None
            cur.next = None
            t2.prev = t
            t.next = t2
            cur = t2
        print('Brand deleted successfully :)')

    def Print_Brands(self):
        if self.head == None :
            print("There is no brand :< " )
            return
        cur = self.head
        print("All brands and model : ")
        while cur != None :
            if cur.point != None :
                temp = cur.point
                print("_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
                print(f"The Models of {cur.value} Brand is :")
                while temp != None :
                    print(f"Model name is : {temp.model_Name} Year : {temp.year} Price : {temp.price}")
                    temp = temp.next
                print("_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
            else :
                print(f'There is no modle for this brand ({cur.value}) :(')
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            cur = cur.next

    def add_CarModel(self, brand, name, year, price) :
        new_model = Model(name, year, price)
        cur = self.Brand_Exist(brand)
        if cur.point == None :
            cur.point = new_model
        else :
            temp = cur.point
            while temp.next != None :
                temp = temp.next
            temp.next = new_model
        print("Model added successfully :)")

    def print_Model(self, brand) :
        print(f"Models of Brand {brand} is : ")
        cur = self.Brand_Exist(brand)
        if cur.point == None :
            print(f'There is no model for this brand ({brand}) :(')
            return
        temp = cur.point
        while temp != None :
            print(f"Model name is : {temp.model_Name} Year : {temp.year} Price : {temp.price}")
            temp = temp.next

    def remove_CarModel(self, brand, model) :
        cur = self.Model_Exist(brand, model) #بترجعلي موقع النود
        ugly_search = self.Brand_Exist(brand) #بترجعلبي موقع البراند 
        A = ugly_search.point.next 
        print(A.model_Name)
        if ugly_search.point.model_Name == model :
            print("yes")
            ugly_search.point = A
            return
        pointer = ugly_search.point
        temp = pointer
        while pointer.model_Name != cur.model_Name :
            temp = pointer 
            pointer = pointer.next
        A = cur.next
        temp.next = A
        cur.next = None

    def Brand_Exist(self, brand) :
        cur = self.head 
        while cur.value != brand :
            cur = cur.next
        return cur
    
    def Search_ForABrand(self, brand) :
        cur = self.head 
        while cur != None :
            if cur.value == brand :
                return True
            cur = cur.next
        return False
    
    def Model_Exist(self, brand, model) :
        cur = self.Brand_Exist(brand)
        temp = cur.point
        while temp != None:
            if temp.model_Name != model :
                temp = temp.next
            else :
                return temp
        print(f"Model {model} not found on brand {brand} :(")

    def Search_ForAModel(self, brand, model) :
        cur = self.Brand_Exist(brand)
        temp = cur.point
        while temp != None:
            if temp.model_Name != model :
                temp = temp.next
            else :
                return True
        return False


def menu() :
    print("'__________Car Brands & Model__________'")
    print("1. Add a new car brand. ")
    print("2. Remove an existing car brand. ")
    print("3. Display all car brands along with their car models. ")
    print("4. Add a car model to a specific brand. ")
    print("5. Remove a car model from a specific brand. ")
    print("6. Display all models for a specific brand. ")
    print("7. Search for a car brand. ")
    print("8. Search for a specific car model within a brand. ")
    print('9. Save to File. ')
    print('10. Read from a file. ')
    print("11. Exit. ")


brand = List()
menu()
choice = 0
while choice != 11 :
    choice = int(input("Enter your choice : "))
    if choice == 1 :
        B = input("Please enter brand name : ")
        brand.add_Brand(B)
    elif choice == 2 :
        if brand.empty() :
            print("There is no brand yet :< ")
        else :
            B = input("Please enter name of brand you want delete : ")
            brand.remove_Brand(B)
    elif choice == 3 :
        brand.Print_Brands()
    elif choice == 4 :
        B = input("Please enter the brand of model : ")
        name = input("Please enter the name of model : ")
        year = input("Please enter the year of model : ")
        price = int(input("Please enter the price of model : "))
        brand.add_CarModel(B, name, year, price)
    elif choice == 5 :
        B = input("Please enter the brand of model : ")
        name = input("Please enter the name of model : ")
        brand.remove_CarModel(B, name)
    elif choice == 6 :
        B = input("Please enter the brand of models : ")
        brand.print_Model(B)
    elif choice == 7 :
        B = input("Please enter the Brand name : ")
        Bool = brand.Search_ForABrand(B)
        if Bool == True :
            print(f"The brand {B} found, Models of Brand : ")
            brand.print_Model(B)
        else :
            print(f"The brand {B} not found :< ")
    elif choice == 8 :
        B = input("Please enter the Brand : ")
        model = input('Please enter the model name : ')
        if brand.Search_ForAModel(B, model) == True :
            print('The Model found : ')
        else :
            print(f"Model {model} not found on brand {B} :(")
    elif choice == 9 :
        with open("cars.txt", "w") as file:
            for line in file:
                print(line.split())
    elif choice == 10 :
        with open("cars.txt", "r") as file :
            for line in file :
                print(line.split())
        
    elif choice == 11 :
        print("Bye :)") 
        break 

