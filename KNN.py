import math

#Training data
students = [
    [2, 60, "Fail"],
    [3, 65, "Fail"],
    [4, 70, "Pass"],
    [5, 80, "Pass"],
    [6, 85, "Pass"]
]

#New students data
new_student = [4.5, 75]

#Value of k
k = 3

#Store distances
distances = []

#Calculate distance
for student in students:
  study_hours = student[0]
  attendance = student[1]
  result = student[2]

  distance = math.sqrt(
      (new_student[0] - study_hours) ** 2 +
      (new_student[1] - attendance) ** 2
  )
  distances.append([distance, result])

#Sort distances
distances.sort()
print("Distances:")
for item in distances:
  print(item)


#Select K nearest neighbors
nearest_neighbors = distances[:k]

print("\nNearest  Nighbours:")
for item in nearest_neighbors:
  print(item)

#Count Pass and Fail
pass_count = 0
fail_count = 0

for item in nearest_neighbors:
  if item[1] == "Pass":
    pass_count += 1
  else:
    fail_count += 1

 #Prediction
if pass_count > fail_count:
  prediction = "Pass"
else:
  prediction = "Fail"

print("\nPass Count:", pass_count)
print("Fail Count:", fail_count)
print("Prediction Result:", prediction)
  
