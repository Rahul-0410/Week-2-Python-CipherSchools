# list 
# numbers=[1,2,3,4,5]
# print(numbers)
# words=["word1","word2","word3"]
# print(words)
# mixed=[1,2,3,4.4,0.1,"eight","Rahul"]
# mixed[1]="two"
# print(mixed)

# adding data to list 

# fruits=['grapes','orange']
# print(fruits)
# fruits.append('mango')
# print(fruits)
# fruits=[]
# fruits.append('mango')
# fruits.append('apple')
# fruits.append('orange')
# print(fruits)
# fruits1=['mango','orange']
# fruits1.insert(1,'grapes')
# print(fruits1)
# fruits2=['apple','grapes']
# fruits=fruits1+fruits2
# print(fruits)
# fruits1.extend(fruits2)
# print(fruits1)
# print(fruits2)

# fruits=['orange','apple','pear','banana','kiwi']
# fruits.pop(1)
# print(fruits)
# del fruits[1]
# print(fruits)
# fruits.remove('banana')
# print(fruits)

# if 'apple' in fruits:
#     print('apple is present')
# else:
#     print('apple is not present')
# fruits=['orange','apple','pear','banana','kiwi','apple','banana']
# print(fruits.count('apple'))
# fruits.sort()
# print(fruits)

# numbers=[3,5,1,9,10]
# numbers.sort()
# print(numbers)
# print(sorted(numbers))
# numbers.clear()
# print(numbers)
# numbers_copy=numbers.copy()
# print(numbers_copy)

# copare lists
# fruits1=['orange','banana','pear']
# fruits3=['orange','banana','pear']
# fruits2=['apple','kiwi','pineapple']
# print(fruits1==fruits2)
# print(fruits1==fruits3)
# print(fruits1 is fruits3)

#split method 
# user_info='harshit, 24'.split(',')
# print(user_info)
# join method 
# user_info=['harshit','24']
# print(','.join(user_info))

# list vs strings
# s="string"
# t=s.title()
# print(t)
# print(s)

# l=['word','word2','word3']
# l.pop()
# print(l)
# loops in lists 
# fruits=['orange','apple','pear','banana','kiwi']
# for fruit in fruits:
#     print(fruit)
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# list inside list
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1])
# for sublist in matrix:
#     for i in sublist:
#         print(i,end='')

# print(matrix[1][::-1])


# numbers=list(range(1,11))
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# numbers.pop()
# print(numbers)
# print(numbers.index(2))
# def negative_list(l):
#     negative=[]
#     for i in l:
#         negative.append(-i)
#     return negative
# print(negative_list(numbers))

# list excercise
# numbers=list(range(1,11))
# def square_list(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square
# print(square_list(numbers))

# def reverse_list(l):
#      l.reverse()
#      return l

# def reverse_list(l):
#     return l[::-1]

# def reverse_list(l):
#     r_list=[]
#     for i in range(1,len(l)+1):
#         popped_item=l.pop()
#         r_list.append(popped_item)
#     return r_list
# numbers=[1,2,3,4,5]
# print(reverse_list(numbers))

# def reverse(l):
#     r_list=[]
#     for i in range(len(l)):
#         popped_item=l.pop()
#         r_list.append(popped_item[::-1])
#     return r_list[::-1]
# str=['abc','tuv','xyz']
# print(reverse(str))

def reverse_elements(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements

str=['abc','tuv','xyz']
print(reverse_elements(str))


# def filter_odd_even(l):
#     odd_nums=[]
#     even_nums=[]
#     for i in l:
#         if i %2==0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#     output=[odd_nums,even_nums]
#     return output

# nums=list(range(1,11))
# print(filter_odd_even(nums))


# def common_elements(l1,l2):
#     output=[]
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print(common_elements([1,2,5,8],[1,2,7,6]))

# numbers=[6,60,2]
# print(min(numbers))
# print(max(numbers))
# def greatest_diff(l):
#     return max(l)-min(l)

# print(greatest_diff(numbers))

def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

mixed=[1,2,3,[2,3],[1,2]]
print(sublist_counter(mixed))






