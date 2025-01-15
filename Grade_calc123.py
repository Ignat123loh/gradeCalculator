l = []
for i in range(int(input("Сколько оценок?"))):
    l.append(int(input("Введите оценку ученика😗🥺🥰")))
n = int(input())
if i < 1:
    print("Error!")
else:
    l.append(n)
print(f"Средняя оценка ученика: {sum(l) / len(l)}")


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


# Тест 1: Проверка с несколькими оценками
grades_1 = [4, 5, 3, 4]
assert calculate_average(grades_1) == 4.0, "Тест 1 не прошел"

# Тест 2: Проверка с одной оценкой
grades_2 = [5]
assert calculate_average(grades_2) == 5.0, "Тест 2 не прошел"

# Тест 3: Проверка с пустым списком оценок (возвращается 0)
grades_3 = []
assert calculate_average(grades_3) == 0, "Тест 3 не прошел"

# Тест 4: Проверка с разными оценками
grades_4 = [1, 2, 3, 4, 5]
assert calculate_average(grades_4) == 3.0, "Тест 4 не прошел"

print("Все тесты пройдены успешно!")