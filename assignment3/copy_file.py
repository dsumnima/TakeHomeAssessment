'''
Program: Copy content from one file to another using exception handling
'''

def copy_file():
    try:
        source = input("Enter source file name: ")
        destination = input("Enter destination file name: ")

        with open(source, "r") as f1:
            data = f1.read()

        # 'x' mode prevents overwriting
        with open(destination, "x") as f2:
            f2.write(data)

        print("File copied successfully!")

    except FileNotFoundError:
        print("Error: Source file does not exist.")
    except FileExistsError:
        print("Error: Destination file already exists.")

copy_file()
