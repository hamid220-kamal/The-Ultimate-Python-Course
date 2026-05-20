#importing the os module to work with the operating system
import os 

#directory path to list the contents of
directory_path = '/users'

content = os.listdir(directory_path)

#printing the contents of the directory

print(content)