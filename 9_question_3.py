class StudentDashboard:
    def grade(marks):
        marks = int(marks)
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"
        return grade

    def password_validity(password):
        has_number = False
        has_8_digits = False

        if len(password) >= 8:
            has_8_digits = True
        if any(letter.isdigit() for letter in password):
            has_number = True

        return has_number & has_8_digits

# print(StudentDashboard.grade(80))

print(StudentDashboard.password_validity("Pa"))

# Range
for i in range(2, 11, 2):
    print(i)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for names, scores in enumerate(zip(names, scores)):
    print(names, scores)

