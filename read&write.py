'''
Created on Feb 29, 2020

@author: ITAUser
'''
#read&write - mod name

#basic concepts
#open file - open()

file1 = "fileName.txt", "mode"

#mode r: read, w: write, a: append r+: special case

#read - read(), readLine() - stores value as a string
#write - write()

#Create a new file
    file1 = open("hello.txt", "a")
    file1.close()
    
#write to the file
    string = "hello my name is Chokyi"
    file1.write(string)
    
#write multiple lines
    line = ["dogs ", "are ", "cool " ]
    file1.writeLines(line)
    file1.close()
    
#read file
    file1.open("hello.txt", "r")
    text = file1.read()
    file1.close()
    
    print(text)
    
    


