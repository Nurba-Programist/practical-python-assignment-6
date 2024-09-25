def are_queens_safe(positions):
    # Проверяем каждую позицию ферзя
    for i in range(8):
        if is_under_attack(positions[i][0], positions[i][1], positions):
            return False  # Если хотя бы один ферзь под атакой, возвращаем False
    return True  # Если все ферзи в безопасности, возвращаем True

def is_under_attack(row, col, positions):
    # Проверяем каждого ферзя, кроме текущего
    for i in range(8):
        if positions[i][0] != row:  # Не проверяем себя
            # Проверяем по вертикали или по диагонали
            if (positions[i][1] == col or abs(positions[i][0] - row) == abs(positions[i][1] - col)):
                return False
    return True

def generate_random_queens_placement():
    import random
    return [(i, random.randint(1, 8)) for i in range(8)]

def print_valid_placements(num_placements=4):

    count = 0
    while count < num_placements:
        placement = generate_random_queens_placement()
        if are_queens_safe(placement):
            print(placement)
            count += 1



