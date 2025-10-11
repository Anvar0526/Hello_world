def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль!"
    return x / y

def calculator():
    print("Простой калькулятор")
    print("Операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    
    while True:
        choice = input("Выберите операцию (1/2/3/4 или + - * /), или 'q' для выхода: ")
        if choice.lower() == 'q':
            print("Выход из калькулятора.")
            break

        if choice not in ('1', '2', '3', '4', '+', '-', '*', '/'):
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Введите числовое значение.")
            continue

        if choice in ('1', '+'):
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
        elif choice in ('2', '-'):
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice in ('3', '*'):
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice in ('4', '/'):
            result = divide(num1, num2)
            print(f"Результат: {num1} / {num2} = {result}")

        print("\n---\n")

if __name__ == "__main__":
    calculator()