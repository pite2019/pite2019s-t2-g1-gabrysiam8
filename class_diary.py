class Student:
	
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.lessons_scores = []

	def add_lesson_score(self, lesson):
		self.lessons_scores.append(LessonScore(self, lesson))

	def count_total_avg_score(self):
		avg_score=0
		grade_counter=0
		for ls in self.lessons_scores:
			avg_score += sum(ls.grades)
			grade_counter += len(ls.grades)
		avg_score/=grade_counter
		return avg_score

	def count_lesson_avg_score(self, lesson):
		for ls in self.lessons_scores:
			if ls.lesson==lesson:
				return sum(ls.grades)/len(ls.grades)





class Lesson:
	
	def __init__(self, name):
		self.name = name
		self.students = []

	def add_students(self, *students):
		for student in students:
			self.students.append(student)
			student.add_lesson_score(self)

	def add_student_grade(self, student, grade):
		if student in self.students:
			for ls in student.lessons_scores:
				if ls.lesson==self:
					ls.add_grade(grade)

	def start_lesson(self, *students):
		pass



class LessonScore:

	def __init__(self, student, lesson):
		self.student = student
		self.lesson = lesson
		self.grades = []
		self.attendance = 0

	def add_grade(self, grade):
		self.grades.append(grade)