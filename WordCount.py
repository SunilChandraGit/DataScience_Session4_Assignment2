'''Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.'''

#define function that takes list of words 'lis' as parameter
#and returns list of character count in words
def getWordLength(lis):
    
    #use lambda and map to get list of integers of length of words
    x=map(lambda x:len(x), list1)
    
    #return word count list
    return x

#declare and initialize list of words
list1=["SunilKumar", "Rajesh", "Ramu", "Shyam"]

#convert map object to list and print it
print(list(getWordLength(list1)))