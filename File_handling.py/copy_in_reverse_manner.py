def reverse():
    f_input=open(r"D:\Python\File_handling.py\file.txt", "r")
    lines = f_input.readlines()
    f_input.close()

    f=open(r"D:\Python\File_handling.py\ex2.txt", "w")
    f.writelines(lines[::-1])
    f.close()

reverse()
