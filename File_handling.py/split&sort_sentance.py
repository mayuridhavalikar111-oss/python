#Program to split the sentance in the file called story.txt.
f=open("D:\Python\File_handling.py\story.txt","w")   
f.write("Welcome to CTP lab or python lab")              #To write the data in the file story.txt file
f.close()

f=open("D:\Python\File_handling.py\story.txt","r")
data=f.read()
print(data)             
f.close() 

words=data.split()            #To split the sentence or text in words and it will form a dictionary of those words.
print(words)     

dict={}                         #To find frequencies and in descending order of frequency.
for i in words:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
sorted_words=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(sorted_words)





#Program for data with special symbols in the file story.txt.(!,@,#,$,%,etc)
import string
f=open("D:\Python\File_handling.py\story.txt","w")   
f.write("Welcome to CTP lecture @  python lab !")         #data with punctuation      
f.close()

f=open("D:\Python\File_handling.py\story.txt","r")
data=f.read()
print(data)             
f.close() 

for ch in string.punctuation:           #This will replace the punctuation marks with nothing.
    data=data.replace(ch," ")

words=data.split()            
print(words)     

 #Write a Python program to read contents of a file and write all contents in uppercase into another file. 

with open("input.txt", "r") as f:
    data = f.read()

with open("output.txt", "w") as f:
    f.write(data.upper())

print("Content converted to uppercase.")


 