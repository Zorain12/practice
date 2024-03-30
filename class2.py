# variable naming convension
# 1- lowercase    firstname
# 2- camelCase    firstName
# 3- snake_case   first_name (perferable for python programming)

# data_types_oython
# int, float, bool, str

# type_checking_syntex
# x=5
# print(type(x))

# unique_values
# x={3,5,6}
# print(x)

# int data types in (static language)
# byte, sbyte
# short, ushort
# int,   uint
# long, ulong

# x=2           ##int
# x=2.3         ##float
# x="zorain"    ##str
# x=True/False  #Bool

## how to check subclass
# print (issubclass(complex, int))  # False
# print (issubclass(float, int))

# Most_Common_values
# numeric values (int+float)
# boolean values
# textual values

# other_values
# set   values
# list  values
# tuple values
# dic   values

# message='From example@gmail.com Mon 10:01 AM' # array
# print(message[12:22])

# x=1234
# x2= (1+2+3+4)/2
# print(x2)
############## TASK ############
# product=['a','b','c','d']
# NP=input('new_product: ')
# a=False
# for i in product:
#     if NP in product:
#         a=True
#         print('Already_Existing')
#         break
# if (a==False):
#     product.append(NP)
#     print(product)
#     print('New_item_added_in_list')

############## while-Loop ###########
# product=['a','b','c','d']
# i=0
# while i<len(product):
#     print(product[i])
#     i+=1

# for i in product:
#     print(i)

############# Reverse_order_for_loop ######for i in range(len(a),-1,-1):
###### even number
# a=[1,3,2,4,6]
# for i in range(len(a)):
#     # print (a[i])
#     if(a[i]%2==0):
#         print(a[i])

#####through while loop
# values=[2,4,8,7,9]
# i=0
# while i<len(values):
#     # print(values[i])
#     if(values[i]%2==0):
#         print(values[i])
#     i+=1

# a=['abc','yyy', 'aop','yoy']
# new_user=[]
# for i in a:
#     if i[-1]=='y':
#         new_user.append(i)
# print(new_user)

# values = [3, 6, 7, 2, 4]
# max_value = values[0]  # max_value = 3
# for value in values:
#     if value > max_value:
#         max_value = value
# print(max_value)

# a = [
#     [2, 3, 5],
#     [1, 2, 3]
#     ]
# b= a[0] + a[1]
# print(b)

# v1 = [2, 3, 4]
# v2 = [5, 6, 8]
# v3 = []
# a = 0
# for b in v1:
#     d = b + v2[a]
#     v3.append(d)
#     a += 1
# print(v3)


# v1 = [2, 3, 4]
# v2 = [5, 6, 8]
# v3 = []
# for i in range(len(v1)):
#     d = v1 + v2
#     v3.append(d)
# print(v3[i])
# a = []
# for i in range(2):
#     for j in range(3):
#         a.append(a[i][j])
# print(a)
# mat = []
# v1 = [[2, 5, 4], [2, 5, 9], [7, 1, 3], [8, 4, 2]]
# for i in range(len(v1)):
#     a = []
#     for j in range(len(v1)-1):
#         a.append(j)
#     mat.append(a)
# print(mat)

# a,b,c=100,50,78
# if a>b:
#     if a>c:
#         print(a)
# elif b>a:
#     if b>c:
#         print(b)
# else:
#     print(c)

# a, b, c = 100, 500, 780
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# mat = [[1, 2, 3], [4, 5, 6]]
# print(mat[0][-1])

# mat = []
# for i in range(2):
#     vector = []
#     for j in range(3):
#         vector.append(j)
#     mat.append(vector)
# print(mat)

# transpose_matrix = []
# matrix = [[2, 4, 6], [1, 2, 4], [3, 7, 1], [2, 7, 1]]
# for i in range(len(matrix[0])):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose_matrix.append(transpose_row)
# print(transpose_matrix)

# users = ["ahmad", "bilal", "anas", "khalil"]
# b = []
# for a in users:
#     b.append(a.upper())
# print(b)

# users = ["ahmad", "bilal", "anas", "khalil"]
# b = [a.upper() for a in users]
# print(b)
# def bubble_sort(data):
#     for i in range(len(data)):


# data = [26, 10, 65, 9,87]
# print(bubble_sort(data))
# m = "zorain"
# print(list(m))

# students = [
#     {"name": "Ahamd", "age": 24},
#     {"name": "bilal", "age": 25},
#     {"name": "Ali", "age": 28},
# ]


###using user define function
# def increase_age(student: dict):
#     student["age"] += 1  # for adults logic > 25 --> if student["age"]>=25:
#     return student

# for adults logic > 25
# def adult_age(student: dict):
#     if student["age"] >= 25:  # for adults logic > 25 --> if student["age"]>=25:
#         return student


# print(increase_age(students[1]))

##### for for loop
# student_record = []
# for student in students:
#     student_record.append(increase_age(student))
# print(student_record)

##### using map function
# print(list(map(increase_age, students)))

############ using filter function
# print(list(filter(adult_age, students)))


# data = [
#     {"key1": 10, "key2": 20},
#     {"key1": 20, "key2": 40},
#     {"key1": 50, "key2": 60},
# ]


# def func():
#     return 'Hello'
# class Product:  # pascal approch fo defning class
#     pass
# p1 = Product()      # constructor calling
# print(p1)


# class Enroll:
#     def __init__(self, student_name):
#         self.name = student_name
#         self.courses = []

#     def add_courses(self, course_name):
#         return f" Name: {self.name}, Courses: {self.courses.append(course_name)}"
#         # self.courses.append(course_name)


# anas = Enroll("Anas")

# Fahad = Enroll("Fahad")

# # anas = Enroll.add_courses("DSA")
# anas.add_courses("DSA")
# Fahad.add_courses("ML")

# print(anas.courses)
# print(Fahad.courses)


# python OOP
# example-1
# class myclass:
#     pass
# print(myclass())     # object creation and creating memory alocation
# print(myclass) # providing reference
# num_1,num_2=input('enter_numbers:')
# print()

# message = "From ali@outlook.com Mon 10:01 AM"
# z=message.split()
# print(z[1][3:])

