# print("Oleksiu")
# age = 25
# print(age)

# Типи даних :
# числові: int(integer) - ціле число. float - дробі
# рядки: str(string) - рядок
# логічний тип: bool(boolean) - True; False - істина,ложь-неправда

# Зарезервовані слова (Keywords) :
# Логика та значення :
# True,False,None (логічні значення та "ніщо")
# and,or,not (логічні оператори "і","або", "не" )
# is   - (перевірка на ідентичність )

# Умови :
# if - якщо; else - інакше  :дозволяє приймати рішення
# if - перевіряє умову ; else - виконується якщо if - хибна

# Цикли :
# while - оператор циклу(поки, до тих пір) для повторення блоку коду поки умова залишається (True)
# як тільки умова стає хибною(False)цикл зупиняється
# програма йде до наступних інструкцій
# while - коли невідомо скільки разів буде цикл наприклад чекати на ввід користувача
# for - коли завчасно знаємо кількість повторень "команда повторюй"
# while - може мати блок else,якій виконаеться 1 раз
# після того як умова циклу стане хибною(але не буде)
# виконуватися,якщо прервати командою break 

# Керування циклами :
#  break -  "все закінчуємо,я виходжу з циклу"
#  continue - "це коло пропускаємо,переходимо до наступного"

# in - це вказивник " де саме шукати" / повторювати,викор. разом з for
# pass - це порожній оператор /"нічого не роби"/ - коли правіла вимогають написання коду,але ви поки що не плануєту там нічого писати

# Функціі та класи :
# def - (створення функціі)
# return, yield - (повернення результату )
# class - (створення класу)
# lambda - (анонімна функція )

# Модулі та помилки :
# import, from, as (підключення бібліотек )
# try, except, finally, raise, assert - (обробка помилок )
# with  - (робота з контекстом, наприклад з файлами )

# Інши (спеціальни ) :
# global, nonlocal (видимість змінних в середині функцій )
# del  -  (видалення об"єкта )
# async, await  - (асихронне програмування )

# ДЗ № 1
# name = "Oleksiu"
# print(name)
# age = 25
# print(age)
# print(f"Привіт, мене звати {name}, мені {age} років.")
# name = input("Як тебе звати? ")
# print(f"Мене звати, {name}! ")

# number = 50
# text = "Hello world" 
# name = "Oleksiu"
# price = 100, 100.17
# is_active = False

# ДЗ № 2
# a = int(input("Введіть число"))
# if a <= 10:
#     print(True)
# else:
#     print(False)
# for i in range(3):
#     password = int(input("Введіть число"))
#     if password == 10:
#         print("Найбільше число")
#         break 
# else:
#     print("Це число меньше. Спробуй ще раз")

# maximum = 0
# for i in range(3):
#     password = int(input("Введить число"))
#     if password >  maximum:
#         maxsimum = password
# print(maxsimum)

# maxsimum = 0
# for i in range(3):
#     number = int(input("Введі число"))
#     if number > maxsimum:
#         maxsimum = number
# print(maxsimum)


# a = (input("Введить число "))
# count = len(a)
# print(len(a))

# a = int(input("Введить число: "))
# count = 0
# temp = abs(a)

# if temp == 0:
#     count = 1
# else:
#     while temp > 0:
#         temp = temp // 10
#         count = count + 1
# print("Кількість цифр: ", count)       

# a = int(input("Введить число: "))
# count = 0
# temp = abs(a)
# while temp > 0:
#     temp = temp // 10
#     count = count + 1
# if a == 0: count = 1   
# print("Кількість цифр: ", count)

# n = int(input("Введіть число n: " ))
# suma = 0      #Змінна для накопичення суми
# for i in range(1, n + 1):   #Перебираємо від 1 до n включно
#     if i % 2 == 0:          
#         suma += i           #Накопичуе суму
# print(f"Сума парних чисел від 1 до {n} доршвнює {suma} ")        

# while True:  #Цикл триває поки не буде правільного числа
#     try:
#         n = int(input("Введить ціле число n: "))
#         break   #Якщо помилки немає,виходимо з циклу
#     except ValueError:
#         print("Помилка ! Будь ласка введить саме число, а не текст. ")

# suma = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         suma += i

# print(f"Сума парних чисел: {suma}" )


#Створення своєі помилки :
# 1.Створюємо свій клас винятку
# class NegativeNumberError(Exception):
#     """Виняток для від'ємних чисел"""
#     pass
# # 2.Використовуємо його:
# try:
#     n = int(input("Введить додатне число n: "))
#     if n < 0:
#         # Команда raise "кидає" ппомилку
#         raise NegativeNumberError("Число не може бути меньшим за нуль! ")
#     suma = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             suma += i
#     print(f"Сума: {suma} ")
# except ValueError:
#     print("Помилка: Ви ввели не число! ")
# except NegativeNumberError as e:
#     print(f"Моя помилка: {e} ")


# #завдання 9 :
# number = float(input("Введить число: "))
# if number > 0:
#     print("Число позитивне")
# elif number < 0: 
#     print("Число негативне")
# else:
#     print ("Це нуль")

# #завдання 10 :
# # Приймаемо перше число і вважаємо його мінімальним на старті :
# min_val = float(input("Введить 1-ше число: "))
# # цикл для решти 4 чисел :
# for i in range(2, 6):
#     num = float(input(f"Введить {i}-те число: "))
#   # Порівняємо кожне нове число  з пототочним мінімумом:
#     if num < min_val:
#         min_val = num
# print(f"Найменьше число: {min_val}  ")

# завдання 11:
# number = input("Введить число: ")
# reversed_number = number[::-1]
# print(f"Результат: {reversed_number} ")

# number = input("Введить число: ")
# reversed_number = ""
# for char in number:
#     reversed_number = char + reversed_number
# print(f"Результат: {reversed_number} ")


# number = int(input("Введить число: ")) 
# reversed_number = 0
# while number > 0:
#     last_digit = number % 10 # 1.Берем останю цифру(залишок від ділення на 10)
#     reversed_number = (reversed_number * 10) + last_digit   #2.Додаємо іі в кінець новогочисла
#     number = number // 10  #Видалямо останню цифру з оригіналу(цілочисельне ділення)
# print(f"Результат: {reversed_number}") 
      
# # Завдання 12
 
# # Завдання 13
# number = int(input("Введіть число від 1 до 50: "))
# for i in range(1, number + 1):
#     if i % 2 == 0:
#         print(i)

# # Завдання 14
# sekret_number = 9
# print("Вгадай число")
# while True:
#     guess = int(input("Введи свою здогадку: "))
#     if guess == sekret_number: 
# while True:
#     name = input("Enter produkt name: ")
#     price = float(input("Enter product price: "))
#     product = {"name": name, "price": price}
#     listofProducts.append(product)
#     total_sum += price
# #l] istOfProdu    print("---")
#     ifct = [ input("Stop? (y/n): ") == "y":


# command = 0
# while True:
#     name = input("Enter product name: ")
#     price = input("Enter product price: ")

#     listOfProduct.append({"name":name, "price":price})
#     command = int(input("Enter command:"))
#     if command == 1:
#         break     

# listofProducts = []
# total_sum = 0#         break
# print(listofProducts, total_sum)#        print("Ти вгадав! Перемога. ")  
#        break
#     if guess < sekret_number:
#         print("Треба більше число. ")
#     if guess > sekret_number:
#         print("Треба менше число. ")

#

