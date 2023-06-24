i=1
students=[]

number=int(input("how many studends"))
while(i<=number):
    a=(input("Enter the student name"))
    b=int(input("Enter the rollnumber"))
    c=int(input("Enter the student age"))
    d=float(input("Enter the student CGPA"))
    student_info={'name':a,"roll no":b,"age":c,"CGPA":d}
    students.append(student_info)
    i+=1
print(students)
n=int(input("Enter the Roll number to be find"))
for s in students :
    if s['roll no']==n:
        print(s)
    else:
        print("student Roll Number not found")
print("To update the student details")
search_roll=int(input("Enter the desired student rollnumber"))
for j in students :
    if j['roll no']==search_roll:
        print("Match found")
        a=input("Enter the student name")
        b=int(input("Enter the rollnumber"))
        c=int(input("Enter the student age"))
        d=eval(input("Enter the student CGPA"))
        print("student details update successfully")
        print(j)
    else:
        print("student Roll Number not found")
print("To delete the student details")
delete_details=int(input("Enter the roll number"))
for k in students :
    if k['roll no']==delete_details:
        print("match found")
        del k
        print("student details deleted successfully")
    else:
        print("student details not found")