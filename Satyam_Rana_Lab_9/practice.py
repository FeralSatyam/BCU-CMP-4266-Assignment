# class Student:
#     def __init__(self, name, student_number):
#         self.name = name
#         self.student_number = student_number
#         self.modules_list = []
    
#     def print_student_info(self):
#         print("Student name: %s" %self.name)
#         print("Student ID: %s" %self.student_number)
#         print("Modules undertaken by the student: ")
#         i = 0
#         for c in self.modules_list:
#             i += 1
#             print("%d %s" %(i,c.print_module_info()))
    
#     def enrol(self, module_running):
#         self.modules_list.append(module_running)
# class Module:
#     def __init__(self, module_title, module_credits, department):
#         self.module_title = module_title
#         self.credits = module_credits
#         self.department = department
    
#     def print_module_info(self):
#         return "%s, Credits: %s, Department: %s" %(self.module_title, self.credits, self.department)
    
# mo1 = Module("Computer Programming", 20, "Cyber Security")
# mo2 = Module("Computer Systems", 20, "Digital Media")
# mo3 = Module("Networking fundamentals", 20, "Networking and Distributed Systems")

# st1 = Student("Adam", "ID2324")
# st2 = Student("Olivia", "ID995")

# st1.enrol(mo1)
# st1.enrol(mo3)

# st2.enrol(mo3)
# st2.enrol(mo2)

# st1.print_student_info()
# print()
# st2.print_student_info()


# class Person:
#     def __init__(self, name, phone_number): 
#         self.name = name
#         self.phone_number = phone_number
#     def get_profile_info(self):
#         return "Name: %s, Phone number: %s" %(self.name, self.phone_number)
# class Student(Person):
#     def __init__(self, course, *args, **kwargs):
#         self.course = course
#         self.classes = []
#         super().__init__(*args, **kwargs)
    
#     def enrol(self, module):
#         self.classes.append(module)

# class StaffMember(Person):
#     def __init__(self, *args, **kwargs):
#         self.courses = []
#         super().__init__(*args, **kwargs)
#     def administrator_for(self, module):
#         self.courses.append(course)
#     def get_salary(self):
#         return self.salary


