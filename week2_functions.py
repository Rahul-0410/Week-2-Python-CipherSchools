# def add_two(a,b):
#     return a+b
# total= add_two(5,5)
# print(total)
# print(add_two(5,4))
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print(add_two(a,b))
# a=str(input("Enter first number: "))
# b=str(input("Enter second number: "))
# print(add_two(a,b))
# print vs return
# def add_three(a,b,c):
    # return a+b+c 
    #  print(a+b+c)
# print(add_three(5,5,5))
# add_three(5,5,5)
# def last_char(name):
#     return name[::-1]
# print(last_char("Rahul"))

# def odd_even(num):
#     if num%2==0:
#         return "even"
    # else:
    #     return "odd"
#     return "odd"
# print(odd_even(10))

# def is_even(num):
#     if num%2==0:
#         return "True"
#     # else:
#     return    "False"
# print(is_even(8))

# def is_even(num):
#     return num%2==0
# print(is_even(8))

# def song():
#     return "happy birthday"
# print(song())


# excercise 1
# def which_is_greater(a,b):
#     if a>b:
#         print(f"{a} is greater than {b}")
#     else:
#         print(f"{b} is greater than {a}") 
# a=int(input())
# b=int(input())
# which_is_greater(a,b)
# 

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(greatest(50,40,30))
# function inside a function

# def greater(a,b):
#     if a>b:
#         return a
#     return b

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# def newgreatest(a,b,c):
#     # bigger=greater(a,b)
#     # return greater(bigger,c)
#     return greater(greater(a,b),c)

# print(newgreatest(1000,200,30))

# excercise 2
# def is_palindrome(word):
#     reversed_word= word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
# def is_palindrome(word):
#     # if word == word[::-1]:
#     #     return True
#     # return False
#     return word== word[::-1]
# print(is_palindrome("naman"))
# print(is_palindrome("horse"))

#fibbonacci series
# def fibonnaci_seq(n):
#     a=0   #first number
#     b=1   # second number
#     if n==1:
#         print(a)
#     elif n ==2:
#         print(a,b)
#     else:
#         print(a,b , end=" " )
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(b,end=" ")

# fibonnaci_seq(20)

#default parameters
# def user_info(first_name,last_name='unknown',age=20):
# # def user_info(first_name,last_name='unknown' , age):
#     print(f"Your first name is {first_name}")
#     print(f"Your last name is {last_name}")
#     print(f"Your age is {age}")

# user_info('Rahul','Gupta',20)

#scope
# x=5 # global variable
# def func():
#     global x
#     x=7
#     return x

# def func2():
#     print(x)
# func2()
# print(func())
# # print(x)
# def sayhello(*,name,age):
#     print("Hello",name,age)
# names=["ram","Sham","Rahul"]
# for item in names:
#     sayhello(name=item, age=40)

# def sayhello():
#     return "Hello,How are you?"
# print(sayhello())
def sum(a,b):
    c= a+b
    return c
a=10
b=20
print(sum(a,b))

d="Hello"
for i in d:
    print(i,end='')