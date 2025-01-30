#Whatever the file operation first we need to open the file by using the open function
#The open function need two parameters the file name(fullpath) and the file operation mode
# create_new_file = open('C:/VSCODE/Python-101/python101/Day5/textoutput.txt','w')
# input_to_file = "I'm input to the file"
# create_new_file.write(input_to_file)
# create_new_file.close()


#Reading the entire content of the file using read method ()
read_from_file = open('C:/VSCODE/Python-101/python101/Day5/textoutput.txt','r')
#The read method reads entire file content and store it in the variable
print(read_from_file.read())
read_from_file.close()

#Reading the file line by line using readlines method()
read_from_file = open('C:/VSCODE/Python-101/python101/Day5/textoutput.txt','r')
#The readlines method reads the file content line by line and store evry line as a value in the list
#example (["I'm input to the file\n", "I'm the second line"])
print(read_from_file.readlines())
read_from_file.close()

#Writing input to the file
create_new_file = open('C:/VSCODE/Python-101/python101/Day5/textoutput1.txt','w')
input_to_file = """I'm input to the file
and a random string"""
create_new_file.write(input_to_file)
create_new_file.close()

#writing multiple lines to a file using writelines
create_new_file = open('C:/VSCODE/Python-101/python101/Day5/textoutput1.txt','w')
multiple_lines = ["1","2","3","4","5","6","7","8"]
create_new_file.writelines(multiple_lines)
create_new_file.close()


#With Statement in Python
#with statement is used for resource management. It ensures that file is properly closed after its suite finishes, 
#even if an exception is raised. with open() as method automatically handles closing the file once the block of code is exited, even if an error occurs. 
#This reduces the risk of file corruption and resource leakage.

try:
    with open("geeks.txt", "r") as file:
        content = file.read()
        print(content)
except  FileNotFoundError as e :
    print (e)

