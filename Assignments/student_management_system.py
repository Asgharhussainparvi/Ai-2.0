names_list =[]
roll_no_list = []
ages_list = []
marks_list_1 = []
marks_list_2 = []
marks_list_3 = []

for i in range(100):
     print("\nA. Add a student \nB. View all students \nC. Search for a student \nD. Update marks of a student \nE. Analyze marks \nF. Delete a student \nG. Exit the application")

     choice = input("Choose one option A|B|C|D|E|F|G :")

     if choice == "A":
        std_name = input("Enter Student name here :")
        names_list.append(std_name)
        roll_no = input("Enter student roll  no here :")
        roll_no_list.append(roll_no)
        age = input("Enter student age here :")
        ages_list.append(age)
        mark1 = float(input("Enter marks for sub 1: "))
        mark2 = float(input("Enter marks for sub 2: "))
        mark3 = float(input("Enter marks for sub 3: "))
        marks_list_1.append(mark1)
        marks_list_2.append(mark2)
        marks_list_3.append(mark3)
        print("Student added successfully!")

     elif choice == 'B':
          if not names_list:
            print("No students found.")
          else:
            for i in range(len(names_list)):
                print(f"{i+1} Name: {names_list[i]}, Roll: {roll_no_list[i]}, Age: {ages_list[i]}, Marks: ({marks_list_1[i]}, {marks_list_2[i]}, {marks_list_3[i]})")

     elif choice == 'C':
        roll_number = input("Enter roll number of the student to search: ")
        if roll_number in roll_no_list:
            i = roll_no_list.index(roll_number)
            print(f"Student found : Name: {names_list[i]}, Roll: {roll_no_list[i]}, Age: {ages_list[i]}, Marks: ({marks_list_1[i]}, {marks_list_2[i]}, {marks_list_3[i]})")
        else:
            print("Student not found.")
    
     elif choice == 'D':
        roll_number = input("Enter roll number of the student to update marks: ")
        if roll_number in roll_no_list:
            i = roll_no_list.index(roll_number)
            print(f"Old Marks: Subject 1: {marks_list_1[i]}, Subject 2: {marks_list_2[i]}, Subject 3: {marks_list_3[i]}")
            marks_list_1[i] = float(input("Enter new marks for subject 1: "))
            marks_list_2[i] = float(input("Enter new marks for subject 2: "))
            marks_list_3[i] = float(input("Enter new marks for subject 3: "))
            print("Marks updated successfully!")
        else:
            print("Student not found.")
    
     elif choice == 'E':
        if not names_list:
            print("No students to analyze.")
        else:
            marks1_avg = sum(marks_list_1) / len(marks_list_1)
            marks2_avg = sum(marks_list_2) / len(marks_list_2)
            marks3_avg = sum(marks_list_3) / len(marks_list_3)
            print(f"Average Marks for Subject 1: {marks1_avg:.2f}")
            print(f"Average Marks for Subject 2: {marks2_avg:.2f}")
            print(f"Average Marks for Subject 3: {marks3_avg:.2f}")

     elif choice == 'F':
        roll_number = input("Enter roll number of the student to delete: ")
        if roll_number in roll_no_list:
            i = roll_no_list.index(roll_number)
            del names_list[i]
            del roll_no_list[i]
            del ages_list[i]
            del marks_list_1[i]
            del marks_list_2[i]
            del marks_list_3[i]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

     elif choice == 'G':
        print("Exit !  ")
        break

     else:
        print("Invalid choice. Please try again.")
