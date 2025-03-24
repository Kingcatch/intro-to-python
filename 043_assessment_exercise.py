#These are the functions I was requried to create for the Maker's Assessment:

#Function to convert a number of minutes into an hours:minutesds style format.

def time_conversion(num):

    hours = num // 60
    minutees = num % 60
    return f"{hours}:{minutees}"

#test cases

print(time_conversion(126))
print(time_conversion(45))
print(time_conversion(200))

#Function to find the longest word in a string. The function should also remove punctuaction and if multiple words have the same length, it shoukd return the first one.

def longest_word(sen):
    words = sen.split()
    cleaned_words = ["". join(char for char in word if char.isalnum()) for word in words]
    return max(cleaned_words, key=len)

#test cases

print(longest_word("fun&!! time"))
print(longest_word("I love dogs and cats"))
print(longest_word("The longest word here is..."))

#Functions to return the sum of numbers in a list up to a given number
#two approaches: one incorparting a loop method and another using mathematics

def sum_to_num(num):
    return sum(range(1, num + 1))

def sum_to_num_formula(num):
    return num * (num + 1) // 2

print(sum_to_num(10))
print(sum_to_num_formula(20))
print(sum_to_num(100))
print(sum_to_num_formula(200))