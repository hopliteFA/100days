# #grading coding challenge

# #provided 
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# #convert and save names and grades dictionary
# student_grades = {}

# for name in student_scores:
#     if student_scores[name] > 90:
#         student_grades[name] = "Outstanding"
#     elif student_scores[name] > 80:
#         student_grades[name] = "Exceeds expectation"
#     elif student_scores[name] > 70:
#         student_grades[name] = "Acceptable"
#     else:
#         student_grades[name] = "Fail"

# for name in student_grades:
#     print(f"{name} scored : {student_grades[name]}")

#challenge exercise 2

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, visit_number, city_names):
    travel_log.append({"country":country_name, "visits":visit_number, "cities":city_names})

#Write a function to answer this request
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])


print(f"You've visited {travel_log[2]['country']} {travel_log[2]['visits']} times.")

print(f"You visited {travel_log[2]['cities']}!")