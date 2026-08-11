f=open("D:\Python\File_handling.py\example.txt","r")    #r mode for reading file
print(f.read())             #It will print the data present in the file
f.close()                    #to close the file

f=open("D:\Python\File_handling.py\example.txt","w")    #w mode for writing in the file
f.write("Welcome to the file")    #This will overwrite all the data in the file
f=open("D:\Python\File_handling.py\example.txt","r")
print(f.read())
f.close()

f=open("D:\Python\File_handling.py\example.txt","a")    #a mode for appending the data in the file
f.write("Hello")             #use f.write for append mode
f=open("D:\Python\File_handling.py\example.txt","r")    #Again r mode to read the appended data in the file
print(f.read())
f.close()

with open("D:\Python\File_handling.py\example.txt","r")as file:    #Method 2:to open the file. With this method their is no need to close the file by f.close() method.
    print(file.read())
