fileptr = open("myfile.txt", "x")

print('file_pointer', fileptr)

if fileptr:
    print("file is created successfully")
    print("Filename:", fileptr.name)
    print("Mode:", fileptr.mode)
    print("Is Closed?", fileptr.closed)

fileptr.close()

print("Is Closed?", fileptr.closed)
