class Classroom:
    def __init__(self):
        self.students = ["Alice", "Bob", "Charlie", "David", "Eve"]
        self.classroom = (10, 20, 30)
        self.grades = {
            "Alice": "A",
            "Bob": "B",
            "Charlie": "A",
            "David": "C",
            "Eve": "B"
        }

    def addStudent(self, name, grade):
        self.students.append(name)
        self.grades[name] = grade

    def get_grade(self, name):
        # for student, grade in self.grades.items():
        #     if name == student:
        #         return grade
        return self.grades.get(name)

    def average_grade(self):
        total = 0
        for student, grade in self.grades.items():
            if grade == "A":
                total += 90
            elif grade == "B":
                total += 75
            elif grade == "C":
                total += 65
        return total / len(self.students)

    def grade_dict(self):
        grade_dict = {}
        for student, grade in self.grades.items():
            if grade not in grade_dict:
                grade_dict[grade] = []
            grade_dict[grade].append(student)
        return grade_dict


# Testing
classroom = Classroom()

print("Add Student")
classroom.addStudent("Chun Hoe", "A")

print(classroom.students)
print("-----------------")

# print(classroom.students[0:3] )
# # Output: ["Alice", "Bob", "Charlie"]

# print(classroom.students[:-1])
# # Output: ['Alice', 'Bob', 'Charlie', 'David']

# print(classroom.students[::1])
print("The grade of chunhoe is:", classroom.get_grade("Chun Hoe"))

# # Removing Duplicates
# index = [1, 2, 3, 4, 5, 3, 4, 6, 3, 1, 2, 4, 5]
# index.sort()
# print(index)

# # Removing Duplicates
# index = list(set(index))
# print(index)

# print(f"The average grade is {classroom.average_grade()}")

print(classroom.grade_dict())