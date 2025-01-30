import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
except Exception as err:
    print(err)
    print(f"Unexpected {err=}, {type(err)=}")

#input data while executing the code
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    #The use of the else clause is better than adding additional code 
    #to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        print("Hi")
        f.close()