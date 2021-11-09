def SwapFileData():
    file1 = input("Enter your first file name:-")
    file2 = input("Enter your second file name:-")

    a=open(file1,'r')
    data_a = a.read()

    b=open(file2,'r')
    data_b = b.read()

    a=open(file1,'w')
    a.write(data_b)

    b=open(file2,'w')
    b.write(data_a)

SwapFileData()