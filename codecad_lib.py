#!/usr/bin/python

#This is Diego's codecademy library of completed/working functions



def is_prime(x):
    '''This function checks if a number is a prime number'''
    if x==0 or x==1 or x<2:#All numbers less than 2 are not prime
        return False
    elif x==2:#2 is a prime number but needs own condition because our range must include 2
        return True
    else:#For any number greater than 2
        for n in range(2,x):#Iterate through every number from 2 to less than number in question x
            print x%n
            if x%n == 0:#If any of the remainders are 0 (indicating even division), end loop, can't be prime
                return False
        return True#If it iterates through all the way without remainder 0, it is prime!
		
def anti_vowel(text):
    '''This function will return the input text without any upper or lower case vowels'''
    vowel= ['a','e','i','o','u','A','E','I','O','U']#Define list of vowels
    new_text= ''#Initialize output string
    for i in range(0,len(text)):#Set loop to iterate through every character in text
        if text[i] not in vowel:#Check if text[i] is in library of vowels, if not, add to output string
            new_text= new_text + text[i]
    return new_text#Return output string
	
def scrabble_score(word):
    '''Function returns score of word, single words without punctuation only'''
    #Define dictionary full of scores for letters
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
    word= word.lower()#Turn all characters of input int valid case to match dictionary
    acceptable= score.keys()#Make a list of all keys
    total_score= 0#Initialize total score
    for i in range(0,len(word)):#Loop through all characters in input word
        if word[i] not in acceptable:#Check that all characters are in list of acceptable characters
            print 'Not acceptable word. Single words without punctuation please'#If not stop and return None
            return None
        else:#If acceptable, add score of character to total score
            total_score= total_score + score[word[i]]
    return total_score	

def censor(text,word):
    '''This function replaces word in text with asterisks of the same length as word'''
    
    word_len= len(word)#Get length of word
    placeholder= '*'*word_len#Make place holder with asterisks same length as word
    
    if word not in text:#Check if occurrences of word in string
        print 'Try new word'#If not, return nothing
        return None
    else:#If there are occurrences of word
        text_list= text.split()#First split string into a list of strings
        for i in range(0,len(text_list)):#Enumerate text list
            if text_list[i]== word:#If item = censored word
                print 'Modifying list'
                text_list[i]= placeholder# Replace item with placeholder
        
        text_list= ' '.join(text_list)# Redefine text_list by joining text_list items with a space
        return text_list#Return text with censors

def count(sequence,item):
    '''This function turns sequence into list and counts occurrences of item in this list'''
    counter= 0
    if type(sequence)== list:#Check data type, if list we'll just iterate through list and count items in list
        for i in range(0,len(sequence)):
            print i, sequence[i], item#Just doublechecking
            if sequence[i] == item:
                counter+= 1#Add 1 every time it finds item
    else:
        list1= sequence.split()#If not a list, turn sequence into a list and do the same as above
        for i in range(0,len(list1)):
            print i, list1[i], item
            if list1[i] == item:
                counter+= 1
    return counter
    print counter
	
def purify(number_list):
    '''This function removes all odd numbers from list and returns new list with even numbers'''
    even_list= []#Initialize empty even list
    for i in range(0,len(number_list)):#Iterate through original list
        if number_list[i]%2==0:#Any element in list that has a remainder that equals zero is even
            even_list.append(number_list[i])#Append all even elements to even list
    return even_list

def product(input_list):
    '''This function takes list of integers and returns product of the list'''
    total= 1#Initialize total variable, 1 works cause it can't be smaller than the smallest element
    for i in range(0,len(input_list)):#Iterate through list
        total= total*int(input_list[i])#Multiply current total by integer form of element i
    return total	
	
def remove_duplicates(list1):
    '''Function removes duplicates'''
    unique= []#Initialize list of unique entries
    
    for i in range(0,len(list1)):#Iterate through list
        if list1[i] not in list1[0:i]:#At every entry, check if entry is in previous entries
            unique.append(list1[i])#If not, add it to unique list
    return unique#Return unique
            