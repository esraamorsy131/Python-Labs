#Question 1
class Rectangle:
    def __init__(self):
        self.length = int(input("Please enter the length: "))
        self.width = int(input("Please enter the width: "))
        
    def get_area(self):
        self.area = self.length * self.width
        print(f"Area of the rectangle is {self.area}")
        

rect = Rectangle()
rect.get_area()

#Question 2
class Bankaaccount:
    def __init__(self,accountnumber,password,balance =0):
        self.__accountnumber = accountnumber 
        self.balance = balance
        self.password = password
      
    def check_password(self):
        user_password = int(input("please enter your password: ")) 
        if user_password == self.password:
            return True
        else:
            return False
         
    def deposit_amount(self):
        self.amount = int(input("please enter the amount you want to deposit :  "))
        self.total = self.balance + self.amount
        self.balance = self.total
        print(self.balance)
        
    
    def withdraw_amount(self):
        if self.check_password() == True:
            self.amount = int(input("please enter the amount you want to withdraw :  "))
            self.total = self.balance - self.amount
            self.balance = self.total
            print(self.balance)
        
            
           
            
        else:
            print("please try again")
     
    
Esraa = Bankaaccount(123,2389)
Esraa.deposit_amount()
Esraa.withdraw_amount()

#Question 3
class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("Im just an animal !")
        
class Dog(Animal):
    def speak(self):
        print("Im just a dog !")
        
class Cat(Animal):
    def speak(self):
        print("Im just a cat !")        


Bow =Dog() 
Bow.speak()

Mickey =Cat()
Mickey.speak()

#Question 4
class Vehicle:
    def __init__(self,model,make = "Made IN China"):
        self.model = model
        
class Car(Vehicle):
    def __init__(self,model,color,speed,make = "Made IN China"):
        self.color = color
        self.speed = speed
    
    def type(self):
        cars = ["Toyota", "Renaut" , "Fiat"]
        self.type = cars
        print(self.type)
            
        
        
    
class Motorcycle(Vehicle):
    def __init__(self,model,color,make = "Made IN China,"):
        self.color = color
    
    def type(self):
        self.type = "jet"
        print(self.type)
        
my_car=Car(2000,"red",1)
my_car.type()

my_moto=Motorcycle(2005,"blue",1.5)
my_moto.type()
        
    
  
    
        