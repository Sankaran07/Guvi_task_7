# 1) Write a Python program using Function to which will do the following:-
# a. The function will create a text file with the current timestamp.
# b.) The file content should have the content of the current timestamp.


# You can create a Python program to achieve this using the datetime module to get
# the current timestamp and write it to a text file. Here's a sample program,

import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate a unique file name based on the timestamp
    file_name = f"timestamp_{current_time.replace(' ', '_').replace(':', '-')}.txt"

    # Create and write the timestamp to the file
    with open(file_name, 'w') as file:
        file.write(current_time)

    return file_name

if __name__ == "__main__":
    file_name = create_timestamp_file()
    print(f"File '{file_name}' created with the current timestamp.")
# This program defines a function create_timestamp_file that does the following:

# Gets the current timestamp using the datetime module.
# Formats the timestamp into a string with a suitable format.
# Generates a unique file name based on the timestamp.
# Creates a text file with the generated file name and writes the current timestamp into it.
# When you run this program, it will create a text file with the current timestamp in the same directory 
# where the script is located.

print('****'*20)

# 2) Write another Python function to read from a text file.
# The function will take the name of the text file and display 
# the content of the file into the console.


# You can create a Python function to read the content of a text file and display it in the console.
#  Here's a function,

def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the text file to read: ")
    read_text_file(file_name)
# This function, read_text_file, takes the name of the text file as an argument and attempts to read and display its content. Here's how it works:

# It opens the file with the given name in read mode ('r').
# Reads the content of the file and stores it in the content variable.
# Prints the content to the console.
# The try and except blocks are used to handle potential errors, such as the file not being found or any other exceptions that may occur during file reading.

# In the example if __name__ == "__main__": block,
# the program prompts the user to enter the name of the text file they want to read and then calls
# the read_text_file function with the provided file name.