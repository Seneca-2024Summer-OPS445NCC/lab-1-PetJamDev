#!/usr/bin/env python3

from student import Student

student2 = Student('Jessica', '023384103')
student1 = Student('John', '013454900')


# Add new courses for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

print(student1.name)
print(student1.number)
print(student1.courses)
student1.displayStudent()



# Add new courses for student2
student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

print(student2.name)
print(student2.number)
print(student2.courses)
student2.displayStudent()



# student1.name is a string like any other
print(student1.name)
student1.name = 'Jack'
print(student1.name)
print(len(student1.name))
