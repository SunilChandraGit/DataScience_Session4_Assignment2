#define a function to check for vowel
def isVowel(ch):
    
    #define and initialize list of vowels
    vowels = ['a','e','i','o','u']
    
    #return true if ch is in vowels list else return false
    if ch in vowels:
        return True
    else:
        return False
    
#call isVowel and check whether e is vowel or not
print(isVowel('e'))
