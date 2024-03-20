#Example 1
name = ["Tehillah", "Gabrella", "Emmanuella"]
age = [2, 5, 7]
print (name, age)


#Example 2
class_roster = ["Xiulan","Kwaku", "Shirley"]
test_scores = [86, 93, 80]
print (class_roster)
print(test_scores)

#for loop
#for loops and list.
#Example 3
class_roster = ["Xiulan","Kwaku", "Shirley"]
test_scores = [86, 93, 80]
for student in class_roster:
    print(student)
for score in test_scores:
    print(score)

#Example 4
Blood_groups = ["A+" "A-", "B+", "B-", "O+", "O-"]
Genotypes = ["AA", "AS", "SS"]
for blood in Blood_groups:
    print (blood)
for patient in Genotypes:
        print(patient)

#Example 5
numbers = [1, 2, 3, 4, 5]
# Initialize a variable to store the sum of numbers
total = 0

# Iterate over each number in the list using a for loop
for num in numbers:
    # Add the current number to the total
    total += num

# Print the total sum
print("The sum of numbers is:", total)

