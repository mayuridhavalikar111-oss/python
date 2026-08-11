#CSV file stands for -comma saperated values
import csv
f=open("D:\Python\File_handling.py\data.csv","w",newline="")  #the newline="" will remove the extra line from CSV module.
writer=csv.writer(f)                            #To Insert 5 records into the file.
writer.writerow(["ID","Name","Age"])
writer.writerow([1,"ABC",30])
writer.writerow([2,"XYZ",28])
writer.writerow([3,"PQR",25])
writer.writerow([4,"IGF",23])
writer.writerow([5,"MNO",22])
f.close()

f=open("D:\Python\File_handling.py\data.csv","r")      #To Read and display the contents of the CSV file.
reader=csv.reader(f)
for row in reader:
    print(row)
f.close()

search_id=input("Enter ID to be searched:")                #To Search and display a specific record by ID.
f=open("D:\Python\File_handling.py\data.csv","r")
reader=csv.reader(f)
next(reader)
found=False
for i in reader:
    if i[0]==search_id:
        print("Found",i)
        found=True
        break
if not found:
    print("Not found")

Name=input("Enter Name to be searched:")                #To Search and display a specific record by NAME.
f=open("D:\Python\File_handling.py\data.csv","r")
reader=csv.reader(f)
next(reader)
found=False
for i in reader:
    if i[1]==Name:
        print("Found",i)
        found=True
        break
if not found:
    print("Not found")
