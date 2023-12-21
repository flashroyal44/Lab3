#Цей код має три функції: InvDigits для обертання порядку цифр одного числа, 
#ReverseDigitsList для обертання порядку цифр для кожного числа у списку та Task1 
#для введення даних, виклику функцій та виведення результатів.

#Вивід буде списком чисел з оберненим порядком цифр. 







import numpy as np

def InvDigits(K):
    """
    Перетворює число K, обертаючи порядок його цифр.

    Аргументи:
    K (int): Ціле число, яке потрібно обернути.

    Повертає:
    int: Число K з оберненим порядком цифр.
    
    Винятки:
    ValueError: Генерується, якщо введені дані не є цілим числом або не можуть бути обернуті.
    """
    try:
        reversed_K = int(str(K)[::-1])
        return reversed_K
    except ValueError:
        raise ValueError("Неправильні дані! Будь ласка, введіть додатне ціле число.")

def ReverseDigitsList(lst):
    """
    Обертає порядок цифр усіх чисел у списку.

    Аргументи:
    lst (list): Список цілих чисел.

    Повертає:
    list: Список чисел з оберненим порядком цифр.
    
    Винятки:
    ValueError: Генерується, якщо обертання одного з чисел у списку неможливе.
    """
    try:
        reversed_list = [InvDigits(num) for num in lst]
        return reversed_list
    except ValueError as ve:
        raise ValueError(f"Помилка при обертанні списку: {ve}")

def Task1():
    """
    Виконує перше завдання: вводить п'ять чисел, обертає їх порядок цифр і виводить результат.
    """
    input_data = []

    for _ in range(5):
        try:
            temp = int(input("Введіть натуральне число (0 < K < 10000): "))
            input_data.append(temp)
        except ValueError:
            print("Неправильний формат числа. Спробуйте ще раз.")

    try:
        output_data = ReverseDigitsList(input_data)
        print("Зворотний порядок цифр: ", output_data)
    except ValueError as ve:
        print(f"Помилка: {ve}")
    return

def ProcessMatrix(file_name):
    """
    Обробляє матрицю з файла.

    Аргументи:
    file_name (str): Ім'я файлу, що містить матрицю.

    Повертає:
    tuple: Детермінант та обернена матриця.
    
    Винятки:
    FileNotFoundError: Генерується, якщо файл не знайдено.
    ValueError: Генерується, якщо виникають проблеми з обробкою матриці.
    """
    try:
        matrix = np.loadtxt(file_name)
        row_sums = matrix.sum(axis=1)
        row_means = row_sums / matrix.shape[1]

        transformed_matrix = matrix.T / row_means
        determinant = np.linalg.det(transformed_matrix)
        inverse_matrix = np.linalg.inv(transformed_matrix)

        return determinant, inverse_matrix
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_name} не знайдено.")
    except Exception as e:
        raise ValueError(f"Помилка при обробці матриці: {e}")

def Task2():
    """
    Виконує друге завдання: обробляє матрицю з файла, обчислює детермінант та виводить обернену матрицю.
    """
    file_name = input("Введіть назву файлу з даними матриці: ")
    
    try:
        determinant, inverse_matrix = ProcessMatrix(file_name)
        print(f"Детермінант: {determinant}")
        print("Обернена матриця:")
        print(inverse_matrix)
    except (FileNotFoundError, ValueError) as e:
        print(f"Помилка: {e}")

