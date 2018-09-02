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

file1 = open(r"test.txt","r")
'''
r is placed before filename to prevent the characters in filename string to be treated 
as special character. For example, if there is \temp in the file address, then \t is 
treated as the tab character and error is raised of invalid address. The r makes the 
string raw, that is, it tells that the string is without any special characters. 
The r can be ignored if the file is in same directory and address is not being placed.
'''
#read(n): Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
readOP = file1.read()
print("O/P for read: " + readOP)
file1.seek(0)

'''
readline(n): Reads a line of the file and returns in form of a string.For specified n,
 reads at most n bytes.
However, does not reads more than one line, even if n exceeds the length of the line.
'''
readlineOP = file1.readline()
print("O/P for readline: " + readlineOP)
file1.seek(0)

#readlines() : Reads all the lines and return them as each line a string element in a list.
readlinesOP = file1.readlines()
print("O/P for readlines: " + str(readlinesOP))
file1.close()
