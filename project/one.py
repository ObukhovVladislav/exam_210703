def valid_name(txt):
    return txt.istitle()


students = ['Иван', 'Мария', 'Сергей']
students_upd = (student for student in students if valid_name(student))
print(students_upd)
print(next(students_upd))
