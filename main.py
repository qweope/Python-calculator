# Функция сложения двух чисел
def add(x, y):
    return x + y


# Функция вычитания двух чисел
def substrack(x, y):
    return x - y


# Функция уможения двух чисел
def multiply(x, y):
    return x * y


# Функция деления двух чисел
def divide(x, y):
    return x / y


print("Выберете операцию")
print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление ")

# Ввод операции
choice = input("Введите операцию:1.Слож/2.Выч/3.Умн/4.Дел:)")
num1 = float(input("Введите первое число операцию:"))
num2 = float(input("Введите второе число операцию:"))

# Выполнение функции
if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "+", num2, "=", substrack(num1, num2))
elif choice == "3":
    print(num1, "+", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "+", num2, "=", divide(num1, num2))
else:
    print("Неверный ввод")