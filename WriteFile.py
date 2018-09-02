'''
Developed by: Hrushikesh Behera
Code to read a text file
'''

'''
The following are the modes in which files can be accessed:

MODES           || NOTATION USE || FILE OPENING MODE || HANDLE POSITION    || COMMENTS 
----------------++--------------++-------------------++--------------------++------------------------
Read Only          r                 reading             beginning of file    Default mode of file open
                                                                              If file doesnot exists, raises I/O error
Read and Write     r+               reading & writing    beginning of file    raises I/O error if file doesnot exists
Write Only         w                writing              beginning of file    existing file-->data is truncated and over written
                                                                              Creates a file if file doesnot exists
Write and read     w+               reading and writing  beginning of file    existing file: data is truncated and over written
Append Only        a                writing              end of the file      creates a file if doesnot exist
                                                                              New data being written will be inserted at end after existing data
Append and read    a+               reading and writing  end of file          Creates a file if doesnot exists
                                                                              New data being written will be inserted at end after existing data
'''

#opens test.txt

#write() : Inserts the string str1 in a single line in the text file.
#writelines() : For a list of string elements, each string is inserted in the text file.
# Used to insert multiple strings at a single time.

file1 = open(r"writetest.txt","w")

file1.write("Congrats \n You can now use this code to integrate in other code and write your output")
L = ["\nline 01","\nline 02"]

file1.writelines(L)