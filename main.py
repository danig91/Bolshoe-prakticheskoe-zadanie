# 1. Создайте список студентов. Каждый студент представлен словарём,
# содержащим имя и список его оценок.
# 2. Напишите цикл, который пройдётся по каждому студенту
# и рассчитает его средний балл.
# - Создайте функцию `calculate_average(grades)`, которая принимает список
# оценок и возвращает среднее значение.
# - Используйте эту функцию внутри цикла для вычисления
# среднего балла каждого студента.
# 3. Определите, является ли студент успешным или отстающим.
# Считайте, что студент успешен, если его средний балл выше или равен 75.
# Добавьте логическое выражение, которое проверяет это условие,
# и выводит соответствующее сообщение.
# 4. Выведите для каждого студента сообщение следующего формата:
# Студент: Harry
# Средний балл: 84.33
# Статус: Успешен
# - Используйте f-строки для форматирования вывода.
# 5. Рассчитайте общий средний балл по всем студентам и выведите его.
# 6. Добавьте нового студента в список, используя метод `append`.
# Удалите студента с самым низким средним баллом из списка.
# 7. Список всех студентов должен пересчитываться каждый раз, когда обновляется список.
# Можно вынести код для этого в отдельную функцию.

def reformat_list_students(list_students):
    new_list_students = []
    for student in list_students:
        new_list_students.append({
            "name": student.get("name"),
            "grades": calculate_average(student.get("grades"))
        })
    return new_list_students


def calculate_average(grades):
    average_score = sum(grades) / len(grades)
    return round(average_score, 2)


def checking_academic_performance(average_score):
    if average_score >= 75:
        return "Успешный"
    else:
        return "Отстающий"


def print_information_about_students(info_about_list, list_students):
    print(f"Список студентов {info_about_list}:\n")

    reformatted_list_students = reformat_list_students(list_students)
    overall_average_score = []

    for every_student in reformatted_list_students:
        name_student = every_student.get("name")
        students_average_score = every_student.get("grades")
        status = checking_academic_performance(students_average_score)

        overall_average_score.append(students_average_score)

        print(f"Студент: {name_student}\n"
              f"Средний балл: {students_average_score}\n"
              f"Статус: {status}\n")

    print(f"Общий средний балл по всем студентам: "
          f"{calculate_average(overall_average_score)}\n")


def add_student(list_students, added_student):
    print(f"Добавлен студент: {added_student.get("name")}\n")
    return list_students.append(added_student)


def delete_student(list_students):
    student_with_low_score = min(
        list_students, key=lambda dict: dict.get("grades", 0)
    )
    print(f"Удалён студент: {student_with_low_score.get("name")}\n")
    return list_students.remove(student_with_low_score)


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]},
]

new_student = {"name": "Neville", "grades": [77, 82, 66]}

# вывод информации о студентах
print_information_about_students("изначальный", students)
# добавление студента
add_student(students, new_student)
# вывод информации после добавления студента
print_information_about_students("после добавления студента", students)
# удаление студента
delete_student(students)
# вывод информации после удаления студента
print_information_about_students("после удаления студента", students)
