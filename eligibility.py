marks=65
attendence=80
marks_ok=marks>=50
attendence_ok=attendence>=75

eiligible = marks_ok and attendence_ok
one_condition = marks_ok or attendence_ok
not_eligible = not eiligible

print("AND=",eiligible)
print("OR=",one_condition)
print("NOT=",not_eligible)
