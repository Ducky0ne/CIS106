# The student will enter their last name, midterm and final exam scores (0 – 100 points). Compute the total exam points to be the sum of 40% of midterm and 60% of the final exam. Display student last name and total exam points. 

print ("Please enter in last name")
last_name = str(input())

print ("Please enter in midterm score")
midterm_score = int(input())

print ("Please enter in final exam score")
final_exam_score = int(input())

total_exam_points = (midterm_score * .40) + (final_exam_score * .60) 

