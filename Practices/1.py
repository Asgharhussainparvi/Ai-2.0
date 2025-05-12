data = ((1, 5), (3, 2), (2, 8), (4, 1))

# Sorting tuples by their second element using a lambda expression as the key
sorted_data = sorted(data, key=lambda item: [1])

print("Original tuple:", data)
print("Sorted by second element:", sorted_data)


#You have a dictionary that contains students' names as keys, and their respective scores in different subjects as lists (values).
student_scores = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 76],
    "Charlie": [80, 95, 89]
}
#Write a Python program using a nested for loop to:
#Iterate through the dictionary.
#Print the student's name and their individual scores on separate lines.
#The program should output the name of each student followed by their individual scores, each on a new line.


# Start of a loop to iterate through the dictionary items (student names and their scores)

    # Print the student's name and a message indicating their scores
    
    # Nested loop to iterate through each score in the current student's list of scores
    
        # Print each individual score on a new line
    
   # Print a blank line to separate each student's scores for better readability




# Write a Python program to iterate through the following dictionary and print a message for each item:
students_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

#If the score is 90 or above, print: "Student <name> has an excellent score!"
#If the score is between 80 and 89, print: "Student <name> has a good score."
#Otherwise, print: "Student <name> needs improvement."

