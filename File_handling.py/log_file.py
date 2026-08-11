#Create a sample log file access.log containing records of web server access logs (timestamp, IP address, URL).
f=open("access.log","w")
f.write("2020-3-13 2:15:4 192:168:1:10 /home\n")
f.write("2020-3-13 2:10:3 192:168:1:15 /about\n")
f.write("2020-3-13 2:10:5 192:168:1:10 /contact\n")
f.write("2020-3-13 2:10:2 192:168:1:20 /login\n")
f.close()

f=open("access.log","r")        
ip_list=[]
for i in f:
    ip= i.split()
    print(ip)
    ip_list.append(ip[2])
print(ip_list)
f.close()

unique=set(ip_list)    #Write a Python program to extract and display all unique IP addresses
print(unique)

#Count the number of occurrences of each IP address.