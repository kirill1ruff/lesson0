grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
average_grades = {}
for i in range(len(students_sorted)):
    students = students_sorted[i]
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    average_grades[students] = average_grade
print(average_grades)