'''
n=int(input("Enter a number:"))        #if this is comented the it will run except block
try:
    print(n)
except:
    print("n is not defined")    #if any error in the program the it will print except block ie., error sentence
'''

           #To copy the data from source.txt file to destination.txt file
try:                                
    f=open("D:\Python\File_handling.py\source.txt","r")           #Create a file named source.txt and add some data to it and then make a copy in the destination.txt file
    data=f.read()
    f.close()
    d=open("D:\Python\File_handling.py\destination.txt","w")
    d.write(data)
    d.close()
    print("Contain copied sucessfully")
except:
    print("file not exist")
      