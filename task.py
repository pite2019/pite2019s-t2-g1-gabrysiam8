from class_diary import Student, Lesson

stud1 = Student("Matt", "Something")
stud2 = Student("Anna", "Jakas")

less1 = Lesson("Maths")

less1.add_students(stud1, stud2)
less1.add_student_grade(stud1, 5)
less1.add_student_grade(stud1, 3)
print(stud1.count_total_avg_score())
print(stud1.count_lesson_avg_score(less1))