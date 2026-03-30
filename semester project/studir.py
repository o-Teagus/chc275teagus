
def getStudent(directory, student):
    if student in directory:
        return directory[student]["grades"], directory[student]["gradelevel"], directory[student]["email"]
    else:
        print("Student not found")

def getStudentGrades(directory, student):
    return directory[student]["grades"]

def getStudentGradeLevel(directory,student):
    return directory[student]["gradelevel"]

def getStudentEmail(directory,student):
    return directory[student]["email"]

def getStudentsByGradeLevel(directory, gradelevel):
    found = False
    for student in directory:
        if directory[student]["gradelevel"] == gradelevel:
            print(student)
            found = True
    if not found:
        print("Nobody found in that grade level")

def addStudent(directory):
    name = input("Enter Name: ").strip().lower()
    enggrades = float(input("Enter English Grade: "))
    mathgrades = float(input("Enter Math Grade: "))
    histgrades = float(input("Enter History Grade: "))
    relgrades = float(input("Enter Religion Grade: "))
    grades = {"English": enggrades, "Math": mathgrades, "History": histgrades, "Religion": relgrades}
    email = input("Enter Email: ").strip().lower()
    gradelevel = int(input("Enter Grade Level: "))
    directory[name] = {"grades": grades, "gradelevel": gradelevel, "email": email}
    print(f"{name} was added")

def removeStudent(directory, student):
    if student in directory:
        directory.pop(student)
        print(f"{student} was removed")
    else:
        print("not found")

def updateGrade(directory, student):
    if student in directory:
        enggrades = float(input("Enter English Grade:"))
        mathgrades = float(input("Enter Math Grade:"))
        histgrades = float(input("Enter History Grade:"))
        relgrades = float(input("Enter Religion Grade:"))
        directory[student]["grades"] = {"English": enggrades, "Math": mathgrades, "History": histgrades, "Religion": relgrades}
        print(f"{student}'s grades were updated")
    else:
        print("not found")

def calculateGPA(directory, student):
    grades = directory[student]["grades"]
    total = sum(grades.values())
    classes = len(grades)
    return total / classes

def checkHonorRoll(directory,student):
    grades = directory[student]["grades"]
    GPA = calculateGPA(directory, student)
    if GPA >= 88 and min(grades.values()) > 81:
        print(f"{student}, made Honor Roll!")
    else:
        print(f"Sorry but {student}, did not make Honor Roll")

def printMenu():
    print("Welcome to CHC's Student Directory")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Get Student")
    print("4. Update Grades")
    print("5. Calculate GPA")
    print("6. Get Students by Grade Level")
    print("7. Exit")
    pass

def main():
    Students = {"Teague": {"grades": {"English": 93, "Math": 95, "History": 99, "Religion": 99},"gradelevel": 11,"email": "jimmy@email.com"},
                "Preston": {"grades": {"English": 90, "Math": 85, "History": 75, "Religion": 89},"gradelevel": 11,"email": "timmy@email.com"},
                "Frank": {"grades": {"English": 80, "Math": 82, "History": 85, "Religion": 89},"gradelevel": 9,"email": "mike@email.com"},
                "Lettuce": {"grades": {"English": 70, "Math": 55, "History": 75, "Religion": 89},"gradelevel": 13,"email": "john@email.com"}}
    
    while True:
        printMenu()
        choice = input("pick an option: ")

        if choice == "1":
            addStudent(Students)

        elif choice == "2":
            student = input("Student name: ").strip().lower()
            removeStudent(Students, student)

        elif choice == "3":
            student = input("Student name: ").strip().lower()
            print(getStudent(Students, student))

        elif choice == "4":
            student = input("Student name: ").strip().lower()
            updateGrade(Students, student)
        
        elif choice == "5":
            student = input("Student name: ").strip().lower()
            gpa = calculateGPA(Students, student)
            print(f"{student}'s GPA is {gpa}")
            checkHonorRoll(Students, student)

        elif choice == "6":
            gradelevel = int(input("Grade level: "))
            getStudentsByGradeLevel(Students, gradelevel)

        elif choice == "7":
            for name in Students:
                print(f"{name},{Students[name]}")
            return True

        else:
            print("Invalid")

if __name__ == "__main__":
    main()