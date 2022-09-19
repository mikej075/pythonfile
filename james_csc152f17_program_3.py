#Michael James
#12/15/17
#csc 152

def main():
    #1 Define variables
    linecount = 0
    wordcount = 0
    charcount = 0
    words = []
    #1.1 Open file
    _file = open(f, 'r')
    #1.2 Loop each line
    for line in _file:
        linecount += 1
        word = line.split()
        words += word
    #1.3Loop through all words 
    for word in words:
        wordcount += 1
        #1.4Loop through words for characters
        for char in word:
            charcount += 1
    
    return (linecount, wordcount, charcount)
#1.5Name of the file
files = int(input("how many files would you like to enter:"))

if (files <= 0):
    print int(input("enter positive number only:"))
        
fname = raw_input('Enter the name of the file to be used: ')
#2 print fileCount
lineCount, charCount, wordCount = fileCount(fname)
print "There are", lineCount, "lines in the file."
print "There are", charCount, "characters in the file."
print "There are", wordCount, "words in the file."

main()