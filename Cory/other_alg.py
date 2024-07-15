def lattice_multiplication(num1, num2):
    # Преобразуем числа в строки для работы с отдельными цифрами
    num1_str = str(num1)
    num2_str = str(num2)

    # Размер решетки
    rows = len(num1_str)
    cols = len(num2_str)

    # Создаем пустую решетку
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
   
    # Заполняем решетку произведениями цифр
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = int(num1_str[i]) * int(num2_str[j])
    
    # Подсчитываем количество строк и столбцов
    result = [0] * (rows + cols - 1)
    
    # Заполняем результат
    for i in range(rows):
        for j in range(cols):
            result[i + j] += grid[i][j]
    print(result)
    # Приводим результат к правильному виду
    for i in range(len(result)-1, 0, -1):
        if result[i] >= 10:
            result[i-1] += result[i] // 10
            result[i] %= 10

    # Преобразуем результат в строку и затем в число
    result_str = ''.join(map(str, result))
    
    return int(result_str)

# Пример использования
num1 = 123
num2 = 456
print(f"Произведение {num1} и {num2} равно {lattice_multiplication(num1, num2)}")


def hanoi(n, source, temp, target):
    if n == 0:
        return
    hanoi(n-1, source, target, temp)
    print(f'Move disk from {source} to {target}')
    hanoi(n-1, temp, source, target)
    
hanoi(4, 'a', 'b', 'c')