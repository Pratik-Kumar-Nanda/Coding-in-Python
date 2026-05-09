"""
list_tuples.py

Practice examples for lists and tuples in Python.
Includes tuple unpacking and list manipulation.
"""

# --------------------------------------------
# Favourite Movies Input
# --------------------------------------------

# print("Tell us your 3 favourite movie.")
# movie_1 = input("Enter 1st movie name: ")
# movie_2 = input("Enter 2nd movie name: ")
# movie_3 = input("Enter 3rd movie name: ")

# movies = [movie_1, movie_2, movie_3]
# print(movies)


# --------------------------------------------
# Palindrome Check
# --------------------------------------------

# numbers = [1, 2, 1]
# copied_numbers = numbers.copy()
# copied_numbers.reverse()

# if numbers == copied_numbers:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# --------------------------------------------
# Grade Counter and Sorting
# --------------------------------------------

# marks = ['A', 'B', 'C', 'D', 'A', 'A', 'B']
# print("The number of students with grade A:", marks.count('A'))

# marks.sort()
# print(marks)


# --------------------------------------------
# Tuple Unpacking Example
# --------------------------------------------

data = (1, 2, 3, 4)

a, *b, c = data

for i in range(len(b)):
    b[i] = b[i] + a
    a += b[i]

print(a)
print(b)
print(c)