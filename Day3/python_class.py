# Creating a Basic class
class student:
    # A class variable is like a constatnt property for the entire student class an example is School Name
    school_name = "Bhashyam"

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        # Accessing Variables: Class variables can be accessed via the class name (classname.classvariable) or an object (objectname.classvariable). Instance variables are accessed via the object (objectname.instancevariable).
        # Accessed the school variable using class name
        return f"Student with Id {self.id} in {student.school_name} has name {self.name} and age is {self.age}"

    # Instance Method which will take self as an attribute and it always needs to be pointed out to an object pointer
    def age(self):
        return f"student age is self.age"

        # Class Method

    def class_method():
        return "I'm a class method"

    # They don't operate on an instance or the class itself,They are often used for utility functions that don't need access to class or instance data.
    @staticmethod
    def static_method():
        return f"I'm just a static method and you can call me using my classname (student.class_method)"


# Gather a list of students from user and output them


print(
    f"\n Accessing a class variable using classname.classvariablename and the value is{student.school_name}"
)
try:
    print(f"\n {student.class_method()}")
except TypeError as e:
    print(
        f"\n You can expect a error while accesing the classmethod using classname as it needs a self paramter and the error is '{e}' which means it needs a pointer"
    )


def student_list():
    Number_students = int(
        input(f"Number of students you want to add to the databases: ")
    )
    try:
        if isinstance(Number_students, int) == True:
            while Number_students > 0:
                print("\n Adding a student in database: ")
                added_t_db = student_add(str(Number_students))
                if added_t_db == None:
                    pass
                # Check the object instance whether its is a student class or not
                elif isinstance(added_t_db, student):
                    print(str(added_t_db))
                    Number_students -= 1

        else:
            print("Wrong")
    except TypeError as e:
        print(e)


def student_add(id):
    studentdetails = tuple(
        input("\n Enter Student details as a comma seperated values:").split(",")
    )
    # print(studentdetails)
    if isinstance(studentdetails, tuple) and len(studentdetails) == 2:
        object_name = student(id, studentdetails[0], studentdetails[1])
        return object_name
    else:
        print(f"\n Wrong Input")


student_list()
