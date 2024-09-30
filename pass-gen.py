#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_list = []
for i in range(nr_letters):
  pass_list.append(random.choice(letters))student_scores = {student: random.randint(0, 100) for student in names}
passed_stu = {student:score for (student,score) in student_scores.items if score>50}
for i in range(nr_symbols):
  pass_list.append(random.choice(symbols))
for i in range(nr_numbers):
  pass_list.append(random.choice(numbers))
random.shuffle(pass_list)
pass_string = ""
for i in pass_list:
  pass_string += i
print(f"Your password is: {pass_string}")  

