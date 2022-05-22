import os


def files_locator(dir, extension):
    # list of strings containing files names in the specified directory /to_send
    directory_content = os.listdir(dir)
    # list of strings containing text file names in the directory
    files = []
    for file in directory_content:
        if file.endswith(extension):
            files.append(file)
    # initialize an empty list to store modification times of text files
    sec = []
    # for loop to get each file creation time
    for csv_items in files:
        modTimesinceEpoc = os.path.getmtime(csv_items)
        sec.append(modTimesinceEpoc)
    # print(sec)
    # initialize temporary variables int and str respectively to use in sorting
    tempInt = 0
    tempStr = ''
    # int to store the number of text files
    number_of_csv = len(files)
    # bubble sorting for loop to sort the file name according to their creation time
    for index in range(number_of_csv-1):
        if sec[index] > sec[index+1]:
            tempInt = sec[index+1]
            tempStr = files[index+1]
            sec[index+1] = sec[index]
            files[index+1] = files[index]
            sec[index] = tempInt
            files[index] = tempStr
    return files  # number_of_csv
