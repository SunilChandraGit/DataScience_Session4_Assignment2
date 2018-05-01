'''Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.'''

#declare and initialize list of words
list1=["SunilKumar", "Rajesh", "Ramu", "Shyam"]

#use lambda and map to get list of integers of length of words
x=map(lambda x:len(x), list1)

#convert map object to list and print it
print(list(x))