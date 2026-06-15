# import mypackage.math_utils as math
# import mypackage.string_utils as string

# print(math.add(5,3))
# print(math.multiply(4,2))
# print(string.shout("hello"))
# print(string.greet("Oleksiu"))

# import mypackage.user_utiles as user

# print(user.full_name("Ivan", "Petrenko"))
# print(user.is_adult(20))
# print(user.is_adult(15))

# import mypackage.temperature_utils as temperature

# print(temperature.celsius_tu_fahrenhtit(100))
# print(temperature.fahrenhtit_tu_celsius(200))

# import mypackage.math1_utils as math1

# print(math1.square(5))
# print(math1.cube(3))

# import mypackage.list_utils as list
# print(list.get_max([1,2,3,4,5,46,12]))
# print(list.get_min([1,2,3,4,5,46,12]))

# import mypackage.geometri as geometri
# print (geometri.area_square(9))
# print (geometri.area_circle(5))

# import utils.math_utils as math
# print(math.add(7, 8))
# print(math.subtract(9, 11))
# print(math.multiply(5, 4))

# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

# import math
# #y = x**2 + 2x - 3
# for x in range(-5, 6):
#     print(x, round(x**2 + 2*x - 3))

# import random
# while True:
#     x = random.randit(1, 6)
#     print(x)
#     a = input("Xoчеш ще ? ")
#     if a == "ні":
#         break

#     def calculate_distancion(x1, x2, y1, y2 )
#         return(match.sqtr(x2 - x1)**2 + (y2 - y1)**2)

# import random
# for i in range(1, 11):
#     coin = random.choice(["Орел", "Решка" ])
#     if coin == "Орел"

# class Book:
#     def __init__(self, title, author, pages):
#        self.title = title
#        self.author = author
#        self.pages = pages
#     def info(self):
#         print(f"Назва: {self.title}, Автор: {self.author},Сторінка: {self.pages}")
# book1 = Book("Moses", "Franko","5" )
# book2 = Book("The Haydamaks", "Shevchenko","8")

# book1.info()
# book2.info()


# class Calculator:
#     def add(self, a, b ):
#         return a + b
#     def subtract(self, a, b):
#         return a - b
#     def multiply(self, a, b):
#         return a * b
# res = Calculator()
# print(res.add(10, 5))
# print(res.subtract(10, 5))
# print(res.multiply(10, 5))


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = "Oleksiy"
#         self.balance = 1000000
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
       
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Недостатньо коштів на рахунку")
#             return self.balance
#         self.balance -= amount
#         return self.balance
#     def get_balance(self):
#         return self.balance
    
# my_acc = BankAccount("Oleksiy", 1000000)
# print(my_acc.deposit(500))
# print(my_acc.withdraw(200))
# print(my_acc.withdraw(2000000))


# class Stil:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def get_info(self):
#         return f"{self.color},{self.model}"
# class Stil21(Stil):
#     def __init__(self, color, model, yer, wusota):
#         super().__init__(color, model)
#         self.yer = yer
#         self.wusota = wusota

#     def get_fuel_info(self):
#         return f"{self.wusota}"
# stil = Stil21( "red", "parta", 1999, 120)
# print(stil.get_fuel_info())


# class Telephone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def get_info(self):
#         return f"{self.brand},{self.model}" 
    
# class Smartphone(Telephone):
#     def __init__(self, brand, model, os = "Android"):
#         super().__init__(brand, model)
#         self.os = os
#     def get_os_info(self):
#         return f"{self.os}"
     
# class IPhone(Smartphone):
#     def __init__(self, brand, model, os ):
#         super().__init__(brand = "Apple", model = model, os = "IOS")
#     def get_os_info(self):
#         return super().get_os_info()

# smartphone1 = Smartphone("Motorola", "g86 power 5g", "Android")
# smartphone2 = IPhone("Apple", "17", "IOS")

# print(smartphone1.get_info())
# print(smartphone2.get_info())


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_price(self):
#         return self.price

# product = Product("Sliva", 15)
# print(product.get_price())

## Завдання 2(наслідування)

# class Vehicle:
#     def __init__(self):
#         pass
#     def move(self):
#         print("The vehicie is moving")

# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#     def move(self):
#         print("The car is driving on the road")
# class Bike:
#     def __init__(self):
#         super().__init__()
#     def move(self):
#         print("The bike is riding on the path")
# car_instance = Car()
# bike_instance = Bike()
# car_instance.move()
# bike_instance.move()

# # Завдання 3 

# class Employee:
#     def __int__(self):
#         pass
#     def work(self):
#         print("Company salary")
# class Manager(Employee):
#     def __int__(self):
#         super().__init__()
#     def work(self):
#         print("Manager = Base salary + bonus""," "Perfromance-based bonus")
# class Developer(Employee):
#     def __int__(self):
#         super().__init__()
#     def work(self):
#         print("Developer = Fixed monthly salary""," "Hourly rate")
# manager_salary = Manager()
# developer_salary = Developer()
# manager_salary.work()
# developer_salary.work()

# class Employee:
#     def __init__(self, salary ):
#         self.salary = salary
#     def work(self):
#         print("Compani salary")
# class Manager(Employee):
#     def __init__(self, salary ):
#         super().__init__(salary)
#         self.salary = salary
#     def work(self):
#         print(f"Manager = Base salary + bonus, Perfromance-based bonus: ${self.salary}" )
# class Developer(Employee):
#     def __init(self, salary ):
#         super().__init__(salary) 
#         self.salary = salary
#     def work(self):
#         print(f"Developer = Fixed monthly salary, Hourly rate: ${self.salary}" )
# manager_salary = Manager(4000)
# developer_salary = Developer(5000) 
# manager_salary.work()
# developer_salary.work()


# class Animal:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"Animal makes a ssound")
# class Dog(Animal):
#     def __init__(self,name, age, breed):
#         super().__init__(name,age)
#         self.breed = breed
#     def speak(self):
        
#         print(f"Woof My name is {self.name}, I am {self.age} yers old" )
# class Cat(Animal):
#     def __init__(self,name, age, color):
#         super().__init__(name, age)
#         self.color = color
#     def speak(self):
        
#         print(f"Meow ! I am {self.color} cat named {self.name}")
# dog = Dog("Rex", 3, "Labrador") 
# cat = Cat("Whiskers",5, "black")
# dog.speak()        
# cat.speak()        

# import math  
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, a, b, c ):
#         self.a = a
#         self.b = b
#         self.c = c
#     def area(self):
#         p = (self.a + self.b +self.c) / 2  
#         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) 

# class Rectangle(Shape):
#     def __init__(self, width, height ):
#         self.width = width
#         self.height = height
#     def area(self):
    
#         return (self.width * self.height)

# triangle = Triangle(3, 4, 5)
# r = Rectangle(5, 6)
# print(triangle.area())
# print(r.area())          

# import math
# from abc import ABC, abstractmethod 
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius ):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius** 2
    
#     def perimeter(self):
#         return 2 * math.pi * self.radius
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def area(self):    
#         p = (self.a + self.b + self.c) / 2
#         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#     def perimeter(self):
#         return self.a + self.b + self.c
# class Rectangle(Shape):
#     def __init__(self, width, height ):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return (self.width + self.height) * 2
# circle = Circle(8)
# print (f"Площа кола: {circle.area(): .2f}")
# print (f"Перимітер кола: {circle.perimeter():.2f}")
# rectangle = Rectangle(10, 12)
# print (f"Площа прямокутника: {rectangle.area()}")
# print (f"Перимітер прямокутника: {rectangle.perimeter()}")
# triangle = Triangle(8,10,12)
# print (f"Площа трикутника: {triangle.area():.2f}")
# print (f"Перимітер трикутника: {triangle.perimeter()}")

        

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         print("Driving the car")
#     @abstractmethod
#     def stop(self):
#         print("Stoping the car")
# class Biek(Vehicle):
#     def __init__(self, model, speed):
#         self.model = model
#         self.speed = speed
#     def drive(self):
#         print(f"{self.model} is driving at {self.speed} km/h")
#     def stop(self):
#         print(f"{self.model} has stooping")
# class Car(Vehicle):
#     def __init__(self, model, speed, color):
#         self.model = model
#         self.speed = speed
#         self.color = color
#     def drive(self):
#         print(f"{self.model} is driving at {self.speed} k/h")
#     def stop(self):
#         print(f"{self.model} has stooping" )
# biek = Biek("Yava", 180)
# print(f"Model:{biek.model}") 
# print(f"Speed:{biek.speed} km/h")
# biek.drive()
# biek.stop()       
        
# car = Car("BMV", 200, "red")
# print(f"Model:{car.model}") 
# print(f"Speed:{car.speed} km/h")
# car.drive()
# car.stop()       
        
# leson 8
# Завдання 1.
# class Product:
#     def __init__(self, name, price ):
#         self.name = name
#         self.price = price
# class Cart(Product):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#         self.items = []
#     def add_product(self,product):
#         self.items.append(product)
#     def total(self):

#         return sum(item.price for item in self.items)
# class Cash:
#     pass
# class Order():
#     def __init__(self, cart, payment):
        
#         self.cart = cart
#         self.payment = payment
#     def checkout(self):
#         amount = self.cart.total()
#         return self.payment.pay(amount)
    

# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def refund(self,amount):
#         pass
#     def process_payment(self, amount):
#         self.pay(amount)
#         self.refund(amount)
# class GooglePay(Payment):
#     def pay(self, amount):
#         print(f"Processing Google Pay payment of ${amount}")
#     def refund(self, amount):
#         print(f"Processing Google Pay refund of ${amount}")
# class ApplePay(Payment):
#     def pay(self, amount):
#         print(f"Processing Apple Pay payment of ${amount}")
#     def refund(self, amount):
#             print(f"Processing Apple Pay refund of ${amount}")
# google_pay = GooglePay()
# apple_pay = ApplePay()
# google_pay.pay(100)
# apple_pay.pay(150)

# try:
#     number = float(input("Введи число:"))
#     if number == 0:
#         raise ValueError("Ділення на нуль заборонено")
#     result = 100 / number
#     print(f"100 / {number} = result")
# except ValueError as e:
#     print(f"Помилка: {e}")


# try:
#     user = (input("Введи імя:"))
#     if user == "":
#         raise ValueError(f"імя не може бути порожнім")
# except ValueError as e:
#     print(f"Помилка: {e}")
# else:
    
#     print(f"Вітаю {user}")
# finally:
#     print(f"Програма завершена") 


# try:
#     a = int(input("Number1 "))
#     b = int(input("Number2 "))
    
#     print (a / b)
# except Exception as e:
#     print(e)

# while True:
#     try:
#         number = float(input("Введи число" ))
        
#     except Exception as e:
#         print(e)
        
#     else:
#         print("Ви ввели правильне число") 
#         break          


# def check_password(password):
#     if len(password) < 8:
#         raise ValueError("Ви ввели неправильний пароль" )          
# try:
#     password = (input("Введить пароль"  ))
#     check_password(password)
#     print("Пароль прийнято" )
    
# except Exception as e:
#     print(e)
    
# try:
#     a = int(input(" Введи число а" ))
#     b = int(input("Введи число b" ))
#     a / b   
# except ZeroDivisionError as e:    
#     print("ZeroDivisionError")

# while True:
#     try:
#         a = int(input("Введить ціле число"))
#     except ValueError as e:
#         print("Помилка. Повторить спробу")
#     else:
#         print("Ви правильно ввели число. Отримали доступ")
#         break     

# def my_age(age):
    
#     if age <= 0 or age >= 150:
#         raise ValueError("Неправильний вік") 
        
# try:
#     age = float(input("Який ваш вік ?"  ))
#     my_age(age)
#     print("Вік правильний")
# except Exception as e:
#     print(e)


# while True:
#     try:
#         number = int(input("Введи число від 1 до 10 "  ))
#         if number > 10 or number < 1:
#             raise ValueError("Ви ввели число поза межами 1-10. Повторіть спробу")
        
#     except Exception as e:
#         print("Помилка.Введитьчисло")
#     else:
#           print("Ви ввели правильне число")
#           break
    
# try:
#     a = int(input("Введить число " )) 
#     b = int(input("Введить 2 число " ))
#     rezult = a / b
#     print(rezult) 
# except ZeroDivisionError as e:
#     print("На нуль ділити не можна" )

# while True:
#     try:
#         a = int(input("Введить ціле число "))  
#     except Exception as e:
#         print("Повторить спробу")
#     else:
#         print("Попитка успішна")
#         break  
        
# 



# try:
#     a = int(input("Введить число "))
#     b = int(input("Введить друге число "))
#     a / b
# except ZeroDivisionError as e:
#     print("Повторить спробу")
# else:
#     print("Дякуємо що ви з нами ")

# while True:
#     try:
#         a = int(input("Введить ціле число "))
#     except Exception as e:
#         print("Повторить спробу")
#     else:
#         print("Дякуємо що ви з нами ")
#         break
# try:
#     password = input("Введить пароль ")
#     if len(password) <= 8:
#         raise ValueError("Пароль не вірний. Повтогрить спробу ")
# except ValueError as e:
#      print(e)        
# else:
#         print("Пароль вірний")

# def check_password():
    
#     while True:
#         password = input("Введить пароль ")    
#         try:
#             if len (password) < 8:
#                 raise ValueError("Пароль невірний.Повторить спробу ")
#         except ValueError as e:
#             print(e)
#         else:
#             print("Пароль вірний")
#             break
# check_password()
               
# try:
#     a = int(input("Введить число "))
#     if a == 0: 
#         print("Не можна ділити на 0 ")
#     else:
#         print(100 / a )       
# except ValueError as e:
#     print("Це не число ")

# while True:
#     try:
#         a = int(input("Введить число "))
#         b = int(input("Введить друге число "))
#         c = input("operatiton: +, -, *, /; ")
#         if c == "+":
#             suma = a + b
#             print(suma)
#         elif c == "-":
#             suma = a - b
#             print(suma)
#         elif c == "*":
#             suma = a * b
#             print(suma)
#         elif c == "/":
#             suma = a / b
#             print(suma)    
#     except ZeroDivisionError as e:
#         print(e)
#         break
         
# class Book:
#     def __init__(self, title, author, pages ):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def info(self):
#         print(f"{self.title}, {self.author},{self.pages}")
# roman = Book("Eneida", "kotlarevskiy", 300)
# roman.info()

# class Student:
#     def __init__(self, name, grades ):
#         self.name = name
#         self.grades = grades
#     def add_grade(self, mark):
#         self.grades.append(mark)
#     def average(self):
#         return sum(self.grades) / len(self.grades)
# studedent1 = Student("Ivan", [5, 4, 3])
# print(studedent1.average())
    
# class Calculator:
#     def __init__(self, a, b ):
#             self.a = a
#             self.b = b
#     def add(self):
#         return self.a + self.b
#     def subtract(self):
#         return self.a - self.b
#     def mulltiply(self):
#         return self.a * self.b
# while True:       
#     num1 = int(input("Введить перше число: "))
#     num2 = int(input("Введить друге число: "))
#     calculator = Calculator(num1, num2  )
#     print(calculator.add())
#     print(calculator.subtract())
#     print(calculator.mulltiply())
#     answer = input("Бажаете продовжити ? (так/ні): ")
#     if answer.lower() != "так":
#          print("Програму завершено.")
#          break
        


# class Calculator:
#     def __init__(self, a, b ):
#             self.a = a
#             self.b = b 
#     def add(self):
#         return self.a + self.b
#     def subtract(self):
#         return self.a - self.b
#     def multiply(self):
#         return self.a * self.b
#     def devide(self):
#         if self.b == 0:
#             return "Помилка: на нуль ділити не можна."
#         return self.a / self.b
        
# while True:        
    
#     num1 = int(input("Введіть перше число: ")) 
#     num2 = int(input("Введіть друге число: "))  
#     calculator = Calculator(num1, num2)
#     operation = input("Оберить дію (+, -, * ) або напишить {вихід}: ")
#     if operation == "вихід":
#         print("Дякуємо за використання калькулятора" )
#         break
    
#     elif operation == "+":
#         print("Результат додавання: ", calculator.add())
#     elif operation == "-":
#         print("Результат віднимання: ",calculator.subtract())
#     elif operation == "*":
#         print("Результат множення: ", calculator.multiply())
#     elif operation == "/":
#         print("Результат ділення:", calculator.devide())
#     else:
#         print("Таку дію не знайдено. Спробуйте ще раз.")
      


# class Book:
#     def __init__(self, title, author, year,is_borrowed = False):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.is_borrowed = is_borrowed
#     def borrow_book(self):
#         if self.is_borrowed == True:
#             print("Книгу взяли.Вона не доступна.")
#         else:
#             self.is_borrowed = True
#             print("Ви успішно взяли книгу.")
#     def return_book(self):
#         if self.is_borrowed == True:
#             self.is_borrowed = False
#             print("Книга повернута. Книга доступна.")
#         else:
#             print("Книга є доступною")
# book1 = Book("Eneida", "Kotlarevsciy", 1842)
# book2 = Book("Histori of Ukrain", "Grushevckiy", 1937) 
# book1.borrow_book()
# book1.borrow_book()
# book2.borrow_book() 
# book1.return_book()
# book1.return_book()      




# Онлайн магазин
# class User:
#     def __init__(self, balance, name ):
#         self.__balance = balance
#         self.name = name

#     def deposit_amount(self, amount ):
#         self.__balance += amount
#         return self.__balance
    
#     def get_balance(self):
#         return self.__balance 
# class PremiumUser(User):
#     def __init__(self, balance, name, price):

#         super().__init__(balance, name)

#         self.price = price
#     def buy_item(self):
#         discount_price = self.price * 0.9
#         if self.get_balance() < discount_price:
        
#             print("На вашому рахунку не достатньо коштів")
#             return False
#         else:
#             self.deposit_amount(-discount_price)
#             print("Товар оплачено. Дякуемо що ви з нами")
#             return True
# premium_user = PremiumUser(1000, "Іван", 500 )
# print(f"Початковий баланс {premium_user.name}: {premium_user.get_balance()} грн ")    
# premium_user.buy_item()
# print(f"Баланс після покупки: {premium_user.get_balance()} грн")

          

# class Vehicle:
#     def __init__(self, brend, speed):
#         self.brend = brend 
#         self.speed = speed
#     def move(self):
#         return(f"[{self.brend}] іде зі швикістю [{self.speed}]км/год")  
# class Car(Vehicle):
#     def __init__(self, brend, speed):
#         super().__init__(brend, speed)
# class ElectricCar(Vehicle):
#     def __init__(self, brend, speed, battery_level ):
#         super().__init__(brend, speed)
#         self.battery_level = battery_level
#     def move(self):
#         if self.battery_level <= 0:
#               return("Батарея розрядженна")
#         else:
#             self.battery_level -= 5   
#             return(f"[{self.brend}] іде зі швидкістю [{self.speed}]км/год. Заряд батареі: [{self.battery_level}%] ")
# def start_race(vehicles_list):
#     for move in vehicles_list:
#         print(move.move())

# car1 = Car("BMV", 220 )
# car2 = ElectricCar("Tesla", 250, 10)    
# start_race([car1, car2])   
# start_race([car1, car2])
# start_race([car1,car2])
# print("Закриплюю матеріал")
# print("Тест2 ")
print("Тест3") 
           