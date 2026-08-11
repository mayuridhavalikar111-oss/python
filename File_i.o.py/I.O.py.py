                                                           #READING A FILE
f=open("D:\Python\File_i.o.py\demo.txt","r") #Oppening file demo

'''#To read all data in demo file.
data=f.read()
print(data)'''

'''#To read only first 5 characters of data in demo file.
data1=f.read(5)
print(data1)'''

#To read first line in the demo file.
line1=f.readline()
print(line1)

#To read second line in the demo file.
line2=f.readline()
print(line2)
f.close() #Closing file demo.





                                                         #WRITING TO A FILE
f=open("D:\Python\File_i.o.py\demo.txt","w") #File in write mode.(w)
f.write("I am Mayuri") #This will overwrite the current data in file demo.

f=open("D:\Python\File_i.o.py\demo.txt","a")#File in append mode.(a)
f.write("\nI am learning Python From ApanaCollege")#This will append the data too existing data in file demo.

f.close() #Closing file demo.





                                                          #r+, w+ & a+
#Trunckted- The data gets completely deleted.

f=open("D:\Python\File_i.o.py\demo.txt","r+") 
        # r+ is open for reading and overwriting . (file is not Trunckted)
f.write("abc") #r+ will overwrite the existing starting characters of the data.

f=open("D:\Python\File_i.o.py\demo.txt","w+") 
        # w+ is open for reading and overwriting. (file is Trunckted)
f.write("abc") #w+ will delete the existing data and print the new one.

f=open("D:\Python\File_i.o.py\demo.txt","a+") 
        # a+ is open for reading and appending.(file is not Trunckted) 
f.write("abc") #a+ will append to the excisting at the end of the data.

f.close()





                                                      #WITH SYNTAX
# with syntax will automatically closes the file , therefore it is not compulsory to close file at the end.
with open("D:\Python\File_i.o.py\demo.txt","r") as f:
    data=f.read
    print(data)

with open("D:\Python\File_i.o.py\demo.txt","w") as f:
    data=f.write("This is Mayuri")  #Overwriting the existing data
    print(data)






                                              #DELETING A FILE
import os
'''os.remove("D:\Python\File_i.o.py\demo.txt")'''






                                        #PRACTICE QUESTIONS
#Q. Create a file "practice.txt"
with open("D:\Python\File_i.o.py\practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("Using Java!\nI like programming in Python.")


#Q. Replace all occurrences pf "Java" with "Python" in above file.
with open("D:\Python\File_i.o.py\practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("D:\Python\File_i.o.py\practice.txt","w") as f:
    f.write(new_data)


#Q. Search if the word "Python" exists in the file or not?
def check_for_word(): #using function
    word="Python"
    with open("D:\Python\File_i.o.py\practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("Found")
        else:
            print("Not Found")


#Q> Write a function to find in which line of the file does the word "learning" occur first.

def check_for_line():
    w="learning"
    data=True
    line_no=1
    with open("D:\Python\File_i.o.py\practice.txt","r") as f:
          while data:
            data=f.readline()
            if(w in data):
                  print(line_no)
                  return
            line_no+=1
    return-1
check_for_line()

#Q. From a file containing numbers separted by commas, print the count of even numbers.
with open("D:\Python\File_i.o.py\practice1.txt","w") as f:
    f.write("12,34,5,2,36,78,45,21,28")
with open("D:\Python\File_i.o.py\practice1.txt","r") as f:
    data=f.read()
    print(data)
#TYPE 1:
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]
#TYPE 2:
count=0
nums=data.split(",")
for val in nums:
    if(int(val)%2==0):
        count+=1

print("Total number of even numbers in the give data is:",count)