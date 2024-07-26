# numbers = [1,2,3]

# new_list_lame_method=[]

# for number in numbers:
#     new_number=number+1
#     new_list_lame_method.append(new_number)

# print(new_list_lame_method)

# new_list_exciting_method=[n+1 for n in numbers]
# print(new_list_exciting_method)

# name = "Joseph"

# letters_list = [letter for letter in name]
# print(letters_list)

# numbers = [num * 2 for num in range(1,5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# long_names =[name.upper() for name in names if len(name) > 4]
# print(long_names)
import random

student_scores = {
    student:random.randint(1,100) for
    student in
    names
}

print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 50}
print(passed_students)