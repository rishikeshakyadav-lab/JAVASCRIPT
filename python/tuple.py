student_info = ("Suraj Singh", 48)
hobbies = {"Vlogging", "", "Cricket"}

subjectmarks = {
    "Python": 95,
    "DBMS": 19,
    "Data Structures": 88,
    "Mathematics": 12,
}

student_details = [student_info, hobbies, subjectmarks]

print("Student Information")
print("Name:", student_details[0][0])
print("Roll Number:", student_details[0][1])

print("\nHobbies:")
for hobby in student_details[1]:
    print("-", hobby)

print("\nSubject Marks:")
for subject, marks in student_details[2].items():
    print(subject, ":", marks)