import employee
import os


def cls():
    """To clear screen."""
    os.system("cls" if os.name == "nt" else "clear")


def get_last_record():
    try:
        search = "Record"
        record_count = 0
        record_number = open("employee.txt", "r")
        for line in record_number.readlines():
            if search in line:
                record_count += 1
        record = record_count + 1
        record_number.close()

        return record

    except IOError:
        print """ please make employee.txt in
         the directory you are running this program from .. """


to_run = "Y"
while to_run == "Y":
    print "please select one of the following  : \n\n\n"
    print " 1- enter employee data ."
    print " 2- display employee data ."
    print " 3- display the last record .\n\n"
    selector = raw_input("what is your selection ? :\n\n")
    cls()
    if selector == "1":
        employee_record = get_last_record()
        employee_name = raw_input("Please enter the employee name : \n ")
        employee_age = raw_input("the age : \n")
        employee_salary = raw_input("the salary :\n")
        employee_email = raw_input("email of employee : \n")
        employee_departement = raw_input("department : \n")
        employee_place_of_department = raw_input("place : \n")
        new_employee = employee.Employee(employee_record, employee_name, employee_age, employee_salary, employee_email, employee_departement, employee_place_of_department)
        employee.Employee.write_info(new_employee)
    if selector == "2":
        reader = open("employee.txt", "r")
        print "\n\n\n"
        print "the database file contains the follwing .... \n\n\n\n\n {0}".format(reader.read())
        reader.close()

    if selector == "3":
        print "\n\nlast record is : {0}".format((get_last_record() - 1))
    to_run = raw_input("do you want the program to run again ?").upper()
    cls()
    print "\n\n\n\t\t\t\t######## ** thanks for using our program... ** ########\n\n\n\n"
