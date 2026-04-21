#write a python program  that takes a student's name,marks in 3 subjects and points the total and average.
student_name=input("enter student's name:")
sub1_marks=float(input("enter marks for sub 1:"))
sub2_marks=float(input("enter marks for sub 2:"))
sub3_marks=float(input("enter marks for sub 3:"))
total_marks=sub1_marks+ sub2_marks + sub3_marks
avg_marks=total_marks/3
print(student_name)
print(total_marks)
print(avg_marks)